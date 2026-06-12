from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from io import BytesIO


def generate_report_pdf(result: dict):
    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()
    content = []

    # TITLE
    content.append(Paragraph("Turnitin-Style Originality Report", styles["Title"]))
    content.append(Spacer(1, 12))

    # SCORE
    score = round(result["ai_score"] * 100, 2)
    content.append(
        Paragraph(f"<b>AI Similarity Score:</b> {score}%", styles["Normal"])
    )
    content.append(Spacer(1, 12))

    # SUMMARY
    summary = result.get("summary", {})

    content.append(Paragraph("<b>Match Breakdown:</b>", styles["Heading2"]))
    content.append(
        Paragraph(
            f"High: {summary.get('high', 0)} | "
            f"Medium: {summary.get('medium', 0)} | "
            f"Low: {summary.get('low', 0)}",
            styles["Normal"],
        )
    )

    content.append(Spacer(1, 12))

    # SOURCES
    content.append(Paragraph("<b>Sources:</b>", styles["Heading2"]))

    for src in result.get("sources", []):
        content.append(
            Paragraph(
                f"{src['name']} - {round(src['match'] * 100)}%",
                styles["Normal"],
            )
        )

    content.append(Spacer(1, 12))

    # MATCHED TEXT
    content.append(Paragraph("<b>Matched Phrases:</b>", styles["Heading2"]))

    for m in result.get("matches", [])[:20]:
        color = "red" if m["severity"] == "high" else "orange"
        content.append(
            Paragraph(
                f"<font color='{color}'>“{m['text']}”</font> (Page {m['page']})",
                styles["Normal"],
            )
        )

    doc.build(content)

    buffer.seek(0)
    return buffer