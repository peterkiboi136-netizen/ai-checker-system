import fitz

def extract_document(pdf_path: str):
    doc = fitz.open(pdf_path)

    pages = []

    for page_index, page in enumerate(doc, start=1):
        words = page.get_text("words")

        structured_words = []

        for w in words:
            x0, y0, x1, y1, text, block, line, word_no = w

            structured_words.append({
                "text": text,
                "bbox": [x0, y0, x1, y1],
                "page": page_index
            })

        pages.append({
            "page": page_index,
            "words": structured_words
        })

    return pages