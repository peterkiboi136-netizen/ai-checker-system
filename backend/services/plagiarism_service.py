from app.pdf.extract import extract_document
from app.ai.similarity import find_matches


def analyze_pdf(pdf_path: str, sources: list):
    document = extract_document(pdf_path)

    matches = find_matches(document, sources)

    return {
        "document": document,
        "matches": matches,
        "ai_score": len(matches) / max(1, sum(len(p["words"]) for p in document))
    }