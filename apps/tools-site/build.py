#!/usr/bin/env python3
"""Builds the static site from src/ into public/.  Run: python3 build.py

src/styles/*.css        -> public/assets/site.css (tokens, base, layout, components, in that order)
src/scripts/*.js        -> public/assets/js/  (core.js + one file per module)
src/content/sections.py -> navigation, home directory, footer
src/content/tools/*.py  -> one page per entry (auto-discovered)
src/content/handlers.py -> which JS module each page needs
See ARCHITECTURE.md for how to add tools, sections, modules and layouts.
"""
import datetime, hashlib, html, importlib, json, os, pkgutil, re, shutil, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC, OUT = os.path.join(ROOT, "src"), os.path.join(ROOT, "public")
sys.path.insert(0, SRC)

from content.common import DOMAIN, BRAND, EMAIL, TOOLS_BASE, GOOGLE_SITE_VERIFICATION, ADSENSE_CLIENT  # noqa: E402
from content.sections import SECTIONS  # noqa: E402
from content.handlers import HANDLERS  # noqa: E402
from content import pages as STATIC  # noqa: E402
from content.guides import GUIDES  # noqa: E402
import content.tools as tools_pkg  # noqa: E402

TODAY = datetime.date.today().isoformat()
CSS_ORDER = ["tokens.css", "base.css", "layout.css", "components.css"]


def e(s):
    return html.escape(str(s), quote=True)


# ---------- load registry ----------
def load_tools():
    items = []
    for m in sorted(pkgutil.iter_modules(tools_pkg.__path__), key=lambda m: m.name):
        mod = importlib.import_module(f"content.tools.{m.name}")
        items.extend(getattr(mod, "TOOLS", []))
    live = [t for t in items if t.get("status", "live") == "live"]
    slugs, sec_ids = set(), {s["id"] for s in SECTIONS}
    for t in live:
        assert t["slug"] not in slugs, f"duplicate slug {t['slug']}"
        slugs.add(t["slug"])
        assert t["section"] in sec_ids, f"{t['slug']}: unknown section {t['section']}"
        assert t["tool"] in HANDLERS, f"{t['slug']}: handler {t['tool']} not mapped in handlers.py"
        t.setdefault("layout", "workbench")
    return live


TOOLS = load_tools()
BY_SLUG = {t["slug"]: t for t in TOOLS}
LIVE_SECTIONS = sorted([s for s in SECTIONS if any(t["section"] == s["id"] for t in TOOLS)], key=lambda s: s["order"])
SECTION = {s["id"]: s for s in SECTIONS}


# ---------- assets ----------
ASSET_V = {}


def build_assets():
    adir = os.path.join(OUT, "assets")
    if os.path.isdir(adir):
        shutil.rmtree(adir)
    os.makedirs(os.path.join(adir, "js"))
    css = "\n".join(open(os.path.join(SRC, "styles", f), encoding="utf-8").read() for f in CSS_ORDER)
    open(os.path.join(adir, "site.css"), "w", encoding="utf-8").write(css)
    ASSET_V["site.css"] = hashlib.md5(css.encode()).hexdigest()[:8]
    for f in os.listdir(os.path.join(SRC, "scripts")):
        if f.endswith(".js"):
            js = open(os.path.join(SRC, "scripts", f), encoding="utf-8").read()
            open(os.path.join(adir, "js", f), "w", encoding="utf-8").write(js)
            ASSET_V["js/" + f] = hashlib.md5(js.encode()).hexdigest()[:8]


def asset(path):
    return f"/assets/{path}?v={ASSET_V[path]}"


def tool_url(slug):
    return f"{TOOLS_BASE}/{slug}"


def link_tools(body):
    """Point in-content links like href="/heic-to-jpg" at the tool's current URL."""
    return re.sub(r'href="/([a-z0-9-]+)"', lambda m: f'href="{tool_url(m.group(1))}"' if m.group(1) in BY_SLUG else m.group(0), body)


# ---------- frame ----------
MARK = ('<rect x="2" y="2" width="28" height="28" rx="7" fill="#13294B"/>'
        '<path d="M9 11h14M16 11v12" stroke="#F2B705" stroke-width="3.2" stroke-linecap="round"/>'
        '<circle cx="9" cy="11" r="2.4" fill="#F2B705"/><circle cx="23" cy="11" r="2.4" fill="#F2B705"/>'
        '<circle cx="16" cy="23" r="2.4" fill="#F2B705"/>')
LOGO = f'<svg viewBox="0 0 32 32" aria-hidden="true">{MARK}</svg>'
FAVICON = "data:image/svg+xml," + html.escape(
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">{MARK}</svg>').replace("#", "%23")


def head(title, desc, path, ld=None, noindex=False, section=None, layout="article", canonical=None):
    url = DOMAIN + path
    canon = DOMAIN + (canonical or path)
    ld_html = "".join('<script type="application/ld+json">' + json.dumps(x, ensure_ascii=False) + "</script>" for x in (ld or []))
    nav = "".join(f'<a href="{TOOLS_BASE}#{s["id"]}">{e(s["nav"])}</a>' for s in LIVE_SECTIONS)
    extra = ""
    if GOOGLE_SITE_VERIFICATION:
        extra += f'<meta name="google-site-verification" content="{e(GOOGLE_SITE_VERIFICATION)}">\n'
    if ADSENSE_CLIENT:
        extra += (f'<meta name="google-adsense-account" content="{e(ADSENSE_CLIENT)}">\n'
                  f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={e(ADSENSE_CLIENT)}" crossorigin="anonymous"></script>\n')
    body_attrs = f' class="layout-{layout}"' + (f' data-section="{section}"' if section else "")
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canon}">
{'<meta name="robots" content="noindex">' if noindex else '<meta name="robots" content="index, follow, max-image-preview:large">'}
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canon}">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#13294B">
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Familjen+Grotesk:wght@500;600;700&family=Public+Sans:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{asset('site.css')}">
{extra}
{ld_html}
</head>
<body{body_attrs}>
<header class="site-head"><div class="wrap">
<a class="brand" href="/">{LOGO}<span>{BRAND}</span></a>
<nav class="nav" aria-label="Main">{nav}</nav>
</div></header>
"""


def footer():
    cols = ""
    for s in LIVE_SECTIONS:
        items = "".join(f'<li><a href="{tool_url(t["slug"])}">{e(t["short"])}</a></li>' for t in TOOLS if t["section"] == s["id"])
        cols += f"<div><h2>{e(s['name'])}</h2><ul>{items}</ul></div>"
    cols += ('<div><h2>About</h2><ul><li><a href="/about">About us</a></li><li><a href="/privacy">Privacy policy</a></li>'
             '<li><a href="/terms">Terms of use</a></li><li><a href="/contact">Contact</a></li></ul></div>')
    return f"""<footer class="site-foot"><div class="wrap">
<div class="foot-grid">{cols}</div>
<p class="foot-small">© {datetime.date.today().year} {BRAND}. All tools run in your browser. Your files are never uploaded.</p>
</div></footer>
"""


def scripts_for(handler):
    mods = ["core.js", HANDLERS[handler] + ".js"]
    return "".join(f'<script src="{asset("js/" + m)}" defer></script>' for m in mods)


# ---------- layouts ----------
def tool_mount(t):
    return (f'<div id="tool" data-tool="{t["tool"]}" data-config="{e(json.dumps(t.get("config", {})))}">'
            '<div class="tool-panel"><p>Loading the tool… If nothing appears, turn on JavaScript in your browser.</p></div></div>')


def guidance(t):
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in t.get("faq", []))
    rel = "".join(f'<li><a href="{tool_url(s)}">{e(BY_SLUG[s]["short"])}</a></li>' for s in t.get("related", []) if s in BY_SLUG)
    out = link_tools(t.get("body", "") + GUIDES.get(t["slug"], ""))
    if faq:
        out += f'<h2>Questions</h2><div class="faq">{faq}</div>'
    if rel:
        out += f'<h2>Related tools</h2><ul class="related">{rel}</ul>'
    return f'<div class="wrap narrow content">{out}</div>'


def layout_workbench(t):
    sec = SECTION[t["section"]]
    return f"""<main>
<div class="wrap">
<p class="crumbs"><a href="/">Home</a> / <a href="{TOOLS_BASE}">Converters</a> / <a href="{TOOLS_BASE}#{sec['id']}">{e(sec['name'])}</a></p>
<div class="tool-head"><span class="kicker" aria-hidden="true"></span><h1>{e(t['h1'])}</h1><p>{e(t['lede'])}</p></div>
{tool_mount(t)}
</div>
{guidance(t)}
</main>"""


def layout_stage(t):
    """Full-width interactive surface; guidance below. For larger interactive apps."""
    return f"""<main>
<div class="stage">
<div class="tool-head"><span class="kicker" aria-hidden="true"></span><h1>{e(t['h1'])}</h1><p>{e(t['lede'])}</p></div>
<div class="stage-surface">{tool_mount(t)}</div>
</div>
{guidance(t)}
</main>"""


LAYOUTS = {"workbench": layout_workbench, "stage": layout_stage}


def tool_page(t):
    path = tool_url(t["slug"])
    sec = SECTION[t["section"]]
    ld = [
        {"@context": "https://schema.org", "@type": "WebApplication", "name": t["h1"], "url": DOMAIN + path,
         "applicationCategory": t.get("category", "MultimediaApplication"), "operatingSystem": "Any (runs in the browser)",
         "browserRequirements": "Requires JavaScript", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
         "description": t["desc"]},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": DOMAIN + "/"},
            {"@type": "ListItem", "position": 2, "name": "Converters", "item": DOMAIN + TOOLS_BASE},
            {"@type": "ListItem", "position": 3, "name": sec["name"], "item": DOMAIN + TOOLS_BASE + "#" + sec["id"]},
            {"@type": "ListItem", "position": 4, "name": t["short"], "item": DOMAIN + path}]},
    ]
    if t.get("faq"):
        ld.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]})
    return (head(t["title"], t["desc"], path, ld, section=t["section"], layout=t["layout"]) +
            LAYOUTS[t["layout"]](t) + "\n" + footer() + scripts_for(t["tool"]) + "\n</body></html>")


def home(path="/"):
    groups = ""
    for s in LIVE_SECTIONS:
        items = "".join(f'<li><a href="{tool_url(t["slug"])}"><strong>{e(t["short"])}</strong><span>{e(t["blurb"])}</span></a></li>'
                        for t in TOOLS if t["section"] == s["id"])
        groups += (f'<section class="dir-group" id="{s["id"]}" data-section="{s["id"]}"><h2>{e(s["name"])}</h2>'
                   f'<p>{e(s["desc"])}</p><ul class="dir-list">{items}</ul></section>')
    ld = [{"@context": "https://schema.org", "@type": "WebSite", "name": BRAND, "url": DOMAIN + "/"},
          {"@context": "https://schema.org", "@type": "Organization", "name": BRAND, "url": DOMAIN + "/", "email": EMAIL}]
    title = "Free Image and PDF Tools That Never Upload Your Files | TechnoForesight"
    desc = ("Convert HEIC and WebP, compress images and PDFs to an exact size, resize exam photos and signatures, "
            "merge and split PDFs. Free, unlimited, and your files never leave your device.")
    return head(title, desc, path, ld, layout="home", canonical=TOOLS_BASE) + f"""<main>
<div class="wrap">
<section class="hero">
<h1>Convert, compress and resize files without uploading them</h1>
<p>Every tool on this site runs inside your browser. Your photos and documents stay on your device, so there are no upload waits, no daily limits and no sign-up.</p>
<ul class="hero-proof"><li>Nothing is uploaded</li><li>No limits or watermarks</li><li>Works on phone and computer</li></ul>
</section>
<div class="dir">{groups}</div>
</div>
<div class="wrap narrow content">
<h2>Why your files stay on your device</h2>
<p>Most online converters send your files to their servers, process them there and send them back. That is slow on mobile data and risky for ID proofs, certificates, bank statements and family photos.</p>
<p>Modern browsers can do this work themselves. When you use a tool here, the page loads the code it needs and processes the file on your phone or computer.</p>
<h2>Made for real upload limits</h2>
<p>Application portals reject files for being a few kilobytes too large, the wrong format or the wrong dimensions. The compressors on this site let you type the exact limit, such as 50 KB or 100 KB, and show the final size against it before you upload.</p>
</div>
</main>
{footer()}</body></html>"""


def article(slug, title, desc, h1, body, noindex=False):
    return head(title, desc, "/" + slug, noindex=noindex) + f"""<main><div class="wrap narrow content">
<h1 style="font:700 clamp(30px,4.4vw,44px)/1.1 var(--head);color:var(--ink);margin:30px 0 10px">{e(h1)}</h1>
{body}
</div></main>
{footer()}</body></html>"""


def update_redirects():
    """Old flat tool URLs (/heic-to-jpg) permanently redirect to /converters/heic-to-jpg."""
    path = os.path.join(ROOT, "firebase.json")
    cfg = json.load(open(path))
    keep = [r for r in cfg["hosting"].get("redirects", []) if not r.get("destination", "").startswith(TOOLS_BASE + "/")]
    gen = [{"source": "/" + t["slug"], "destination": tool_url(t["slug"]), "type": 301} for t in TOOLS]
    cfg["hosting"]["redirects"] = keep + gen
    with open(path, "w") as f:
        json.dump(cfg, f, indent=2)
        f.write("\n")


def write(name, text):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(text)


def main():
    os.makedirs(OUT, exist_ok=True)
    for f in os.listdir(OUT):
        if f.endswith(".html") or f in ("sitemap.xml", "robots.txt", "ads.txt"):
            os.remove(os.path.join(OUT, f))
    build_assets()
    tdir = os.path.join(OUT, TOOLS_BASE.strip("/"))
    if os.path.isdir(tdir):
        shutil.rmtree(tdir)
    os.makedirs(tdir)
    write("index.html", home("/"))                       # root shows the converters hub for now
    write(TOOLS_BASE.strip("/") + ".html", home(TOOLS_BASE))
    for t in TOOLS:
        write(tool_url(t["slug"]).strip("/") + ".html", tool_page(t))
    write("about.html", article("about", f"About {BRAND}", f"About {BRAND}: free browser-based file tools that never upload your files.", f"About {BRAND}", STATIC.ABOUT))
    write("privacy.html", article("privacy", f"Privacy Policy | {BRAND}", f"How {BRAND} handles your data. Files are processed in your browser and never uploaded.", "Privacy policy", STATIC.PRIVACY))
    write("terms.html", article("terms", f"Terms of Use | {BRAND}", f"Terms of use for {BRAND} tools.", "Terms of use", STATIC.TERMS))
    write("contact.html", article("contact", f"Contact | {BRAND}", f"Contact {BRAND}.", "Contact us", STATIC.CONTACT))
    write("404.html", article("404", f"Page not found | {BRAND}", "Page not found.", "Page not found", STATIC.NOTFOUND, noindex=True))
    urls = [TOOLS_BASE] + [tool_url(t["slug"]) for t in TOOLS] + ["/about", "/privacy", "/terms", "/contact"]
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
          "".join(f"<url><loc>{DOMAIN}{u}</loc><lastmod>{TODAY}</lastmod></url>\n" for u in urls) + "</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")
    if ADSENSE_CLIENT:
        write("ads.txt", f"google.com, {ADSENSE_CLIENT.replace('ca-', '')}, DIRECT, f08c47fec0942fa0\n")
    update_redirects()
    print(f"Built {len(TOOLS)} tool pages in {len(LIVE_SECTIONS)} sections, plus home and 5 static pages.")


if __name__ == "__main__":
    main()
