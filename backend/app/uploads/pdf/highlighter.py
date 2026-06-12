import fitz  # PyMuPDF
import os
import uuid


def highlight_pdf(input_pdf_path: str, matches: list, output_pdf_path: str = None):
    """
    Turnitin-style PDF highlighter using PyMuPDF.

    Args:
        input_pdf_path: original PDF
        matches: list of dicts:
            {
                "text": str,
                "score": float (0-1)
            }
        output_pdf_path: optional output path

    Returns:
        output_pdf_path
    """

    if output_pdf_path is None:
        output_pdf_path = f"highlighted_{uuid.uuid4().hex}.pdf"

    doc = fitz.open(input_pdf_path)

    for page in doc:
        for match in matches:
            text = match.get("text", "")
            score = match.get("score", 0)

            if not text:
                continue

            # Choose color based on plagiarism score
            if score >= 0.8:
                color = (1, 0, 0)  # red (high risk)
            elif score >= 0.5:
                color = (1, 0.6, 0)  # orange
            else:
                color = (1, 1, 0)  # yellow

            # Search text in page
            areas = page.search_for(text)

            for area in areas:
                highlight = page.add_highlight_annot(area)
                highlight.set_colors(stroke=color)
                highlight.update()

    doc.save(output_pdf_path)
    doc.close()

    return output_pdf_path