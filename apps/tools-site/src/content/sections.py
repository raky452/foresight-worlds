"""Sections group pages in navigation, the home directory and the footer.
A section only appears publicly when it has at least one live page, so new
sections can be prepared here without showing up on the site.
Give each new section an accent colour in src/styles/tokens.css ([data-section=id]).
"""
SECTIONS = [
    dict(id="image", name="Image tools", nav="Image tools",
         desc="Convert phone photos, change formats and shrink images to an exact size.", order=10),
    dict(id="pdf", name="PDF tools", nav="PDF tools",
         desc="Merge, split, rotate, compress and convert PDFs without uploading them.", order=20),
    dict(id="forms", name="Exam and form uploads", nav="Exam and form uploads",
         desc="Get photos and signatures accepted by online application forms the first time.", order=30),
]
