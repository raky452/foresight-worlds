# TechnoForesight site: architecture

Maintainer notes. This file lives in the repository; only the generated `public/` folder is deployed to the website.

## Principles
1. **Registry first.** Pages, sections and handlers are data. The generator (`build.py`) turns data into pages, navigation, footer, sitemap and structured data. Adding a tool should never require editing templates.
2. **Small runtime, plug-in modules.** `core.js` holds shared helpers, the library loader and the workbench panel. Each tool family is a separate module that registers handlers. A page loads `core.js` plus only the module it needs.
3. **One design system.** All colours, type, spacing and widths are tokens in `src/styles/tokens.css`. Sections get an accent with one line: `[data-section=id]{--accent:...}`.
4. **Quiet until live.** A section is shown publicly only when it has at least one `live` page. Entries marked `status="draft"` are not built. New families can be prepared without appearing on the site.
5. **Client-side by default.** Processing happens in the browser (zero compute cost, privacy). Server-side work is the exception and goes behind `/api/` (see below).

## Layout of the repo
```
build.py                 generator: src/ -> public/
firebase.json            hosting config
src/styles/              tokens.css, base.css, layout.css, components.css (concatenated in that order)
src/scripts/core.js      runtime: TF.register, TF.shell, TF.loadLib, TF.addLib, file helpers
src/scripts/<module>.js  one per tool family (image, pdf, forms, ...)
src/content/common.py    domain, brand, email
src/content/sections.py  sections: id, name, nav label, description, order
src/content/handlers.py  handler name -> module file
src/content/tools/*.py   page entries, auto-discovered (one file per family)
src/content/pages.py     about, privacy, terms, contact
public/                  generated output (do not edit by hand)
```

## Add a tool page that reuses an existing handler
Add an entry to the right `src/content/tools/<family>.py` with `slug, section, tool, config` and content fields, then run `python3 build.py`.

## Add a new handler or tool family
1. Create `src/scripts/<module>.js`:
   ```js
   (function (TF) {
     TF.register({
       myhandler: function (root, cfg) {
         var sh = TF.shell(root, { accept: '...', multiple: true, kind: 'files', filter: function (f) { return true; }, action: 'Run' });
         sh.onRun(async function (files, say) { /* return [{ name, blob, before?, target?, note? } | { name, error }] */ });
       }
     });
   })(window.TF);
   ```
   Need a third-party library? `TF.addLib('key', 'https://cdnjs.cloudflare.com/...')` then `await TF.loadLib('key')`. Pin exact versions.
2. Map the handler in `src/content/handlers.py`.
3. Add pages in `src/content/tools/<family>.py`. If it is a new family, add a section in `sections.py` and an accent in `tokens.css`.

## Layouts
Set `layout` on an entry. Available:
- `workbench` (default): header, tool panel, guidance and FAQ below. For converters and single-task tools.
- `stage`: full-width surface (`--w-stage`) with a tall canvas area, guidance below. For larger interactive applications that need room.
Add a layout by writing a `layout_<name>(entry)` function in `build.py`, registering it in `LAYOUTS`, and adding its styles under a `.layout-<name>` block in `layout.css`.

## URL conventions
- TechnoForesight is an umbrella. Converter tools live under `/converters/<slug>` (`TOOLS_BASE` in `common.py`), lowercase, hyphenated, matching the search phrase (`/converters/heic-to-jpg`). Never rename a live slug.
- The site root `/` currently shows the converters hub with its canonical set to `/converters`, so search engines index the tools under `/converters` and the root can later become the umbrella home page without breaking any indexed link.
- The original flat URLs (`/heic-to-jpg`) permanently (301) redirect to `/converters/...`. `build.py` regenerates these redirects in `firebase.json` on every build; commit the updated `firebase.json`.
- `GOOGLE_SITE_VERIFICATION` and `ADSENSE_CLIENT` in `common.py` switch on the Search Console meta tag, the AdSense script and `ads.txt`.
- Future families that are not single-task tools should use a short path prefix chosen per family (for example `/<family>/<slug>`), so they do not compete with tool slugs.

## Server-side features (when needed)
Keep the static site on Firebase Hosting and put any server work (document conversion that needs LibreOffice, account features, integration endpoints, protocol servers for AI clients) in Cloud Run services that scale to zero. Route them through hosting so they share the domain:
```json
"rewrites": [{ "source": "/api/<service>/**", "run": { "serviceId": "<service>", "region": "asia-south1" } }]
```
Rules: authenticate every endpoint, never store user files longer than a request, set a budget alert before enabling billing.

## Before applying for AdSense
- Expand each tool page to roughly 600+ words of real guidance.
- Make sure the contact email in `common.py` receives mail.
- Keep ads out of the tool panel and away from download buttons.
