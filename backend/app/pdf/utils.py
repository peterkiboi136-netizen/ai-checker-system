import fitz


def extract_text(pdf_path: str):
    """
    Extract full text from PDF using PyMuPDF
    """
    doc = fitz.open(pdf_path)
    text = ""

    for page in doc:
        text += page.get_text()

    doc.close()

    return text