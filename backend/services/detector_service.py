from app.ai.transformer_detector import detect_ai_text
from app.ai.vector_engine import vector_similarity_check
from app.ai.internet_scanner import internet_scan


def run_full_detection(text: str):
    ai_score = detect_ai_text(text)
    vector_matches = vector_similarity_check(text)
    internet_matches = internet_scan(text)

    matches = []

    for m in vector_matches:
        matches.append({
            "text": m["text"],
            "score": m.get("score", 0.85),
            "source": "vector"
        })

    for m in internet_matches:
        matches.append({
            "text": m["text"],
            "score": m.get("score", 0.7),
            "source": "internet"
        })

    return {
        "ai_score": ai_score,
        "matches": matches
    }