"""Extra guide sections appended below a tool page's main content.
Keyed by slug. Keep each guide practical: steps, numbers, troubleshooting.
Links like href="/slug" are pointed at the tool's current URL automatically.
"""

GUIDES = {

"heic-to-jpg": """
<h2>Open HEIC files on Windows, Mac and Android</h2>
<p>Whether you need to convert depends on where the photo is going.</p>
<ul>
<li><strong>Windows 10 and 11</strong> show HEIC only after you install the HEIF Image Extensions from the Microsoft Store, and some photos also need the HEVC Video Extensions, which cost a small fee. Even then, many websites and older programs still reject the files.</li>
<li><strong>Mac</strong> opens HEIC in Preview and Photos without any extra software. Converting is still useful when you send photos to someone on Windows or upload them to a form.</li>
<li><strong>Android</strong> phones can usually display HEIC in recent versions, but apps and websites you upload to may not accept it.</li>
</ul>
<h2>Copy iPhone photos as JPG automatically</h2>
<p>If you move photos to a computer with a cable, open <strong>Settings → Photos</strong> on the iPhone and, under Transfer to Mac or PC, choose <strong>Automatic</strong>. The iPhone then converts photos to JPG as they copy. This does not help with photos you have already copied, emailed or downloaded from iCloud, which is where this converter comes in.</p>
<h2>Choosing the right quality</h2>
<table>
<tr><th>Use</th><th>Suggested quality</th><th>Typical size for a 12 MP photo</th></tr>
<tr><td>Printing or editing</td><td>95 to 100%</td><td>4 to 7 MB</td></tr>
<tr><td>Sharing and email</td><td>85 to 90%</td><td>2 to 4 MB</td></tr>
<tr><td>Websites and chat apps</td><td>70 to 80%</td><td>1 to 2 MB</td></tr>
</table>
<p>If a form needs a specific size such as 100 KB, convert at 90% first, then use the <a href="/compress-image">image compressor</a> to reach the exact limit.</p>
<h2>Troubleshooting</h2>
<ul>
<li><strong>A photo will not open:</strong> some HEIC files are actually Live Photo videos or bursts. Export the still photo from the Photos app and try again.</li>
<li><strong>The converted photo looks rotated:</strong> the converter applies the orientation your camera saved. If a photo still looks wrong, it was probably rotated in an editing app that did not save the change.</li>
<li><strong>Conversion is slow:</strong> HEIC decoding is heavy work done on your own device. Large batches convert faster on a laptop than on an older phone.</li>
</ul>
""",

"webp-to-png": """
<h2>What WebP is and why websites use it</h2>
<p>WebP is an image format released by Google in 2010. It supports both lossy compression, like JPG, and lossless compression, like PNG, along with transparency and animation. Because WebP files are usually 25 to 35% smaller than comparable JPG or PNG files, most large websites, online shops and content delivery networks now serve images as WebP to load pages faster.</p>
<p>The side effect is that images you save from the web often arrive as .webp files, which some tools still do not handle well.</p>
<h2>Programs that may not open WebP</h2>
<ul>
<li>Older versions of Microsoft Office, Windows Photo Viewer and some print software.</li>
<li>Government, exam and job application portals that only accept JPG or PNG.</li>
<li>Some email clients, older Android galleries and design tools set up before WebP became common.</li>
</ul>
<h2>PNG or JPG: which to choose</h2>
<table>
<tr><th>Choose PNG when</th><th>Choose JPG when</th></tr>
<tr><td>The image has a transparent background, such as a logo or sticker</td><td>The image is a photo with no transparency</td></tr>
<tr><td>You will edit the image further</td><td>You need a small file to share or upload</td></tr>
<tr><td>It contains text, diagrams or screenshots that must stay sharp</td><td>A form or website asks for JPG</td></tr>
</table>
<p>For photos, <a href="/webp-to-jpg">WebP to JPG</a> gives a much smaller file than PNG.</p>
<h2>Troubleshooting</h2>
<ul>
<li><strong>Only the first frame converted:</strong> animated WebP files contain several frames. The converter saves the first frame as a still image.</li>
<li><strong>The PNG is much bigger than the WebP:</strong> this is expected. PNG stores every pixel without lossy compression.</li>
<li><strong>The file will not open at all:</strong> check the file really is WebP. Some sites serve AVIF images, which also work here if your browser is up to date.</li>
</ul>
""",

"webp-to-jpg": """
<h2>Why images save as WebP</h2>
<p>When you right-click an image on a website and save it, you usually get whatever format the site serves, and most large sites now serve WebP because it loads faster. Google Chrome, Edge and other browsers save the file exactly as it arrived, so a product photo or wallpaper can end up as a .webp file even though the page looked like an ordinary picture.</p>
<h2>When you need JPG instead</h2>
<ul>
<li>Uploading a photo to a government, exam, bank or job portal that lists JPG as the only accepted format.</li>
<li>Printing at a photo shop or kiosk.</li>
<li>Inserting images into older versions of Word, PowerPoint or other office software.</li>
<li>Sending photos to someone whose phone or computer cannot preview WebP.</li>
</ul>
<h2>Picking a quality setting</h2>
<p>WebP images on websites are already compressed, so converting at 100% will not bring back lost detail; it only makes the file larger. A quality of 85 to 92% keeps the image looking the same as the original. If the JPG must be under a size limit, set the quality to 90% here and then use the <a href="/compress-image">image compressor</a> with the exact limit.</p>
<h2>What happens to transparency</h2>
<p>JPG has no transparency, so transparent areas become white. That is usually fine for photos, but logos and stickers will gain a white box around them. For those, use <a href="/webp-to-png">WebP to PNG</a> to keep the transparent background.</p>
<h2>Troubleshooting</h2>
<ul>
<li><strong>“This browser cannot save JPG files”:</strong> this should not happen in any current browser. Update your browser and reload the page.</li>
<li><strong>Converted image looks blurry:</strong> the original WebP was small or heavily compressed. Converting cannot add detail; look for a larger version of the image.</li>
<li><strong>Many files at once:</strong> add them all, convert, and use Download all as ZIP.</li>
</ul>
""",

"compress-image": """
<h2>KB, MB and why your file may still be rejected</h2>
<p>Websites count file sizes in two slightly different ways. Most operating systems use 1 KB = 1,024 bytes, while some portals check against 1 KB = 1,000 bytes. A file shown as 49.5 KB on your computer can be 50,688 bytes, which a strict portal reads as over a 50 KB limit. To be safe, aim about 5% below the limit, for example 47 KB for a 50 KB rule.</p>
<p>1 MB is 1,024 KB, so a 2 MB limit allows roughly 2,048 KB.</p>
<h2>What really controls image file size</h2>
<ul>
<li><strong>Pixel dimensions:</strong> a 4000 × 3000 phone photo has 12 million pixels. Halving the width and height cuts that to 3 million, roughly a quarter of the data.</li>
<li><strong>Compression quality:</strong> lower JPG quality removes fine detail. Between 70% and 90% the difference is hard to see; below 50% blocks and smudges appear.</li>
<li><strong>Content:</strong> busy scenes, grass, hair and noise compress poorly. Plain backgrounds and documents compress well.</li>
<li><strong>Not DPI:</strong> the DPI value stored in a file does not change its size in KB. Only dimensions and compression do.</li>
</ul>
<h2>Sizes commonly asked for</h2>
<table>
<tr><th>Upload</th><th>Common limit</th><th>Tip</th></tr>
<tr><td>Signature</td><td>10 to 20 KB</td><td>Crop tightly around the signature first</td></tr>
<tr><td>Passport-style photo</td><td>20 to 50 KB</td><td>Crop to head and shoulders</td></tr>
<tr><td>ID proof or certificate image</td><td>100 to 300 KB</td><td>Set a maximum width of about 1200 px</td></tr>
<tr><td>Email attachment</td><td>1 to 2 MB per photo</td><td>Quality 80% keeps photos sharp</td></tr>
</table>
<p>These are common examples, not official rules. Always follow the limits stated on the form you are filling in.</p>
<h2>Troubleshooting</h2>
<ul>
<li><strong>The result looks blocky:</strong> the limit is too small for the image size. Enter a smaller maximum width so the compressor can keep quality higher.</li>
<li><strong>The file is below the minimum size:</strong> some forms reject files that are too small. Try a slightly higher target or use the <a href="/exam-photo-signature-resizer">photo and signature resizer</a>, which handles minimum and maximum sizes together.</li>
<li><strong>The form wants exact pixel dimensions:</strong> use the photo and signature resizer instead, which sets dimensions and size in one step.</li>
</ul>
""",

"compress-image-to-20kb": """
<h2>How to photograph a signature for a 20 KB limit</h2>
<ol>
<li>Sign on plain white paper with a black or dark blue ballpoint or gel pen. Avoid pencil and light blue ink, which fade after compression.</li>
<li>Sign a little larger than usual, inside a box roughly 7 cm wide and 3 cm high.</li>
<li>Place the paper on a flat surface near a window. Hold the phone directly above it so the edges of the paper look straight, not slanted.</li>
<li>Turn off the flash, which can leave a bright patch, and tap the screen to focus on the ink.</li>
<li>Crop the photo close to the signature in your phone's editor, leaving a small white margin, then compress it here.</li>
</ol>
<h2>Why signatures compress so well</h2>
<p>A signature is mostly white paper with a few dark lines. JPG compression handles large plain areas very efficiently, which is why even a tightly cropped high-resolution signature usually fits under 20 KB without visible loss. Shadows, paper texture and a grey background make the file larger, so good light helps more than any setting.</p>
<h2>Thumb impressions and small photos</h2>
<p>Thumb impressions follow the same steps: use a stamp pad, press the thumb once on white paper, photograph it straight on, and crop closely. Faces are harder: at 20 KB a portrait loses detail quickly. If a form allows a larger size for the photo, such as 50 KB, use <a href="/compress-image-to-50kb">compress to 50 KB</a> for the photo and keep 20 KB for the signature.</p>
<h2>Checking before you upload</h2>
<ul>
<li>Open the compressed file and zoom in: every letter of the signature should be readable.</li>
<li>Check the file type is .jpg if the form asks for JPG or JPEG; they are the same format.</li>
<li>Check the size shown under the result is inside both the minimum and the maximum the form allows.</li>
<li>If the form also gives pixel dimensions, such as 140 × 60, use the <a href="/exam-photo-signature-resizer">photo and signature resizer</a>.</li>
</ul>
""",

"compress-image-to-50kb": """
<h2>Taking a photo that compresses well</h2>
<p>A clean, evenly lit photo stays sharp at 50 KB; a dark, noisy one turns blotchy. Before compressing:</p>
<ol>
<li>Stand against a plain white or light wall, facing a window or soft light, so there are no strong shadows on your face.</li>
<li>Ask someone to take the photo from about 1 metre away at eye level, rather than taking a selfie at arm's length, which distorts the face.</li>
<li>Look straight at the camera with a neutral expression, ears and eyebrows visible, and no cap or dark glasses unless the rules allow them.</li>
<li>Crop to head and shoulders, so the face takes up most of the frame.</li>
</ol>
<h2>Typical photo rules on Indian application forms</h2>
<table>
<tr><th>Requirement</th><th>Common examples</th></tr>
<tr><td>File size</td><td>20 to 50 KB, sometimes up to 100 or 200 KB</td></tr>
<tr><td>Dimensions</td><td>200 × 230 px, or 3.5 × 4.5 cm (413 × 531 px at 300 DPI)</td></tr>
<tr><td>Format</td><td>JPG or JPEG</td></tr>
<tr><td>Background</td><td>White or light coloured</td></tr>
<tr><td>Recency</td><td>Taken within the last 3 to 6 months</td></tr>
</table>
<p>These are common patterns, not the rules of any particular exam. Each notification lists its own requirements, and they change from year to year. When the form gives exact dimensions as well as a size, use the <a href="/exam-photo-signature-resizer">photo and signature resizer</a>, which handles both.</p>
<h2>Common reasons a photo is rejected</h2>
<ul>
<li>File size outside the allowed range, either too large or too small.</li>
<li>Wrong format, for example PNG or HEIC from an iPhone instead of JPG.</li>
<li>Face too small in the frame, or the photo is a full-length picture.</li>
<li>Blurred, dark or heavily filtered photos, or photos with a coloured background when white is required.</li>
</ul>
<h2>Printing the same photo</h2>
<p>If you also need printed copies, the <a href="/passport-photo-sheet">passport photo sheet maker</a> arranges many copies on one A4 page or 4 × 6 photo paper.</p>
""",

"exam-photo-signature-resizer": """
<h2>Converting centimetres to pixels</h2>
<p>Forms often give a size in centimetres, but an image file is measured in pixels. The conversion depends on the print resolution (DPI): pixels = centimetres ÷ 2.54 × DPI. At the standard 300 DPI:</p>
<table>
<tr><th>Size in cm</th><th>Pixels at 300 DPI</th><th>Pixels at 200 DPI</th></tr>
<tr><td>2.5 × 3.5 cm</td><td>295 × 413</td><td>197 × 276</td></tr>
<tr><td>3.5 × 4.5 cm</td><td>413 × 531</td><td>276 × 354</td></tr>
<tr><td>5 × 5 cm</td><td>591 × 591</td><td>394 × 394</td></tr>
<tr><td>6 × 2 cm (signature)</td><td>709 × 236</td><td>472 × 157</td></tr>
</table>
<p>If the notification gives both centimetres and pixels, always use the pixel numbers.</p>
<h2>Crop to fill or fit inside?</h2>
<ul>
<li><strong>Crop to fill</strong> trims the edges of the photo so it fills the whole size exactly. Use it for photos; choose Keep the face so the top of the head is not cut off.</li>
<li><strong>Fit inside</strong> keeps the whole image and adds white space around it. Use it for signatures and thumb impressions, where nothing should be cut.</li>
</ul>
<h2>Reading the result</h2>
<p>Each result shows the final width and height, the file size and a bar comparing the size with your maximum. If the file comes out below the minimum, the tool tries the highest quality first. A small, simple image such as a short signature can still fall below a minimum like 10 KB; in that case photograph the signature larger and more sharply, or use the slightly larger dimensions the rules allow.</p>
<h2>Before you submit</h2>
<ul>
<li>Upload the photo and signature in the right boxes: forms often reject a signature uploaded as the photo.</li>
<li>Keep the original photo; you may need it again in a different size for the admit card stage or another exam.</li>
<li>If the portal shows a preview, check that the face and signature are clear before final submission, which usually cannot be changed later.</li>
</ul>
""",

"compress-pdf": """
<h2>Why some PDFs are so large</h2>
<p>A PDF made from a word processor stores text as text, so even a long report is usually small. Large PDFs almost always contain images: scanned pages, phone photos of documents, or high-resolution pictures. A single colour page scanned at 300 DPI can be 1 to 3 MB, so a 10-page scan easily reaches 20 MB.</p>
<h2>How this compressor works</h2>
<p>The tool redraws every page as an image at a resolution and quality chosen to fit your target, starting at the highest quality and stepping down until the whole file fits. This works on any PDF and reaches small limits reliably, but it has one trade-off: text in the result can no longer be selected or searched. For scanned documents that does not matter, because their text was already part of an image.</p>
<h2>How small can a PDF get?</h2>
<table>
<tr><th>Document</th><th>Realistic target</th></tr>
<tr><td>1 scanned page, black and white</td><td>50 to 100 KB</td></tr>
<tr><td>1 scanned page, colour</td><td>100 to 200 KB</td></tr>
<tr><td>5-page scanned document</td><td>300 KB to 1 MB</td></tr>
<tr><td>20-page scanned document</td><td>1 to 3 MB</td></tr>
</table>
<p>Pushing far below these targets makes text hard to read. If a portal's limit is very small, upload fewer pages: <a href="/split-pdf">split the PDF</a> and submit only the pages asked for.</p>
<h2>Getting the best result</h2>
<ul>
<li><strong>Turn on black and white</strong> for text documents, certificates and forms without colour stamps. It often halves the size.</li>
<li><strong>Crop scans before making the PDF:</strong> table edges and backgrounds around the paper waste space. Use <a href="/jpg-to-pdf">JPG to PDF</a> on cropped photos.</li>
<li><strong>Check readability:</strong> open the result and zoom into the smallest text, such as registration numbers and dates, before uploading.</li>
<li><strong>Keep the original:</strong> the compressed copy is for uploading, not for archiving.</li>
</ul>
""",

"merge-pdf": """
<h2>Ordering pages before you merge</h2>
<p>Files are merged in the order shown in the list. Use the arrows to move a file up or down before you press Merge PDFs. A quick way to avoid mistakes is to name files with numbers before adding them, for example 01-application.pdf, 02-certificate.pdf and 03-id-proof.pdf; they are then easy to put in order at a glance.</p>
<h2>Common uses</h2>
<ul>
<li>Combining an application form, certificates and ID proof into the single PDF a portal asks for.</li>
<li>Joining pages scanned one at a time into one document.</li>
<li>Putting monthly statements or invoices together for an accountant or a loan application.</li>
<li>Assembling a report from separate chapters.</li>
</ul>
<h2>What merging keeps and what it does not</h2>
<table>
<tr><th>Kept</th><th>Not kept</th></tr>
<tr><td>Page content, text you can select, images and page sizes</td><td>Bookmarks and outlines from the original files</td></tr>
<tr><td>Links within the pages</td><td>Form fields may stop working in some files</td></tr>
<tr><td>Original quality: nothing is compressed</td><td>Passwords: protected files cannot be merged</td></tr>
</table>
<h2>Merged file too large?</h2>
<p>Merging adds the file sizes together. If the result is over an upload limit, run it through <a href="/compress-pdf">compress PDF</a>, or compress the largest scanned file first and merge again. To remove a page you do not need, use <a href="/split-pdf">split PDF</a> to extract only the pages you want.</p>
<h2>Troubleshooting</h2>
<ul>
<li><strong>“Password-protected”:</strong> open the file with its password in a PDF reader and save or print it to a new PDF, then merge that copy.</li>
<li><strong>“Could not be opened”:</strong> the file may be damaged or not a real PDF. Try opening it in your browser; if that fails, download it again from the source.</li>
<li><strong>Pages sideways after merging:</strong> fix them with <a href="/rotate-pdf">rotate PDF</a>.</li>
</ul>
""",

"jpg-to-pdf": """
<h2>Scanning documents with your phone</h2>
<p>Good photos make a clean, small PDF. For each page:</p>
<ol>
<li>Lay the page flat on a dark table so the paper's edges stand out.</li>
<li>Use daylight or a bright room and turn off the flash, which causes glare.</li>
<li>Hold the phone directly above the page so it looks rectangular, not slanted.</li>
<li>Crop to the page edges in your phone's photo editor before adding the photos here.</li>
</ol>
<h2>Choosing page size and orientation</h2>
<table>
<tr><th>Setting</th><th>Use it when</th></tr>
<tr><td>A4</td><td>Documents for India, the UK, Europe and most of the world</td></tr>
<tr><td>US Letter</td><td>Documents for the USA and Canada</td></tr>
<tr><td>Same as each image</td><td>Photos, screenshots or slides where you want no white border</td></tr>
<tr><td>Automatic orientation</td><td>Mixed portrait and landscape pages in one file</td></tr>
</table>
<p>Small margins give a neat printed look. Choose no margin when every bit of the page matters, such as receipts or narrow certificates.</p>
<h2>Keeping the PDF under a size limit</h2>
<p>Each phone photo is often 2 to 5 MB, so a few pages can create a large PDF. The tool already reduces very large photos to a sensible print size. If the result is still over a portal's limit, use <a href="/compress-pdf">compress PDF</a> with the exact limit, and turn on black and white for text documents.</p>
<h2>Troubleshooting</h2>
<ul>
<li><strong>Pages in the wrong order:</strong> rearrange the images with the arrows before creating the PDF.</li>
<li><strong>A page is sideways:</strong> rotate the photo in your phone first, or fix the PDF afterwards with <a href="/rotate-pdf">rotate PDF</a>.</li>
<li><strong>iPhone photos:</strong> HEIC photos work directly; there is no need to convert them first. See also <a href="/heic-to-pdf">HEIC to PDF</a>.</li>
</ul>
""",

"heic-to-png": """
<h2>When PNG is worth the extra size</h2>
<p>A 12-megapixel iPhone photo is usually 1 to 3 MB as HEIC, 3 to 5 MB as JPG and 15 to 25 MB as PNG. That size buys you an exact copy: every later save in an editor keeps full quality, which matters if you retouch, crop repeatedly or combine the photo with graphics and text.</p>
<ul>
<li><strong>Choose PNG</strong> for editing in Photoshop, GIMP, Canva or Figma, for photos of documents where text must stay crisp, and for archiving.</li>
<li><strong>Choose JPG</strong> for sharing, email, printing at a shop and uploading to forms. Use <a href="/heic-to-jpg">HEIC to JPG</a>.</li>
</ul>
<h2>Troubleshooting</h2>
<ul>
<li><strong>Download is slow on a phone:</strong> PNG files are large. Convert fewer photos at a time, or use JPG.</li>
<li><strong>No transparent background:</strong> camera photos have no transparency; PNG keeps the background exactly as it was.</li>
<li><strong>Need a smaller copy later:</strong> the <a href="/compress-image">image compressor</a> turns the PNG into a JPG of any size you choose.</li>
</ul>
""",

"avif-to-jpg": """
<h2>Where AVIF files come from</h2>
<p>AVIF is based on the AV1 video codec and often makes images 30 to 50% smaller than JPG at similar quality. Many websites now serve AVIF to browsers that support it, so saving an image can give you an .avif file. Some recent phones and cameras can also save photos as AVIF.</p>
<h2>Why convert to JPG</h2>
<ul>
<li>Many photo viewers, office programs and print services do not open AVIF yet.</li>
<li>Upload forms on job, exam and government portals almost always ask for JPG.</li>
<li>JPG works on every phone and computer without extra software.</li>
</ul>
<h2>Quality tips</h2>
<p>AVIF images from websites are already compressed, so 85 to 90% quality is enough; converting at 100% only makes the file bigger. If you need the transparent background of a logo or product image, use <a href="/avif-to-png">AVIF to PNG</a> instead, because JPG fills transparent areas with white.</p>
<h2>Troubleshooting</h2>
<ul>
<li><strong>A file will not open:</strong> update your browser. Safari needs version 16 or later to read AVIF.</li>
<li><strong>Very large AVIF images:</strong> converting a large batch uses a lot of memory on older phones; convert a few at a time.</li>
</ul>
""",

"avif-to-png": """
<h2>Troubleshooting</h2>
<ul>
<li><strong>The converted image has a white background:</strong> the original AVIF had no transparency. PNG keeps exactly what was there.</li>
<li><strong>Need a smaller file afterwards:</strong> use the <a href="/compress-image">image compressor</a> to save a JPG or WebP at the size you need.</li>
<li><strong>Converting on a phone:</strong> this works in current mobile Chrome and Safari 16 or later. Large batches are quicker on a computer.</li>
</ul>
<h2>Using the PNG in documents and designs</h2>
<p>PNG images with transparency sit cleanly on coloured slide backgrounds and document headers in PowerPoint, Google Slides, Word and Canva. If an app shows a black background where transparency should be, it does not support transparent PNG; place the image on a white background in an editor first, or convert to JPG with <a href="/avif-to-jpg">AVIF to JPG</a>.</p>
""",

"png-to-jpg": """
<h2>How much smaller will the JPG be?</h2>
<table>
<tr><th>Kind of PNG</th><th>Typical saving as JPG at 90%</th></tr>
<tr><td>Photo saved as PNG</td><td>80 to 90% smaller</td></tr>
<tr><td>Screenshot of a web page or app</td><td>50 to 80% smaller</td></tr>
<tr><td>Simple logo or diagram with flat colours</td><td>Little saving; PNG may already be smaller</td></tr>
</table>
<p>For flat graphics with few colours, PNG is often the better format already. JPG pays off for photos and complex screenshots.</p>
<h2>Keeping text readable in screenshots</h2>
<p>JPG compression can blur the edges of small text. For screenshots that contain text, keep the quality at 90% or higher, and avoid shrinking the image afterwards. If the screenshot is for a website, <a href="/png-to-webp">PNG to WebP</a> gives a smaller file with sharper text than JPG.</p>
<h2>Troubleshooting</h2>
<ul>
<li><strong>Transparent areas turned white:</strong> JPG has no transparency. Keep the PNG for designs that need it.</li>
<li><strong>Need an exact size limit:</strong> use the <a href="/compress-image">image compressor</a> and type the size in KB.</li>
</ul>
""",

"jpg-to-png": """
<h2>Common reasons to convert JPG to PNG</h2>
<ul>
<li>A website, app store listing or assignment specifically requires PNG.</li>
<li>You will edit the image many times and want to avoid the extra loss each JPG save adds.</li>
<li>You plan to remove the background later in an editor, which needs a format that supports transparency.</li>
</ul>
<h2>What to expect</h2>
<table>
<tr><th>Question</th><th>Answer</th></tr>
<tr><td>Will quality improve?</td><td>No. PNG keeps the JPG exactly as it is; it cannot restore detail already lost.</td></tr>
<tr><td>Will the file be bigger?</td><td>Yes, usually 3 to 10 times bigger for photos.</td></tr>
<tr><td>Will the background become transparent?</td><td>No. Use a background remover in an editor for that.</td></tr>
</table>
<h2>Troubleshooting</h2>
<ul>
<li><strong>PNG too large to upload:</strong> check whether the site also accepts JPG or WebP. If it needs PNG under a size limit, reduce the pixel dimensions with <a href="/resize-image">resize image</a> first.</li>
</ul>
""",

"jpg-to-webp": """
<h2>Choosing quality for web images</h2>
<table>
<tr><th>Image</th><th>Suggested quality</th></tr>
<tr><td>Product photos and hero banners</td><td>82 to 88%</td></tr>
<tr><td>Blog and article photos</td><td>75 to 82%</td></tr>
<tr><td>Thumbnails</td><td>70 to 75%</td></tr>
</table>
<p>Resize images to the largest width your site displays before converting; a 4000-pixel photo shown at 1200 pixels wastes most of its data. Use <a href="/resize-image">resize image</a> first, then convert.</p>
<h2>Adding WebP images to your website</h2>
<p>Most website builders, WordPress, Shopify and modern frameworks accept WebP uploads directly. If you hand-write HTML, a normal img tag pointing at the .webp file works in every current browser.</p>
<h2>Troubleshooting</h2>
<ul>
<li><strong>Safari cannot save WebP:</strong> older Safari versions can display WebP but not create it. Use Chrome, Edge or Firefox for converting.</li>
<li><strong>Colours look slightly different:</strong> some photos carry colour profiles that browsers handle differently. Converting at 90% or higher keeps the difference minimal.</li>
</ul>
""",

"png-to-webp": """
<h2>Lossy or near-lossless?</h2>
<p>This converter saves lossy WebP with transparency. At 90% quality and above, logos, icons and screenshots look the same as the PNG to almost everyone while being much smaller. For pixel-art or images where every pixel must be exact, keep the PNG.</p>
<h2>Typical savings</h2>
<table>
<tr><th>Image</th><th>Typical WebP size compared with PNG</th></tr>
<tr><td>Product photo with transparent background</td><td>70 to 90% smaller</td></tr>
<tr><td>Screenshot with text</td><td>40 to 70% smaller</td></tr>
<tr><td>Small flat icon</td><td>Similar size; little benefit</td></tr>
</table>
<h2>Troubleshooting</h2>
<ul>
<li><strong>The app I use only accepts PNG:</strong> keep the PNG for that app; WebP is mainly for websites.</li>
<li><strong>Edges of transparent areas look rough:</strong> raise the quality to 95%.</li>
<li><strong>Converting fails in Safari:</strong> use Chrome, Edge or Firefox, which can create WebP files.</li>
</ul>
""",

"compress-image-to-100kb": """
<h2>Getting a readable document photo under 100 KB</h2>
<ol>
<li>Photograph the document flat, in daylight, with the phone held directly above it.</li>
<li>Crop to the edges of the paper, so no table or background is included.</li>
<li>Enter a maximum width of 1200 pixels in the compressor; this keeps an A4 page readable on screen.</li>
<li>Keep the target at 100 KB, or a little below, such as 95 KB, for strict portals.</li>
</ol>
<h2>What fits in 100 KB</h2>
<table>
<tr><th>Image</th><th>Result at 100 KB</th></tr>
<tr><td>One A4 page of printed text</td><td>Clearly readable at 1200 px wide</td></tr>
<tr><td>ID card front</td><td>Sharp, with plenty of room</td></tr>
<tr><td>Full-colour certificate with seals</td><td>Readable; fine detail softens slightly</td></tr>
<tr><td>Profile photo</td><td>Sharp at up to about 800 × 800 px</td></tr>
</table>
<h2>Troubleshooting</h2>
<ul>
<li><strong>Small print is blurred:</strong> crop tighter or raise the maximum width; a slightly larger image at lower quality reads better than a tiny one.</li>
<li><strong>The portal needs a PDF:</strong> make one with <a href="/jpg-to-pdf">JPG to PDF</a>, then use <a href="/compress-pdf-to-100kb">compress PDF to 100 KB</a>.</li>
</ul>
""",

"resize-image": """
<h2>Common sizes</h2>
<table>
<tr><th>Use</th><th>Size</th></tr>
<tr><td>Passport photo, India, UK and EU</td><td>3.5 × 4.5 cm (413 × 531 px at 300 DPI)</td></tr>
<tr><td>US passport photo</td><td>2 × 2 in (600 × 600 px at 300 DPI)</td></tr>
<tr><td>Website hero or banner</td><td>1920 px wide</td></tr>
<tr><td>Blog or article image</td><td>1200 px wide</td></tr>
<tr><td>Instagram square post</td><td>1080 × 1080 px</td></tr>
<tr><td>YouTube thumbnail</td><td>1280 × 720 px</td></tr>
</table>
<h2>Resizing and file size</h2>
<p>Halving the width and height leaves a quarter of the pixels, which usually cuts the file size by about three quarters. If you need both a pixel size and a KB limit, resize here first, then use the <a href="/compress-image">image compressor</a>. For forms that specify both, the <a href="/exam-photo-signature-resizer">photo and signature resizer</a> does it in one step.</p>
<h2>Troubleshooting</h2>
<ul>
<li><strong>The image looks stretched:</strong> you entered both width and height in a different ratio from the photo. Leave one empty to keep proportions.</li>
<li><strong>Printed size is wrong:</strong> print at 100% or actual size, not fit to page.</li>
</ul>
""",

"passport-photo-sheet": """
<h2>Photo requirements to check first</h2>
<ul>
<li>A recent photo with a plain white or off-white background and even lighting.</li>
<li>Face looking straight at the camera, eyes open, neutral expression.</li>
<li>Head and top of shoulders visible, with the face filling most of the frame.</li>
<li>No filters or beauty effects, and no shadows on the face or background.</li>
</ul>
<p>Rules vary by country and document, so check the official instructions for your passport, visa or ID card.</p>
<h2>Printing tips</h2>
<table>
<tr><th>Where</th><th>What to print</th></tr>
<tr><td>Home inkjet or laser printer</td><td>The PDF on A4 photo paper, at 100% scale</td></tr>
<tr><td>Photo shop or kiosk, 4 × 6 print</td><td>The JPG created with the 4 × 6 paper option</td></tr>
<tr><td>Local print shop on A4</td><td>The PDF; ask them to print at actual size</td></tr>
</table>
<p>After printing, measure one photo with a ruler: it should be exactly 3.5 × 4.5 cm, or 2 × 2 inches for the US size.</p>
""",

"split-pdf": """
<h2>Choosing the right mode</h2>
<table>
<tr><th>Mode</th><th>Use it to</th></tr>
<tr><td>Extract pages into one PDF</td><td>Send only pages 1, 3 and 5 of a statement as one file</td></tr>
<tr><td>One PDF for each range</td><td>Separate a scanned bundle into several documents, such as 1-2, 3-5 and 6-8</td></tr>
<tr><td>Every page as its own PDF</td><td>Upload pages separately to a portal that wants one page per box</td></tr>
</table>
<h2>Tips</h2>
<ul>
<li>Check page numbers in your PDF reader first; the first page of the file is always page 1, even if it is printed as page i or cover.</li>
<li>Splitting does not reduce quality or change page sizes.</li>
<li>To combine the pieces differently later, use <a href="/merge-pdf">merge PDF</a>.</li>
<li>If each piece must be under a size limit, compress them with <a href="/compress-pdf">compress PDF</a>.</li>
</ul>
""",

"rotate-pdf": """
<h2>Fixing a document with mixed orientation</h2>
<p>Scanned bundles often have a few landscape pages, such as tables or certificates, among portrait pages. Enter only those page numbers, for example 3, 7-8, choose the direction, and the rest stay as they are. Run the tool again with different pages and directions if some pages need turning the other way.</p>
<h2>Which way to rotate</h2>
<table>
<tr><th>The page appears</th><th>Choose</th></tr>
<tr><td>Lying on its left side (text reads bottom to top)</td><td>90° clockwise</td></tr>
<tr><td>Lying on its right side (text reads top to bottom)</td><td>90° anticlockwise</td></tr>
<tr><td>Upside down</td><td>180°</td></tr>
</table>
<h2>Tips</h2>
<ul>
<li>Rotation is saved in the file, so the pages show correctly in every viewer and on upload portals.</li>
<li>Rotating does not change quality or file size.</li>
<li>Password-protected PDFs need to be unlocked with their password first.</li>
</ul>
""",

"pdf-to-jpg": """
<h2>Choosing resolution</h2>
<table>
<tr><th>Setting</th><th>A4 page becomes</th><th>Good for</th></tr>
<tr><td>Small (96 DPI)</td><td>794 × 1123 px</td><td>Chat apps and quick previews</td></tr>
<tr><td>Standard (150 DPI)</td><td>1240 × 1754 px</td><td>Uploads, slides and most uses</td></tr>
<tr><td>High (300 DPI)</td><td>2480 × 3508 px</td><td>Printing and zooming into small text</td></tr>
</table>
<h2>Common uses</h2>
<ul>
<li>Uploading a document to a form that accepts only JPG.</li>
<li>Posting a page of a report or menu on social media.</li>
<li>Inserting a PDF page into a presentation as an image.</li>
</ul>
<h2>Tips</h2>
<ul>
<li>If the JPG must be under a size limit, compress it afterwards with the <a href="/compress-image">image compressor</a>.</li>
<li>Convert only the pages you need by typing them in the Pages box, for example 2 or 1-3.</li>
<li>Password-protected PDFs must be unlocked first.</li>
</ul>
""",

"heic-to-pdf": """
<h2>Tips for a clean multi-page PDF</h2>
<ul>
<li>Crop each photo to the document's edges in the iPhone Photos app before adding it; backgrounds make the PDF larger.</li>
<li>Choose Automatic orientation if you mix portrait and landscape pages.</li>
<li>Pick A4 for documents used in India, the UK and Europe, and US Letter for the USA and Canada.</li>
</ul>
<h2>Typical sizes</h2>
<table>
<tr><th>Pages</th><th>Approximate PDF size</th></tr>
<tr><td>1 photo</td><td>0.5 to 1.5 MB</td></tr>
<tr><td>5 photos</td><td>3 to 7 MB</td></tr>
<tr><td>10 photos</td><td>6 to 14 MB</td></tr>
</table>
<p>If the portal has a smaller limit, compress the result with <a href="/compress-pdf">compress PDF</a>.</p>
""",

"compress-pdf-to-100kb": """
<h2>What fits in 100 KB</h2>
<table>
<tr><th>Document</th><th>Usually fits?</th></tr>
<tr><td>1-page certificate, black and white</td><td>Yes, clearly readable</td></tr>
<tr><td>1-page colour certificate with seals</td><td>Yes, slightly softer</td></tr>
<tr><td>2 to 3 pages, black and white</td><td>Usually, with small text still readable</td></tr>
<tr><td>5 or more pages</td><td>Often too small to stay readable</td></tr>
</table>
<h2>Step by step for a scanned mark sheet</h2>
<ol>
<li>Photograph or scan the mark sheet flat and crop to the paper.</li>
<li>Create the PDF with <a href="/jpg-to-pdf">JPG to PDF</a>, choosing A4 and no margin.</li>
<li>Compress it here with Black and white turned on.</li>
<li>Open the result and zoom into the roll number and marks to check they are readable.</li>
</ol>
""",


"jxl-to-jpg": """
<h2>Which apps open JPEG XL</h2>
<table>
<tr><th>Where</th><th>Opens .jxl?</th></tr>
<tr><td>Google Chrome 155 or newer</td><td>Yes, since October 2026</td></tr>
<tr><td>Safari 17 or newer (Mac, iPhone, iPad)</td><td>Yes</td></tr>
<tr><td>Microsoft Edge</td><td>Not by default at the time of writing</td></tr>
<tr><td>Windows 11 Photos</td><td>Only after installing the free JPEG XL Image Extension from the Microsoft Store</td></tr>
<tr><td>Windows 10, most Android galleries, older office software</td><td>Usually no</td></tr>
</table>
<p>Even where you can view a .jxl image, websites, upload forms, email recipients and print shops may still reject it. Converting to JPG avoids all of these problems.</p>
<h2>Choosing the quality</h2>
<table>
<tr><th>Use</th><th>Suggested quality</th></tr>
<tr><td>Printing or editing</td><td>95 to 100%</td></tr>
<tr><td>Sharing, email and documents</td><td>85 to 90%</td></tr>
<tr><td>Websites and chat apps</td><td>75 to 80%</td></tr>
</table>
<p>If an upload form has a size limit, convert at 90% first and then use the <a href="/compress-image">image compressor</a> to reach the exact size.</p>
<h2>Troubleshooting</h2>
<ul>
<li><strong>The first file takes a few seconds:</strong> in browsers without built-in JPEG XL support the page downloads a small decoder once. Later files are quicker.</li>
<li><strong>Transparent areas turned white:</strong> JPG has no transparency. Use <a href="/jxl-to-png">JXL to PNG</a> to keep it.</li>
<li><strong>The file still will not open:</strong> check that it really is a .jxl image. Files saved from websites are sometimes WebP or AVIF; this page converts those too.</li>
</ul>
""",

"jxl-to-png": """
<h2>JPEG XL, PNG, JPG and WebP compared</h2>
<table>
<tr><th>Format</th><th>Transparency</th><th>Lossless</th><th>Opens almost everywhere</th></tr>
<tr><td>JPEG XL</td><td>Yes</td><td>Yes</td><td>Not yet</td></tr>
<tr><td>PNG</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
<tr><td>JPG</td><td>No</td><td>No</td><td>Yes</td></tr>
<tr><td>WebP</td><td>Yes</td><td>Yes</td><td>Most current apps</td></tr>
</table>
<h2>Troubleshooting</h2>
<ul>
<li><strong>The PNG is very large:</strong> this is expected. For websites, <a href="/png-to-webp">PNG to WebP</a> makes it small again while keeping transparency.</li>
<li><strong>Colours look slightly different:</strong> some JPEG XL images use wide-gamut or HDR colour. PNG saved by a browser uses standard colour, so very bright highlights may look calmer.</li>
<li><strong>The first file is slow in Edge:</strong> the page loads a decoder once for browsers without built-in JPEG XL support.</li>
</ul>
""",

"open-jxl-file": """
<h2>Open JPEG XL on each device</h2>
<ul>
<li><strong>Windows 11:</strong> install the free JPEG XL Image Extension from the Microsoft Store to see .jxl files in Photos and File Explorer, or drag the file into Google Chrome 155 or newer.</li>
<li><strong>Windows 10:</strong> there is no built-in support. Open the file in an up-to-date Google Chrome, or convert it above.</li>
<li><strong>Microsoft Edge:</strong> Edge did not show JPEG XL by default at the time of writing. Use Chrome or the converter on this page.</li>
<li><strong>Mac, iPhone and iPad:</strong> Preview, Photos and Safari open .jxl on macOS 14 and iOS 17 or newer.</li>
<li><strong>Android:</strong> most gallery apps cannot open .jxl yet. Open this page in Chrome on your phone and convert the file here.</li>
</ul>
<h2>Why JPEG XL appeared suddenly</h2>
<p>Google Chrome began showing JPEG XL images by default in October 2026. Because Chrome is the most used browser, image services can now send .jxl pictures to many more people, so saved images, downloads and attachments increasingly arrive as .jxl. Support in other apps is catching up one program at a time.</p>
<h2>Should you keep the .jxl file?</h2>
<p>Yes, if your devices open it: JPEG XL files are smaller and keep excellent quality. Convert a copy to JPG when you need to share, upload, print or edit the image in software that does not support the format yet. For images with transparent backgrounds, use <a href="/jxl-to-png">JXL to PNG</a>.</p>
""",

}
