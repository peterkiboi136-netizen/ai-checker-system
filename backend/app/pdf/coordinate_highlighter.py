import fitz
import os

# ----------------------------------------
# HIGHLIGHT MATCHES
# ----------------------------------------
def highlight_pdf_coordinates(
    input_pdf,
    suspicious_chunks,
    output_pdf
):

    doc = fitz.open(input_pdf)

    total_highlights = 0

    for page_num in range(len(doc)):

        page = doc[page_num]

        for match in suspicious_chunks:

            text_to_find = match.get(
                "input_chunk",
                ""
            )

            if len(text_to_find) < 20:
                continue

            try:

                text_instances = page.search_for(
                    text_to_find[:100]
                )

                for inst in text_instances:

                    highlight = page.add_highlight_annot(
                        inst
                    )

                    highlight.update()

                    total_highlights += 1

            except Exception as e:

                print(
                    "Highlight error:",
                    e
                )

    os.makedirs(
        os.path.dirname(output_pdf),
        exist_ok=True
    )

    doc.save(output_pdf)

    doc.close()

    return {
        "output_pdf": output_pdf,
        "highlights": total_highlights
    }