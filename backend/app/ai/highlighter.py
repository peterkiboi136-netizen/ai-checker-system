import re
from app.ai.detector import detect_ai_text


# ----------------------------------------
# SPLIT TEXT INTO SENTENCES
# ----------------------------------------
def split_sentences(text: str):
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    return [s.strip() for s in sentences if len(s.strip()) > 3]


# ----------------------------------------
# ASSIGN COLOR BASED ON SCORE
# ----------------------------------------
def get_color(score: float):
    if score <= 30:
        return "green"
    elif score <= 60:
        return "yellow"
    else:
        return "red"


# ----------------------------------------
# MAIN HIGHLIGHT ENGINE
# ----------------------------------------
def highlight_text(text: str):
    sentences = split_sentences(text)

    results = []

    for sentence in sentences:
        score = detect_ai_text(sentence)

        results.append({
            "sentence": sentence,
            "ai_score": score,
            "color": get_color(score)
        })

    return {
        "total_sentences": len(results),
        "highlights": results
    }