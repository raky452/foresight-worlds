"""Static pages (about, privacy, terms, contact)."""
import datetime
from .common import BRAND, EMAIL
TODAY = datetime.date.today().isoformat()

ABOUT = f"""<p>{BRAND} is a growing set of free tools for everyday file problems: photos that will not open, documents that are too large for an upload limit, and forms that want an exact photo size.</p>
<h2>How the tools work</h2>
<p>Every tool runs inside your web browser. When you choose a file, it is processed on your own device and the result is saved straight back to it. We do not receive, store or see your files.</p>
<h2>Who we build for</h2>
<p>Students and job applicants filling in online forms, people moving photos between iPhone and Windows, small offices handling PDFs every day, and anyone who would rather not upload private documents to a stranger's server.</p>
<h2>Contact</h2>
<p>Suggestions for new tools and bug reports are welcome at <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>"""

PRIVACY = f"""<p><em>Last updated: {TODAY}</em></p>
<h2>Your files</h2>
<p>The tools on {BRAND} process files entirely in your browser. Files you choose are not uploaded to our servers, and we have no access to them. When you close or reload the page, the files and results are removed from the page's memory.</p>
<h2>Information collected when you visit</h2>
<p>Like most websites, our hosting provider (Google Firebase Hosting) automatically records basic technical information for security and reliability, such as IP address, browser type and the pages requested. We do not use this to identify you.</p>
<h2>Third-party code</h2>
<p>Some tools load open-source software libraries from public content delivery networks (cdnjs.cloudflare.com and cdn.jsdelivr.net), and fonts from Google Fonts. These providers receive standard request information, such as your IP address, when the code is downloaded. They do not receive your files.</p>
<h2>Analytics</h2>
<p>We use Google Analytics to understand how visitors use the site, for example which pages are visited, which tools are used and whether they work, so we can improve it. Google Analytics uses cookies and receives standard information such as your approximate location, device, browser and the pages you view. It never receives the files you convert or their contents. You can opt out with the <a href="https://tools.google.com/dlpage/gaoptout" rel="nofollow">Google Analytics opt-out browser add-on</a>.</p>
<h2>Advertising and cookies</h2>
<p>We may show advertising provided by Google. Google and its partners may use cookies to serve ads based on your previous visits to this and other websites. You can opt out of personalised advertising at <a href="https://www.google.com/settings/ads" rel="nofollow">Google Ads Settings</a> or <a href="https://www.aboutads.info/choices/" rel="nofollow">aboutads.info</a>. Where required by law, we will ask for your consent before personalised ads or non-essential cookies are used.</p>
<h2>Children</h2>
<p>The site is intended for a general audience and does not knowingly collect personal information from children.</p>
<h2>Changes and contact</h2>
<p>We will update this page if our practices change. Questions about privacy: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>"""

TERMS = f"""<p><em>Last updated: {TODAY}</em></p>
<h2>Using the tools</h2>
<p>The tools on {BRAND} are free to use for personal and commercial purposes. Use them only with files you have the right to use and modify.</p>
<h2>No guarantee</h2>
<p>The tools are provided as they are, without warranties of any kind. Always keep your original files and check results before relying on them, especially for official applications. Size presets are common examples, not official requirements: check the rules of the organisation you are applying to.</p>
<h2>Limitation of liability</h2>
<p>To the extent permitted by law, {BRAND} is not liable for any loss arising from the use of the site or its tools, including rejected applications or lost data.</p>
<h2>Changes</h2>
<p>We may change the tools or these terms at any time. Continued use of the site means you accept the current terms. Questions: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>"""

CONTACT = f"""<p>Found a bug, need a new tool, or want to work with us? Email <a href="mailto:{EMAIL}">{EMAIL}</a>. We read every message and usually reply within two working days.</p>
<p>When reporting a problem, tell us which tool you used, your browser and device, and what happened. Please do not send us your private files: our tools run on your device, so we can usually reproduce problems with a similar sample file.</p>"""

NOTFOUND = """<p>That page does not exist or has moved. Go to the <a href="/">home page</a> to see all tools.</p>"""
