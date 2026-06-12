from app.pdf.utils import extract_text
from app.pdf.highlighter import highlight_pdf
from app.services.detector_service import run_full_detection


def process_pdf(input_path: str, output_path: str):
    text = extract_text(input_path)

    result = run_full_detection(text)

    highlighted_pdf = highlight_pdf(
        input_pdf_path=input_path,
        matches=result["matches"],
        output_pdf_path=output_path
    )

    return {
        "ai_score": result["ai_score"],
        "matches": result["matches"],
        "highlighted_pdf": highlighted_pdf
    }