"""Image tools.
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
dict(slug="heic-to-jpg", section="image", tool="convert", config={"to": "jpeg"},
 short="HEIC to JPG", blurb="Open iPhone photos anywhere",
 title="HEIC to JPG Converter – Free, No Upload, Batch | TechnoForesight",
 desc="Convert iPhone HEIC photos to JPG in your browser. Free, unlimited batch conversion, no upload and no sign-up. Works on Windows, Mac, Android and iPhone.",
 h1="Convert HEIC to JPG",
 lede="Turn iPhone photos into JPG files that open on every computer, website and printer. Convert one photo or a whole batch at once.",
 body="""
<h2>How to convert HEIC to JPG</h2>
<ol><li>Choose your HEIC photos, or drag them onto the box above. You can add many at once.</li>
<li>Set the quality. 90% keeps photos looking the same as the originals at a smaller size.</li>
<li>Select <strong>Convert to JPG</strong>, then download each photo or all of them as one ZIP file.</li></ol>
<h2>Why your photos are HEIC</h2>
<p>iPhones save photos as HEIC (High Efficiency Image Container) by default since iOS 11. HEIC files are about half the size of JPGs at similar quality, which saves space on the phone. The trouble starts when the photo leaves the phone: older versions of Windows, many government and job portals, online print shops and some email clients cannot open HEIC at all.</p>
<p>JPG is the safe choice when you need a photo to just work. Every device, browser and upload form accepts it.</p>
<h2>Converting on Windows without installing anything</h2>
<p>Windows can show HEIC only after you install an extension from the Microsoft Store, and some versions charge for it. This page needs nothing installed: open it in Edge, Chrome or Firefox, add your photos and download JPGs.</p>
<h2>Stop your iPhone saving HEIC</h2>
<p>If you always need JPG, open <strong>Settings → Camera → Formats</strong> on the iPhone and choose <strong>Most Compatible</strong>. New photos will be saved as JPG. Photos you have already taken stay HEIC, which is what this converter is for.</p>
""",
 faq=[("Is it safe to convert private photos here?", PRIVACY_LINE),
      ("Will I lose quality converting HEIC to JPG?", "JPG is slightly less efficient than HEIC, so the file can be larger, but at 90% quality the difference is not visible. Choose 100% if you plan to edit or print the photo."),
      ("Are location and camera details kept?", "No. The converted JPG does not include the original EXIF data, such as GPS location. That makes it safer to share publicly."),
      ("Can I convert Live Photos?", "Yes. You get the still image from the Live Photo. The short video part is not included."),
      ("How many photos can I convert at once?", "There is no fixed limit. Very large batches depend on your device's memory, so convert a few hundred at a time on phones.")],
 related=["heic-to-png", "compress-image", "jpg-to-pdf", "resize-image"]),

dict(slug="heic-to-png", section="image", tool="convert", config={"to": "png"},
 short="HEIC to PNG", blurb="Lossless copies of iPhone photos",
 title="HEIC to PNG Converter – Free and Private | TechnoForesight",
 desc="Convert HEIC photos to lossless PNG files in your browser. No upload, no sign-up, batch conversion supported.",
 h1="Convert HEIC to PNG",
 lede="Make lossless PNG copies of iPhone photos for editing, design work or apps that do not accept HEIC.",
 body="""
<h2>How to convert HEIC to PNG</h2>
<ol><li>Choose or drop your HEIC photos.</li><li>Select <strong>Convert to PNG</strong>.</li><li>Download each file, or all of them as a ZIP.</li></ol>
<h2>PNG or JPG?</h2>
<p>PNG keeps every pixel exactly, so it is the better choice when you will edit the photo further, cut out a background, or add text and graphics on top. The trade-off is size: a 12-megapixel photo is often 15 to 25 MB as PNG, compared with 3 to 5 MB as JPG.</p>
<p>If you only want to share, upload or print the photo, use <a href="/heic-to-jpg">HEIC to JPG</a> instead. If a form needs a small file, run the PNG through the <a href="/compress-image">image compressor</a> afterwards.</p>
<h2>Good uses for PNG copies</h2>
<ul><li>Editing in Photoshop, GIMP, Canva or Figma without generation loss</li><li>Screenshots and photos of documents where sharp text matters</li><li>Archiving an exact copy in a widely supported format</li></ul>
""",
 faq=[("Is my photo uploaded?", PRIVACY_LINE),
      ("Why is the PNG so much bigger than the HEIC?", "HEIC and JPG use lossy compression, which throws away detail your eyes rarely notice. PNG is lossless, so it stores everything and the file is larger."),
      ("Does PNG keep transparency?", "Yes, PNG supports transparency, but normal camera photos have no transparent areas, so the result looks the same as the original.")],
 related=["heic-to-jpg", "png-to-jpg", "compress-image"]),

dict(slug="webp-to-png", section="image", tool="convert", config={"to": "png"},
 short="WebP to PNG", blurb="Save web images in a common format",
 title="WebP to PNG Converter – Free, Batch, No Upload | TechnoForesight",
 desc="Convert WebP images to PNG in seconds. Keeps transparency, works in your browser, no upload and no limits.",
 h1="Convert WebP to PNG",
 lede="Images saved from websites are often WebP. Convert them to PNG so they open in any editor, document or app, with transparency kept.",
 body="""
<h2>How to convert WebP to PNG</h2>
<ol><li>Choose or drop one or more WebP images.</li><li>Select <strong>Convert to PNG</strong>.</li><li>Download the PNG files individually or as a ZIP.</li></ol>
<h2>Why you end up with WebP files</h2>
<p>Most large websites serve images as WebP because it loads faster than JPG or PNG. When you right-click and save an image, you get the WebP file. Older photo viewers, Microsoft Office versions, some print services and many upload forms still reject it.</p>
<h2>PNG keeps transparency</h2>
<p>Logos, icons and stickers in WebP format often have a transparent background. Converting to PNG keeps that transparency, so the image still sits cleanly on top of slides, documents and designs. If you do not need transparency and want a smaller file, use <a href="/webp-to-jpg">WebP to JPG</a>.</p>
<h2>Respect image rights</h2>
<p>Converting a file does not change who owns it. Only reuse images you have permission to use.</p>
""",
 faq=[("Is it free and unlimited?", "Yes. Because conversion happens on your device, there are no daily caps, sign-ups or watermarks."),
      ("Is the image uploaded anywhere?", PRIVACY_LINE),
      ("Can I convert animated WebP?", "The converter saves the first frame as a still PNG. Animated WebP to GIF is not supported yet.")],
 related=["webp-to-jpg", "png-to-jpg", "compress-image"]),

dict(slug="webp-to-jpg", section="image", tool="convert", config={"to": "jpeg"},
 short="WebP to JPG", blurb="Make web images open everywhere",
 title="WebP to JPG Converter – Free, Private, Batch | TechnoForesight",
 desc="Convert WebP images to JPG in your browser. Free, unlimited, no upload. Adjustable quality and ZIP download for batches.",
 h1="Convert WebP to JPG",
 lede="Change WebP images into JPG files that every app, printer and upload form accepts.",
 body="""
<h2>How to convert WebP to JPG</h2>
<ol><li>Choose or drop your WebP images.</li><li>Pick a quality. 90% is a good balance of size and sharpness.</li><li>Select <strong>Convert to JPG</strong> and download the results.</li></ol>
<h2>When JPG is the right choice</h2>
<p>JPG is the most compatible image format there is. Choose it for photos you want to email, print, attach to documents or upload to forms. JPG does not support transparency, so transparent areas are filled with white. If you need the transparent background, convert to <a href="/webp-to-png">PNG</a> instead.</p>
<h2>Need a smaller file?</h2>
<p>After converting, use the <a href="/compress-image">image compressor</a> to bring the JPG under a size limit such as 100 KB or 50 KB.</p>
""",
 faq=[("Why do transparent areas turn white?", "The JPG format cannot store transparency, so we fill those areas with white. Use WebP to PNG to keep transparency."),
      ("Is anything uploaded?", PRIVACY_LINE),
      ("Does it work on a phone?", "Yes, it works in Chrome, Safari, Edge and Firefox on Android and iPhone.")],
 related=["webp-to-png", "compress-image", "jpg-to-pdf"]),

dict(slug="avif-to-jpg", section="image", tool="convert", config={"to": "jpeg"},
 short="AVIF to JPG", blurb="Convert the newest web format",
 title="AVIF to JPG Converter – Free, No Upload | TechnoForesight",
 desc="Convert AVIF images to JPG in your browser. Free, private and unlimited. Batch convert and download as ZIP.",
 h1="Convert AVIF to JPG",
 lede="AVIF is the newest image format on the web. Convert AVIF files to JPG so you can open, edit, print and upload them anywhere.",
 body="""
<h2>How to convert AVIF to JPG</h2>
<ol><li>Choose or drop your AVIF images.</li><li>Set the quality and select <strong>Convert to JPG</strong>.</li><li>Download each JPG or the whole batch as a ZIP.</li></ol>
<h2>What is AVIF?</h2>
<p>AVIF is based on the AV1 video codec. It makes images even smaller than WebP, so more websites and phones now use it. Support outside the browser is still patchy: many photo viewers, office suites and online forms do not accept AVIF yet.</p>
<h2>Browser support</h2>
<p>This converter uses your browser's own image decoder. Current versions of Chrome, Edge, Firefox and Safari (version 16 and later) can all read AVIF. If a file will not open, update your browser and try again.</p>
""",
 faq=[("Is it private?", PRIVACY_LINE),
      ("Can I convert AVIF to PNG?", "Use the WebP to PNG converter: it accepts AVIF files as well and saves PNG."),
      ("Why did my AVIF fail to convert?", "Your browser may be too old to read AVIF. Update to the latest Chrome, Edge, Firefox or Safari.")],
 related=["webp-to-jpg", "heic-to-jpg", "compress-image"]),

dict(slug="png-to-jpg", section="image", tool="convert", config={"to": "jpeg"},
 short="PNG to JPG", blurb="Shrink screenshots and graphics",
 title="PNG to JPG Converter – Free and Private | TechnoForesight",
 desc="Convert PNG images to smaller JPG files in your browser. Free, unlimited, no upload. Transparent areas become white.",
 h1="Convert PNG to JPG",
 lede="Make PNG images smaller and more compatible by converting them to JPG. Ideal for photos, screenshots you want to email and form uploads.",
 body="""
<h2>How to convert PNG to JPG</h2>
<ol><li>Choose or drop your PNG files.</li><li>Choose a quality, then select <strong>Convert to JPG</strong>.</li><li>Download the JPG files.</li></ol>
<h2>How much smaller will it get?</h2>
<p>For photos saved as PNG, JPG is usually 5 to 10 times smaller. For screenshots with large flat areas, the saving is smaller and text edges can look slightly soft. For screenshots of documents, keep the quality at 90% or higher.</p>
<h2>Transparency</h2>
<p>JPG cannot store transparency, so transparent pixels are filled with white. Keep the original PNG if you need the transparent version for design work.</p>
""",
 faq=[("Is anything uploaded?", PRIVACY_LINE),
      ("Can I get an exact file size?", "Yes. Use the image compressor and type the size you need, for example 50 KB."),
      ("Does it reduce resolution?", "No. The width and height stay the same. Only the file format changes.")],
 related=["jpg-to-png", "compress-image", "resize-image"]),

dict(slug="jpg-to-png", section="image", tool="convert", config={"to": "png"},
 short="JPG to PNG", blurb="Lossless copies for editing",
 title="JPG to PNG Converter – Free, No Upload | TechnoForesight",
 desc="Convert JPG images to PNG in your browser. Free, private, batch conversion with ZIP download.",
 h1="Convert JPG to PNG",
 lede="Save JPG photos as PNG for editing, design tools and apps that ask for PNG files.",
 body="""
<h2>How to convert JPG to PNG</h2>
<ol><li>Choose or drop your JPG images.</li><li>Select <strong>Convert to PNG</strong>.</li><li>Download the PNG files individually or as a ZIP.</li></ol>
<h2>What converting does and does not do</h2>
<p>PNG is lossless, so from now on the image will not lose any more quality when you edit and save it repeatedly. Converting cannot bring back detail the JPG has already lost, and it does not make the background transparent. The PNG file will usually be larger than the JPG.</p>
<p>When should you convert? When a website, app, or assignment specifically asks for PNG, or when you plan to make many edits to the same image.</p>
""",
 faq=[("Will the background become transparent?", "No. The image is copied exactly, including its background."),
      ("Is anything uploaded?", PRIVACY_LINE),
      ("Why is my PNG bigger?", "PNG stores every pixel without lossy compression, so photos take more space than as JPG.")],
 related=["png-to-jpg", "heic-to-png", "resize-image"]),

dict(slug="compress-image", section="image", tool="compress", config={"target": 100, "presets": [20, 50, 100, 200, 500, 1000]},
 short="Compress image to KB", blurb="Hit an exact size limit",
 title="Compress Image to KB – Exact Size, Free, No Upload | TechnoForesight",
 desc="Reduce image size to an exact KB target such as 20 KB, 50 KB, 100 KB or 200 KB. Free, unlimited and private: images never leave your device.",
 h1="Compress an image to an exact size",
 lede="Type the size you need, such as 50 KB or 200 KB, and get the sharpest image that fits under it.",
 body="""
<h2>How it works</h2>
<ol><li>Choose or drop one or more images (JPG, PNG, HEIC, WebP or AVIF).</li>
<li>Type the maximum size in KB, or tap one of the common sizes.</li>
<li>Select <strong>Compress images</strong>. The bar under each result shows the new size against your limit.</li></ol>
<p>The tool first lowers the JPG quality step by step to find the best quality that fits. Only if that is not enough does it reduce the pixel dimensions, a little at a time. That gives you the clearest image the limit allows.</p>
<h2>Picking a size</h2>
<ul><li><strong>20 KB or less</strong>: signatures and thumb impressions on application forms. See <a href="/compress-image-to-20kb">compress image to 20 KB</a>.</li>
<li><strong>50 KB</strong>: passport-style photos on most job and exam portals. See <a href="/compress-image-to-50kb">compress image to 50 KB</a>.</li>
<li><strong>100 to 200 KB</strong>: document photos, ID proofs and profile pictures. See <a href="/compress-image-to-100kb">compress image to 100 KB</a>.</li>
<li><strong>500 KB to 1 MB</strong>: email attachments and website images that should still look sharp.</li></ul>
<h2>Need a fixed width and height as well?</h2>
<p>Many forms ask for exact pixel dimensions as well as a size limit. Use the <a href="/exam-photo-signature-resizer">photo and signature resizer</a>, which sets both at once.</p>
""",
 faq=[("Are my images uploaded?", PRIVACY_LINE),
      ("Why is my image still not under the limit?", "Very small targets on very large or detailed images need a big reduction in dimensions. Enter a maximum width, such as 800 pixels, to help the compressor."),
      ("Should I choose JPG or WebP?", "Choose JPG for forms, email and printing. Choose WebP only for your own website, where it gives smaller files at the same quality."),
      ("Can I compress many photos at once?", "Yes. Add as many as you like and download them all as one ZIP file.")],
 related=["compress-image-to-20kb", "compress-image-to-50kb", "compress-image-to-100kb", "resize-image"]),

dict(slug="compress-image-to-100kb", section="image", tool="compress", config={"target": 100, "presets": [80, 100, 150, 200]},
 short="Compress image to 100 KB", blurb="For ID proofs and documents",
 title="Compress Image to 100 KB – Free and Private | TechnoForesight",
 desc="Reduce JPG, PNG or HEIC images to 100 KB or less. Ideal for ID proofs, certificates and profile photos. Free and private.",
 h1="Compress an image to 100 KB",
 lede="Shrink photos of documents, ID cards and certificates to 100 KB or less while keeping the text readable.",
 body="""
<h2>How to compress to 100 KB</h2>
<ol><li>Choose your images. You can add several documents at once.</li><li>Keep the target at 100 KB or pick another size.</li><li>Select <strong>Compress images</strong> and download.</li></ol>
<h2>Keeping document text readable</h2>
<p>Text needs sharp edges, so for document photos it is better to reduce the dimensions a little than to lower quality a lot. Enter a maximum width of about 1200 pixels: that is enough for an A4 page to stay readable on screen, and it leaves more of the 100 KB for sharpness.</p>
<p>If the portal wants a PDF instead of an image, convert your photos with <a href="/jpg-to-pdf">JPG to PDF</a>, then use <a href="/compress-pdf-to-100kb">compress PDF to 100 KB</a>.</p>
""",
 faq=[("Is anything uploaded?", PRIVACY_LINE),
      ("My document is unreadable at 100 KB. What can I do?", "Crop away the table or background around the document before compressing, and set a maximum width of about 1200 pixels."),
      ("Does it work with PNG screenshots?", "Yes. They are saved as JPG, which is much smaller for this kind of image.")],
 related=["compress-image", "jpg-to-pdf", "compress-pdf-to-100kb"]),

dict(slug="resize-image", section="image", tool="resize", config={},
 short="Resize image", blurb="Pixels, cm, mm or inches",
 title="Resize Image Online – Pixels, cm, mm, Inches | TechnoForesight",
 desc="Resize images to exact pixels, centimetres, millimetres or inches. Free, batch resizing, no upload.",
 h1="Resize an image",
 lede="Change the width and height of images in pixels, centimetres, millimetres or inches. Resize one image or a whole batch.",
 body="""
<h2>How to resize</h2>
<ol><li>Choose or drop your images.</li>
<li>Enter a width. Leave the height empty to keep the original proportions, or enter both to set an exact size.</li>
<li>Choose the unit. For cm, mm and inches, pick the print resolution (300 DPI is standard for printing).</li>
<li>Select <strong>Resize images</strong> and download.</li></ol>
<h2>Pixels or centimetres?</h2>
<p>Screens care about pixels. Paper cares about physical size. When a form asks for a photo “3.5 × 4.5 cm”, it usually means the pixel size that prints at that size at a given resolution. At 300 DPI that is 413 × 531 pixels, which is what this tool calculates for you.</p>
<h2>Entering both width and height</h2>
<p>If the proportions you type differ from the photo's, the image is stretched to fit. To crop instead of stretching, use the <a href="/exam-photo-signature-resizer">photo and signature resizer</a>, which crops to fill the exact size.</p>
""",
 faq=[("Is anything uploaded?", PRIVACY_LINE),
      ("Can I make an image bigger?", "Yes, but enlarging cannot add real detail, so large increases look soft."),
      ("How do I reach a file size limit too?", "Resize first, then use the image compressor with the KB limit you need.")],
 related=["compress-image", "exam-photo-signature-resizer", "passport-photo-sheet"]),
]
