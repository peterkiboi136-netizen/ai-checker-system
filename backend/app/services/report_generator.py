from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from reportlab.lib.pagesizes import letter

import os


def generate_reports(
    filename,
    analysis,
    extracted_text
):

    reports_dir = "app/generated_reports"

    os.makedirs(
        reports_dir,
        exist_ok=True
    )

    styles = getSampleStyleSheet()

    # =========================
    # AI REPORT
    # =========================

    ai_report_path = os.path.join(
        reports_dir,
        f"{filename}_ai_report.pdf"
    )

    ai_doc = SimpleDocTemplate(
        ai_report_path,
        pagesize=letter
    )

    ai_content = []

    ai_content.append(
        Paragraph(
            "<b>AI Detection Report</b>",
            styles["Title"]
        )
    )

    ai_content.append(
        Spacer(1, 20)
    )

    ai_content.append(
        Paragraph(
            f"<b>Filename:</b> {filename}",
            styles["BodyText"]
        )
    )

    ai_content.append(
        Paragraph(
            f"<b>AI Score:</b> {analysis['ai_score']}%",
            styles["BodyText"]
        )
    )

    ai_content.append(
        Paragraph(
            f"<b>Risk Level:</b> {analysis['risk_level']}",
            styles["BodyText"]
        )
    )

    ai_content.append(
        Paragraph(
            f"<b>Word Count:</b> {analysis['word_count']}",
            styles["BodyText"]
        )
    )

    ai_content.append(
        Paragraph(
            f"<b>Sentence Count:</b> {analysis['sentence_count']}",
            styles["BodyText"]
        )
    )

    ai_doc.build(ai_content)

    # =========================
    # SIMILARITY REPORT
    # =========================

    similarity_report_path = os.path.join(
        reports_dir,
        f"{filename}_similarity_report.pdf"
    )

    similarity_doc = SimpleDocTemplate(
        similarity_report_path,
        pagesize=letter
    )

    similarity_content = []

    similarity_content.append(
        Paragraph(
            "<b>Similarity Report</b>",
            styles["Title"]
        )
    )

    similarity_content.append(
        Spacer(1, 20)
    )

    similarity_content.append(
        Paragraph(
            f"<b>Filename:</b> {filename}",
            styles["BodyText"]
        )
    )

    # FAKE similarity score for now
    similarity_score = 18

    similarity_content.append(
        Paragraph(
            f"<b>Similarity Score:</b> {similarity_score}%",
            styles["BodyText"]
        )
    )

    preview = extracted_text[:2000]

    similarity_content.append(
        Spacer(1, 20)
    )

    similarity_content.append(
        Paragraph(
            f"<b>Text Preview:</b><br/>{preview}",
            styles["BodyText"]
        )
    )

    similarity_doc.build(similarity_content)

    return {
        "ai_report": ai_report_path,
        "similarity_report": similarity_report_path
    }