from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_report(data, filename):

    pdf_path = f"reports/{filename}.pdf"

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    content = []

    title = Paragraph(
        "AI Plagiarism Report",
        styles["Title"]
    )

    content.append(title)

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            f"Filename: {data['filename']}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Plagiarism Score: {data['similarity_score']}%",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"AI Score: {data['ai_score']}%",
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            "Matched Sentences:",
            styles["Heading2"]
        )
    )

    for sentence in data["matched_sentences"]:

        content.append(
            Paragraph(
                sentence,
                styles["BodyText"]
            )
        )

    doc.build(content)

    return pdf_path