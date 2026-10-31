"""Exam and form upload tools.
Each entry is one public page. Fields:
  slug      URL path (/slug). Keep flat, lowercase, hyphenated, matching the search phrase.
  section   id from sections.py
  tool      handler name registered by a JS module (see handlers.py)
  config    JSON passed to the handler
  layout    optional: "workbench" (default) or "stage"
  status    optional: "live" (default) or "draft" (drafts are not built)
  short, blurb, title, desc, h1, lede, body, faq, related: page content
"""
from ..common import PRIVACY_LINE

TOOLS = [
dict(slug="compress-image-to-20kb", section="forms", tool="compress", config={"target": 20, "presets": [10, 15, 20, 30]},
 short="Compress image to 20 KB", blurb="For signatures and small uploads",
 title="Compress Image to 20 KB Online – Signature and Photo | TechnoForesight",
 desc="Reduce a signature or photo to 20 KB or less for online application forms. Free, works on phone, no upload.",
 h1="Compress an image to 20 KB",
 lede="Online forms often allow only 10 to 20 KB for a signature or thumb impression. Get your image under the limit while keeping the writing clear.",
 body="""
<h2>Get a clear signature under 20 KB</h2>
<ol><li>Sign in dark blue or black ink on plain white paper.</li>
<li>Photograph it in daylight, straight from above, with the signature filling most of the frame.</li>
<li>Choose the photo above, keep the target at 20 KB and select <strong>Compress images</strong>.</li></ol>
<p>A signature has lots of white space and very little detail, so it compresses well. A 4 MB phone photo will typically come down to 10 to 20 KB while staying readable.</p>
<h2>If the form also asks for pixel dimensions</h2>
<p>Some forms say, for example, “140 × 60 pixels, 10 to 20 KB”. In that case use the <a href="/exam-photo-signature-resizer">photo and signature resizer</a>, which crops or fits the image to the exact dimensions and the size range in one step.</p>
<h2>Common reasons uploads are rejected</h2>
<ul><li>The file is a PNG or HEIC when the form wants JPG. This tool always saves JPG by default.</li>
<li>The image is smaller than the minimum size, such as 10 KB. Use a slightly larger target, such as 18 KB.</li>
<li>The signature is faint. Use darker ink and better light rather than editing the photo.</li></ul>
""",
 faq=[("Will the signature still be readable?", "Yes, as long as the original photo is sharp and well lit. The compressor keeps quality as high as the limit allows."),
      ("Is my signature uploaded anywhere?", PRIVACY_LINE),
      ("Can I make a photo 20 KB too?", "Yes, but faces lose detail at 20 KB. Check whether the form allows a larger photo size, such as 50 KB.")],
 related=["exam-photo-signature-resizer", "compress-image-to-50kb", "compress-image"]),

dict(slug="compress-image-to-50kb", section="forms", tool="compress", config={"target": 50, "presets": [30, 40, 50, 60]},
 short="Compress image to 50 KB", blurb="For passport-style photos",
 title="Compress Photo to 50 KB Online – Free, No Upload | TechnoForesight",
 desc="Reduce a photo to 50 KB or less for exam, job and government forms. Free, private, works on mobile.",
 h1="Compress a photo to 50 KB",
 lede="50 KB is one of the most common photo limits on job, exam and government portals. Get your photo under it with your face still sharp.",
 body="""
<h2>How to get a photo under 50 KB</h2>
<ol><li>Choose your photo. Phone photos, scans and HEIC files from iPhones all work.</li>
<li>Keep the target at 50 KB, or type a different limit.</li>
<li>Select <strong>Compress images</strong> and download the JPG.</li></ol>
<h2>Tips for a photo that gets accepted</h2>
<ul><li>Use a plain, light background and even lighting on your face.</li>
<li>Crop to head and shoulders before compressing, so the limited file size is spent on your face.</li>
<li>If the form specifies dimensions, such as 200 × 230 pixels or 3.5 × 4.5 cm, use the <a href="/exam-photo-signature-resizer">photo and signature resizer</a> instead.</li></ul>
<h2>Check the minimum size too</h2>
<p>Many forms reject files that are too small as well as too large, for example “between 20 KB and 50 KB”. The result shows the exact file size, so you can confirm it falls inside the range before uploading.</p>
""",
 faq=[("Is the photo uploaded?", PRIVACY_LINE),
      ("The form says 50 KB, should I aim for exactly 50?", "Aim slightly lower, such as 45 KB. Some portals count a kilobyte as 1,000 bytes rather than 1,024, so a file at exactly 50 KB can be rejected."),
      ("Can I do this on my phone?", "Yes. Open this page in your phone browser and choose the photo from your gallery.")],
 related=["exam-photo-signature-resizer", "compress-image-to-20kb", "passport-photo-sheet"]),

dict(slug="exam-photo-signature-resizer", section="forms", tool="formphoto", config={},
 short="Photo and signature resizer", blurb="Exact pixels and KB range",
 title="Photo and Signature Resizer for Online Forms (Pixels + KB) | TechnoForesight",
 desc="Resize photos and signatures to the exact pixel size and KB range required by exam, job and government application forms. Free and private.",
 h1="Resize photo and signature for online forms",
 lede="Set the exact width, height and minimum and maximum file size the form asks for, and get an upload-ready JPG in one step.",
 body="""
<h2>How to prepare your upload</h2>
<ol><li>Open the official notification or the form's upload page and note the required width and height (in pixels or cm), the minimum and maximum file size, and the format.</li>
<li>Choose your photo or signature above.</li>
<li>Pick the closest preset or enter the numbers exactly. For centimetres at 300 DPI: 3.5 cm is 413 pixels and 4.5 cm is 531 pixels.</li>
<li>Use <strong>Crop to fill</strong> for photos and <strong>Fit inside</strong> for signatures, then select <strong>Prepare for upload</strong>.</li></ol>
<div class="note"><p>Size rules differ between exams and change from year to year. The presets are common sizes, not official rules. Always check the latest notification for the exam you are applying to.</p></div>
<h2>Photo checklist</h2>
<ul><li>Recent photo, face clearly visible, eyes open, no sunglasses or cap.</li>
<li>Plain white or light background, even light without shadows.</li>
<li>Face should fill roughly half to two thirds of the photo height.</li></ul>
<h2>Signature checklist</h2>
<ul><li>Sign with black or dark blue ink on plain white paper.</li>
<li>Photograph or scan it straight on and crop close to the signature before resizing.</li>
<li>Do not sign in capital letters if the instructions forbid it.</li></ul>
<h2>Need printed copies too?</h2>
<p>Use the <a href="/passport-photo-sheet">passport photo sheet maker</a> to print many copies on one A4 sheet or 4 × 6 photo paper.</p>
""",
 faq=[("Is my photo uploaded to your server?", PRIVACY_LINE),
      ("The portal still rejects my file. What should I check?", "Check three things: the file is JPG (or the format the form asks for), the size is inside the minimum and maximum range, and the width and height match exactly. The result line shows all three."),
      ("Why is my file smaller than the minimum size?", "Small, simple images such as signatures sometimes compress below the minimum even at full quality. Use a sharper original or slightly larger dimensions if the rules allow it."),
      ("Can I use it on my phone?", "Yes. It works in the browser on Android and iPhone, including HEIC photos from the iPhone camera.")],
 related=["compress-image-to-50kb", "compress-image-to-20kb", "passport-photo-sheet", "resize-image"]),

dict(slug="passport-photo-sheet", section="forms", tool="passport", config={},
 short="Passport photo sheet", blurb="Print many copies on A4 or 4×6",
 title="Passport Size Photo Sheet Maker – A4 and 4×6 | TechnoForesight",
 desc="Make a printable sheet of passport size photos (3.5 × 4.5 cm or 2 × 2 inch) on A4 or 4 × 6 paper. Free, private, download as PDF or JPG.",
 h1="Make a passport photo sheet",
 lede="Fill an A4 page or 4 × 6 photo paper with passport-size copies of your photo, ready to print and cut.",
 body="""
<h2>How to make the sheet</h2>
<ol><li>Choose a front-facing photo with a plain background.</li>
<li>Choose the photo size and paper. 3.5 × 4.5 cm is used in India, the UK, the EU and many other countries. The USA uses 2 × 2 inches.</li>
<li>Select <strong>Make photo sheet</strong> and download the PDF.</li></ol>
<h2>Print at actual size</h2>
<p>In the print dialog, set scale to <strong>100%</strong> or <strong>Actual size</strong>. If “Fit to page” is switched on, the photos print slightly smaller than the required size. Use the cutting lines as a guide.</p>
<h2>How many photos fit?</h2>
<p>With small margins, an A4 sheet holds 30 photos at 3.5 × 4.5 cm, and a 4 × 6 inch print holds 6. Enter a smaller number of copies if you need fewer.</p>
<h2>Is the photo itself acceptable?</h2>
<p>This tool sizes and arranges your photo. It does not check official rules such as head size or background colour. Check the rules for the passport, visa or ID you are applying for.</p>
""",
 faq=[("Is my photo uploaded?", PRIVACY_LINE),
      ("Why are the printed photos the wrong size?", "Your printer was probably set to “Fit to page”. Print the PDF at 100% or actual size."),
      ("Can I print it at a photo shop?", "Yes. Take the JPG for 4 × 6 photo paper or the PDF for A4 printing.")],
 related=["exam-photo-signature-resizer", "resize-image", "compress-image-to-50kb"]),

dict(slug="compress-pdf-to-100kb", section="forms", tool="compresspdf", config={"target": 100, "presets": [50, 100, 150, 200]},
 short="Compress PDF to 100 KB", blurb="For certificates and ID proofs",
 title="Compress PDF to 100 KB Online – Free, No Upload | TechnoForesight",
 desc="Reduce certificates, mark sheets and ID proofs to 100 KB for online forms. Free and private: the PDF never leaves your device.",
 h1="Compress a PDF to 100 KB",
 lede="Application portals often limit documents to 100 KB. Bring your certificate, mark sheet or ID proof under the limit while keeping it readable.",
 body="""
<h2>How to get under 100 KB</h2>
<ol><li>Choose the PDF of your document.</li>
<li>Keep the target at 100 KB.</li>
<li>Tick <strong>Black and white</strong> if the document has no colour stamps or photos you must keep, then select <strong>Compress PDF</strong>.</li></ol>
<h2>Start from a good scan</h2>
<p>The smaller the limit, the more the starting scan matters. Place the document flat on a dark table, take the photo in daylight straight from above, and crop off the background before creating the PDF with <a href="/jpg-to-pdf">JPG to PDF</a>. A clean single page compresses to under 100 KB and stays readable.</p>
<h2>Multi-page documents</h2>
<p>A 100 KB limit leaves very little room per page for long documents. Upload only the pages the form asks for, using <a href="/split-pdf">split PDF</a>, or check whether the portal allows a larger size for multi-page files.</p>
""",
 faq=[("Is the document uploaded?", PRIVACY_LINE),
      ("Will the portal accept it?", "The result is a normal PDF. Check the size shown under the result is below the limit before uploading."),
      ("Why is my text not selectable afterwards?", "To reach 100 KB, pages are saved as images. That does not matter for scanned certificates, which were images to begin with.")],
 related=["compress-pdf", "jpg-to-pdf", "compress-image-to-100kb", "exam-photo-signature-resizer"]),
]
