"""PDF tools.
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
dict(slug="merge-pdf", section="pdf", tool="merge", config={},
 short="Merge PDF", blurb="Combine files in any order",
 title="Merge PDF Files – Free, Unlimited, No Upload | TechnoForesight",
 desc="Combine multiple PDF files into one in your browser. Reorder files, no upload, no sign-up and no page limits.",
 h1="Merge PDF files",
 lede="Combine several PDFs into one document. Put them in the order you want, and your files stay on your device.",
 body="""
<h2>How to merge PDFs</h2>
<ol><li>Choose two or more PDF files, or drop them onto the box.</li>
<li>Use the arrows to put them in the right order.</li>
<li>Select <strong>Merge PDFs</strong> and download <em>merged.pdf</em>.</li></ol>
<h2>Why merging here is private</h2>
<p>Most online PDF tools upload your documents to their servers. That is a real concern for bank statements, ID proofs, contracts and medical reports. This tool merges the files inside your browser, so the documents never leave your device.</p>
<h2>What is kept</h2>
<p>Pages are copied exactly: text stays selectable, links and images are kept, and nothing is compressed. Bookmarks from the original files are not carried over.</p>
<h2>Password-protected PDFs</h2>
<p>PDFs locked with a password cannot be merged. Open them with the password and save an unlocked copy first.</p>
""",
 faq=[("Is there a limit on files or pages?", "No fixed limit. Very large documents depend on your device's memory."),
      ("Are my PDFs uploaded?", PRIVACY_LINE),
      ("Can I merge images and PDFs together?", "Convert the images with JPG to PDF first, then merge the results.")],
 related=["split-pdf", "compress-pdf", "jpg-to-pdf", "rotate-pdf"]),

dict(slug="split-pdf", section="pdf", tool="split", config={},
 short="Split PDF", blurb="Extract or separate pages",
 title="Split PDF – Extract Pages for Free, No Upload | TechnoForesight",
 desc="Split a PDF into separate files or extract selected pages into a new PDF. Free and private: your document never leaves your device.",
 h1="Split a PDF",
 lede="Take out the pages you need, split a PDF into ranges, or save every page as its own file.",
 body="""
<h2>How to split a PDF</h2>
<ol><li>Choose your PDF. The tool shows how many pages it has.</li>
<li>Choose what to do: extract pages into one PDF, make one PDF per range, or save every page separately.</li>
<li>Type the pages, such as <code>1-3, 5, 8-10</code>, and select <strong>Split PDF</strong>.</li></ol>
<h2>Writing page ranges</h2>
<ul><li><code>2</code> is a single page.</li><li><code>4-7</code> is pages 4 to 7.</li><li><code>10-</code> is page 10 to the end.</li><li>Separate items with commas: <code>1, 3-4, 9-</code>.</li></ul>
<h2>Common uses</h2>
<p>Send only the relevant pages of a long statement, separate a scanned bundle into individual documents, or take one certificate out of a combined file for an upload.</p>
""",
 faq=[("Is the PDF uploaded?", PRIVACY_LINE),
      ("Do the pages lose quality?", "No. Pages are copied exactly, with text still selectable."),
      ("Can I split a password-protected PDF?", "Not yet. Save an unlocked copy first.")],
 related=["merge-pdf", "pdf-to-jpg", "rotate-pdf", "crop-pdf"]),

dict(slug="rotate-pdf", section="pdf", tool="rotate", config={},
 short="Rotate PDF", blurb="Fix sideways pages",
 title="Rotate PDF Pages – Free and Permanent | TechnoForesight",
 desc="Rotate all or selected pages of a PDF and save the result permanently. Free, private, works in your browser.",
 h1="Rotate PDF pages",
 lede="Fix scanned pages that are sideways or upside down, and save the rotation permanently.",
 body="""
<h2>How to rotate</h2>
<ol><li>Choose one or more PDFs.</li><li>Pick the rotation. Leave pages empty to rotate every page, or enter pages such as <code>2, 5-6</code>.</li><li>Select <strong>Rotate PDF</strong> and download.</li></ol>
<h2>Permanent, not just on screen</h2>
<p>Rotating in a PDF viewer usually changes only your view. This tool saves the rotation into the file, so it looks right for everyone you send it to, and in upload previews.</p>
""",
 faq=[("Is the file uploaded?", PRIVACY_LINE),
      ("Does rotating reduce quality?", "No. Only the page orientation setting changes."),
      ("Can I rotate only some pages?", "Yes. Type the page numbers or ranges in the Pages box.")],
 related=["merge-pdf", "split-pdf", "crop-pdf", "compress-pdf"]),

dict(slug="jpg-to-pdf", section="pdf", tool="img2pdf", config={},
 short="JPG to PDF", blurb="Turn photos and scans into a PDF",
 title="JPG to PDF Converter – Combine Images, Free, No Upload | TechnoForesight",
 desc="Convert JPG, PNG, HEIC and WebP images into one PDF. Choose A4 or Letter, margins and order. Free and private.",
 h1="Convert JPG to PDF",
 lede="Turn photos of documents, certificates and receipts into one tidy PDF, in the order you choose.",
 body="""
<h2>How to convert images to PDF</h2>
<ol><li>Choose your images. JPG, PNG, HEIC, WebP and AVIF all work.</li>
<li>Arrange them with the arrows. Each image becomes one page.</li>
<li>Choose the page size, orientation and margin, then select <strong>Create PDF</strong>.</li></ol>
<h2>Settings explained</h2>
<ul><li><strong>A4</strong> is the standard page size in India, the UK and most of the world. US Letter is used in the USA and Canada.</li>
<li><strong>Automatic orientation</strong> turns each page to landscape when the image is wider than it is tall.</li>
<li><strong>Same as each image</strong> makes every page exactly the size of its image, with no white borders.</li></ul>
<h2>Making the PDF smaller</h2>
<p>Phone photos make large PDFs. If a portal has a size limit, use <a href="/compress-pdf">compress PDF</a> on the result, or compress the images first with the <a href="/compress-image">image compressor</a>.</p>
""",
 faq=[("Are my images uploaded?", PRIVACY_LINE),
      ("Why are my iPhone photos rotated correctly?", "The tool reads the orientation saved by your phone camera and applies it before creating the page."),
      ("Is there a page limit?", "No fixed limit. Hundreds of photos may be slow on older phones.")],
 related=["compress-pdf", "merge-pdf", "pdf-to-jpg", "pdf-to-png"]),

dict(slug="pdf-to-jpg", section="pdf", tool="pdf2img", config={},
 short="PDF to JPG", blurb="Save pages as images",
 title="PDF to JPG Converter – High Quality, No Upload | TechnoForesight",
 desc="Convert PDF pages to JPG or PNG images at up to 300 DPI. Choose pages, download as ZIP. Free and private.",
 h1="Convert PDF to JPG",
 lede="Save each page of a PDF as a JPG or PNG image, for slides, social posts, previews or forms that only accept images.",
 body="""
<h2>How to convert</h2>
<ol><li>Choose a PDF.</li><li>Pick the quality and format. Leave Pages empty to convert all pages.</li><li>Select <strong>Convert to images</strong> and download one page or all of them as a ZIP.</li></ol>
<h2>Which quality to choose</h2>
<ul><li><strong>Small (96 DPI)</strong> for viewing on phones and sharing in chats.</li>
<li><strong>Standard (150 DPI)</strong> for most uses, including slides and uploads.</li>
<li><strong>High (300 DPI)</strong> for printing or when you need to zoom into small text.</li></ul>
<p>Choose PNG for pages with mostly text and diagrams, where it stays crisp. Choose JPG for pages with photos, where it is much smaller.</p>
""",
 faq=[("Is the PDF uploaded?", PRIVACY_LINE),
      ("Can I convert just one page?", "Yes. Type its number in the Pages box."),
      ("Does it work with scanned PDFs?", "Yes. Each scanned page becomes an image.")],
 related=["pdf-to-png", "jpg-to-pdf", "split-pdf", "compress-image"]),

dict(slug="pdf-to-png", section="pdf", tool="pdf2img", config={"fmt": "png", "transparent": True},
 short="PDF to PNG", blurb="Sharp pages, transparent background",
 title="PDF to PNG, Transparent Background | TechnoForesight",
 desc="Convert PDF pages to sharp PNG images, with an optional transparent background. Up to 300 DPI, no upload, free.",
 h1="Convert PDF to PNG",
 lede="Save PDF pages as crisp PNG images, and remove the white page background when the PDF does not paint one, so logos, signatures and diagrams can sit on any colour.",
 body="""
<h2>How to convert a PDF to PNG</h2>
<ol><li>Choose a PDF.</li><li>Pick the resolution. Leave <strong>Transparent background</strong> ticked if you want the page without its white backdrop.</li>
<li>Type page numbers such as <code>2</code> or <code>1-3</code>, or leave Pages empty to convert every page.</li>
<li>Select <strong>Convert to images</strong> and download one page or all of them as a ZIP.</li></ol>
<h2>When PNG is the better choice</h2>
<p>PNG keeps every pixel exactly as it was drawn, so thin lines, small text, charts and logos stay sharp. JPG blurs those edges to save space. Choose PNG for slides, design work, documentation screenshots and anything you will edit again. Choose <a href="/pdf-to-jpg">PDF to JPG</a> for photo-heavy pages where a small file matters more than perfect edges.</p>
<h2>How the transparent background works</h2>
<p>Most PDFs made from a word processor, a design tool or an invoice generator do not paint a white rectangle behind the content; the white you see is only the viewer. With the option on, this tool leaves that area empty, so the PNG shows through to whatever sits behind it. If a PDF does paint a coloured or white background (common in scanned pages and slide exports), that background stays, because it is part of the page. Photos of paper and scans therefore stay opaque.</p>
<div class="note"><p>To use a signature or logo from a PDF: convert the page at 300 DPI with transparency on, then crop the PNG to the part you need.</p></div>
""",
 faq=[("Is my PDF uploaded?", PRIVACY_LINE),
      ("Why is my PNG background still white?", "The PDF itself paints a white or coloured background, which is common for scans and slide exports. Only pages that leave the background empty become transparent."),
      ("Which resolution should I choose?", "Standard (150 DPI) suits slides and most uploads. Choose High (300 DPI) for print or to crop small details, and Small (96 DPI) for quick sharing."),
      ("Are PNG files bigger than JPG?", "Yes, often several times bigger for pages with photos, but similar for plain text pages. Compress the result with the image compressor if you need a smaller file.")],
 related=["pdf-to-jpg", "compress-image", "split-pdf", "jpg-to-pdf"]),

dict(slug="crop-pdf", section="pdf", tool="croppdf", config={},
 short="Crop PDF", blurb="Trim margins from every page",
 title="Crop PDF Pages, Trim Margins Free | TechnoForesight",
 desc="Crop PDF margins in millimetres for all or selected pages. Free, no upload, runs in your browser.",
 h1="Crop PDF pages",
 lede="Trim white margins or unwanted edges from every page of a PDF, or only the pages you choose, and download a new file.",
 body="""
<h2>How to crop a PDF</h2>
<ol><li>Choose one or more PDFs.</li>
<li>Enter how many millimetres to remove from the top, bottom, left and right. The values are measured on the page as it appears on screen, even if the page is rotated.</li>
<li>Leave Pages empty to crop every page, or type pages such as <code>1, 3-5</code>.</li>
<li>Select <strong>Crop PDF</strong> and download the result.</li></ol>
<h2>What cropping does</h2>
<p>The tool shrinks the visible area of each page and keeps the text and images inside it as they were, so text stays selectable and the file does not lose quality. This is a good fit for scanned pages with wide borders, documents exported with large margins, and pages you want to print or present with less white space.</p>
<div class="note"><p>Cropping hides the outside area but does not erase it. Content you trim off may still exist inside the file, so do not rely on cropping to remove confidential information. Black it out before you export the PDF instead.</p></div>
<h2>Choosing the margins</h2>
<p>A standard A4 page is 210 by 297 mm. Many word processors leave about 25 mm of margin, so removing 20 mm from each side leaves the text almost touching the edge. Start with 10 mm, check the result, and run the tool again on the new file if you want to trim more.</p>
""",
 faq=[("Is my PDF uploaded?", PRIVACY_LINE),
      ("Does cropping reduce the file size?", "Usually not much. The hidden area can stay inside the file. To make the file smaller, use compress PDF afterwards."),
      ("Can I crop only some pages?", "Yes. Type the page numbers or ranges in the Pages box, for example 2 or 1-3, 6."),
      ("Why does my PDF look the same in some programs?", "A few older programs ignore the page size and show the full original page. The file opens cropped in common browsers and PDF viewers.")],
 related=["rotate-pdf", "split-pdf", "compress-pdf", "pdf-to-png"]),

dict(slug="compress-pdf", section="pdf", tool="compresspdf", config={"target": 500, "presets": [100, 200, 500, 1000, 2000]},
 short="Compress PDF to size", blurb="Fit any upload limit",
 title="Compress PDF to Size (100 KB, 200 KB, 1 MB) – No Upload | TechnoForesight",
 desc="Reduce a PDF to a target size such as 100 KB, 200 KB, 500 KB or 1 MB. Free, works in your browser, your document is never uploaded.",
 h1="Compress a PDF to a target size",
 lede="Type the size limit you need to meet and get the most readable PDF that fits under it.",
 body="""
<h2>How to compress a PDF</h2>
<ol><li>Choose your PDF.</li><li>Type the maximum size in KB, or tap a common limit.</li><li>Tick <strong>Black and white</strong> for scanned documents, then select <strong>Compress PDF</strong>.</li></ol>
<h2>How it reaches your size</h2>
<p>The tool redraws each page as an image and tries progressively smaller settings until the whole document fits your limit, keeping the highest quality that fits. This works especially well for scanned documents and phone photos turned into PDFs, which are where most oversized PDFs come from.</p>
<div class="note"><p>Because pages become images, text in the compressed file cannot be selected or searched. Keep your original file as well.</p></div>
<h2>Tips for small limits like 100 KB</h2>
<ul><li>Remove pages the form does not need with <a href="/split-pdf">split PDF</a>.</li>
<li>Turn on black and white: it often halves the size of scanned pages.</li>
<li>Each page needs its share of the limit. Under 100 KB works well for 1 to 3 pages; longer documents need larger limits to stay readable.</li></ul>
""",
 faq=[("Is my PDF uploaded?", PRIVACY_LINE),
      ("Why can't I select text after compressing?", "Pages are saved as images to reach small sizes reliably. For documents that must stay searchable, use a larger target or keep the original."),
      ("The result is still larger than my target. What now?", "The tool stops before pages become unreadable. Remove unneeded pages, turn on black and white, or ask whether the portal accepts a larger file.")],
 related=["compress-pdf-to-100kb", "split-pdf", "jpg-to-pdf", "compress-image"]),

dict(slug="heic-to-pdf", section="pdf", tool="img2pdf", config={},
 short="HEIC to PDF", blurb="iPhone photos into one PDF",
 title="HEIC to PDF Converter – iPhone Photos to PDF, Free, No Upload | TechnoForesight",
 desc="Convert iPhone HEIC photos into a single PDF. Choose page size, order and margins. Free, private and unlimited.",
 h1="Convert HEIC to PDF",
 lede="Turn iPhone photos of documents, receipts and certificates into one PDF you can email or upload, without converting each photo first.",
 body="""
<h2>How to convert HEIC photos to PDF</h2>
<ol><li>Choose your HEIC photos. You can mix in JPG, PNG and WebP files too.</li>
<li>Put them in order with the arrows. Each photo becomes one page.</li>
<li>Choose A4 or US Letter, the orientation and the margin, then select <strong>Create PDF</strong>.</li></ol>
<h2>Why go straight from HEIC to PDF</h2>
<p>iPhones save photos as HEIC, which many websites, printers and Windows computers cannot open. Most people convert each photo to JPG and then build a PDF in a second tool. This page does both in one step, inside your browser, and keeps the orientation your iPhone recorded so pages are the right way up.</p>
<h2>Keep the PDF small</h2>
<p>Phone photos make large PDFs. If a form has a size limit, run the result through <a href="/compress-pdf">compress PDF</a>, or crop the photos to the document edges before converting.</p>
""",
 faq=[("Are my photos uploaded?", PRIVACY_LINE),
      ("Can I scan several pages into one PDF?", "Yes. Add all the photos, arrange them, and they become one multi-page PDF."),
      ("Does it work on iPhone?", "Yes. Open the page in Safari, choose photos from your library and download the PDF to Files.")],
 related=["heic-to-jpg", "jpg-to-pdf", "compress-pdf", "merge-pdf"]),

]
