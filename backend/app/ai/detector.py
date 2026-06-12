from app.pdf.word_extractor import extract_words_with_positions

def map_matches_to_words(pdf_path, matches):
    """
    Convert AI matches → exact word positions
    """

    pages = extract_words_with_positions(pdf_path)

    highlights = []

    for page in pages:
        for word in page["words"]:
            for match in matches:

                if match["text"].lower() in word["text"].lower():
                    highlights.append({
                        "page": page["page"],
                        "text": word["text"],
                        "x": word["x"],
                        "y": word["y"],
                        "width": word["width"],
                        "height": word["height"],
                        "severity": match.get("severity", "low")
                    })

    return highlights