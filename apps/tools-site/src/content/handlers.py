"""Which JS module provides each tool handler.
Adding a module: create src/scripts/<module>.js that calls TF.register({...}),
then map its handler names here. Pages load core.js plus only the modules they need.
"""
HANDLERS = {
    "convert": "image", "compress": "image", "resize": "image",
    "formphoto": "forms", "passport": "forms",
    "merge": "pdf", "split": "pdf", "rotate": "pdf",
    "img2pdf": "pdf", "pdf2img": "pdf", "compresspdf": "pdf", "croppdf": "pdf",
}
