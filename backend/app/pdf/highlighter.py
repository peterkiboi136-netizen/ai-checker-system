import fitz  # PyMuPDF


# ----------------------------------------
# COLOR RULES
# ----------------------------------------
def get_color(score):

    if score >= 80:
        return (1, 0, 0)      # red
    elif score >= 50:
        return (1, 0.6, 0)    # orange
    else:
        return (1, 1, 0)      # yellow


# ----------------------------------------
# MAIN HIGHLIGHT FUNCTION
# ----------------------------------------
def highlight_pdf(input_pdf_path, matches, output_pdf_path):

    doc = fitz.open(input_pdf_path)

    for page in doc:

        for match in matches:

            sentence = match.get("sentence", "")
            score = match.get("similarity", 0)

            if not sentence:
                continue

            color = get_color(score)

            areas = page.search_for(sentence)

            for area in areas:

                annot = page.add_highlight_annot(area)
                annot.set_colors(stroke=color)
                annot.update()

    doc.save(output_pdf_path)
    doc.close()

    return output_pdf_path