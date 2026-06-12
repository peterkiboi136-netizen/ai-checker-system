import fitz  # PyMuPDF


def extract_words_with_positions(pdf_path: str):
    """
    Returns every word with exact coordinates (Turnitin-style foundation)
    """

    doc = fitz.open(pdf_path)

    all_pages = []

    for page_index, page in enumerate(doc, start=1):
        words = page.get_text("words")

        page_words = []

        for w in words:
            x0, y0, x1, y1, text, block, line, word_no = w

            page_words.append({
                "text": text,
                "x": x0,
                "y": y0,
                "width": x1 - x0,
                "height": y1 - y0,
                "page": page_index
            })

        all_pages.append({
            "page": page_index,
            "words": page_words
        })

    return all_pages