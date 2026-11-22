"""Downloadable software pages. Currently: TechnoForesight Assistant for Windows (/assistant)."""
from .common import BRAND, EMAIL

ASSISTANT_SLUG = "assistant"
ASSISTANT_VERSION = "0.1.0"
_RELEASES = "https://github.com/raky452/ai/releases"
SETUP_URL = _RELEASES + "/latest/download/TechnoForesightAssistant-Setup.exe"
PORTABLE_URL = _RELEASES + "/latest/download/TechnoForesightAssistant-Portable.zip"
SOURCE_URL = "https://github.com/raky452/ai/tree/main/technoforesight/windows-assistant"
OLLAMA_URL = "https://ollama.com/download/windows"
# YouTube video id of the demo/installation video. Empty = no embed.
ASSISTANT_VIDEO_ID = ""

ASSISTANT_TITLE = f"Free Offline AI Assistant for Windows (Alt+Space) | {BRAND}"
ASSISTANT_DESC = ("Download TechnoForesight Assistant: a free AI command bar for Windows 10 and 11 that runs on your own PC. "
                  "Open apps, find files, summarise PDFs and ask questions with nothing uploaded.")
ASSISTANT_H1 = "TechnoForesight Assistant for Windows"


def _video():
    if not ASSISTANT_VIDEO_ID:
        return ""
    return (f'<h2>Watch it in action</h2><div style="position:relative;padding-top:56.25%;border-radius:14px;overflow:hidden">'
            f'<iframe src="https://www.youtube-nocookie.com/embed/{ASSISTANT_VIDEO_ID}" title="TechnoForesight Assistant demo" '
            'style="position:absolute;inset:0;width:100%;height:100%;border:0" loading="lazy" '
            'allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>')


def assistant_body():
    return f"""<p style="font-size:19px;color:var(--muted);margin-top:0">A free AI command bar for your Windows laptop. Press <strong>Alt+Space</strong> anywhere, type what you want, and it happens. The AI runs <strong>on your own PC</strong>, so your questions and documents never leave it.</p>
<p style="display:flex;gap:12px;flex-wrap:wrap;margin:26px 0 8px">
<a class="btn primary" href="{SETUP_URL}" style="text-decoration:none" data-download="assistant-setup">Download for Windows (free)</a>
<a class="btn ghost" href="{PORTABLE_URL}" style="text-decoration:none">Portable zip</a>
</p>
<p style="color:var(--muted);font-size:14px;margin:0">Version {ASSISTANT_VERSION} · Windows 10 and 11 (64-bit) · No admin rights needed · <a href="{SOURCE_URL}" rel="nofollow">Source code</a></p>
<ul class="hero-proof"><li>Runs offline on your PC</li><li>No account or subscription</li><li>Nothing uploaded</li></ul>
{_video()}
<h2>What you can type</h2>
<ul>
<li><strong>open chrome</strong>, <strong>word</strong>, <strong>calculator</strong>, <strong>whatsapp</strong>: opens any app in your Start menu, including Microsoft Store apps.</li>
<li><strong>find files invoice</strong>: searches your Desktop, Documents, Downloads and OneDrive folders. Press the down arrow and Enter to open a result.</li>
<li><strong>summarise C:\\Users\\you\\Downloads\\report.pdf</strong>: reads a PDF, Word (.docx) or text file and gives you five key points plus any dates, amounts and action items.</li>
<li><strong>settings wifi</strong>, <strong>settings bluetooth</strong>, <strong>settings display</strong>: jumps straight to that page of Windows Settings.</li>
<li><strong>lock pc</strong>: locks your computer instantly.</li>
<li><strong>technoforesight.in</strong> or <strong>google ipl score</strong>: opens a website or searches the web.</li>
<li>Anything else, such as <em>"write a leave letter for tomorrow"</em> or <em>"explain GST in simple words"</em>, is answered by the AI model on your laptop.</li>
</ul>
<h2>How to install (5 minutes)</h2>
<ol>
<li><strong>Download</strong> the installer with the button above.</li>
<li><strong>Run</strong> <code>TechnoForesightAssistant-Setup.exe</code>. Windows may show <em>"Windows protected your PC"</em> because the app is new and not yet code-signed. Click <strong>More info</strong>, then <strong>Run anyway</strong>. Tick <em>Start automatically when I sign in</em> so Alt+Space always works.</li>
<li><strong>Install the AI engine.</strong> On first launch the assistant shows an <em>Install Ollama</em> button. Ollama is the free, open-source engine that runs AI models on your PC. Download it from <a href="{OLLAMA_URL}" rel="nofollow">ollama.com</a> and install it, then click <em>I've installed it, check again</em>.</li>
<li><strong>Download the AI model.</strong> Click <em>Download AI model</em>. This is a one-time download of about 2.5 GB (the Qwen3 4B model), so use Wi-Fi.</li>
<li><strong>Press Alt+Space</strong> and start typing.</li>
</ol>
<h2>Why offline AI?</h2>
<p>Most AI assistants send everything you type to a company's servers. That is a problem when you are summarising a bank statement, an offer letter or a medical report. TechnoForesight Assistant uses an open-source model that runs on your own processor, the same way the converters on this site process files inside your browser. It also keeps working without internet once the model is downloaded, and there are no daily limits or subscriptions.</p>
<h2>Will it run on my laptop?</h2>
<p>The default model needs about 8 GB of RAM and works on most laptops from the last eight years, including older Intel Core i5 machines without a graphics card. Answers appear word by word; expect a few seconds for a short answer on an older laptop. If you have 16 GB of RAM or more, you can switch to the larger <code>qwen3:8b</code> model for better answers by adding <code>model = "qwen3:8b"</code> to <code>%APPDATA%\\TechnoForesight\\config.toml</code>.</p>
<h2>Questions</h2>
<div class="faq">
<details><summary>Is it really free?</summary><p>Yes. The assistant, the Ollama engine and the Qwen3 model are all free. Qwen3 is released under the Apache 2.0 open-source licence.</p></details>
<details><summary>Can I change the Alt+Space shortcut?</summary><p>Yes. Create <code>%APPDATA%\\TechnoForesight\\config.toml</code> and add a line such as <code>hotkey = "ctrl+space"</code>, then restart the assistant.</p></details>
<details><summary>Why does Windows warn me when I run the installer?</summary><p>Windows SmartScreen warns about any new app that is not yet code-signed. The full source code is public on GitHub, and the installer only writes to your own user folder.</p></details>
<details><summary>How do I uninstall it?</summary><p>Open Settings, then Apps, find TechnoForesight Assistant and click Uninstall. You can uninstall Ollama the same way.</p></details>
<details><summary>Does it work on Mac or Linux?</summary><p>A Linux version is available in the same <a href="https://github.com/raky452/ai/tree/main/technoforesight" rel="nofollow">GitHub project</a>. Mac and Android versions are in development.</p></details>
</div>
<h2>Feedback</h2>
<p>Found a bug or want a new command? Email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>"""
