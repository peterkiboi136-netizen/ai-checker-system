def analyze_text(text: str):
    words = text.split()
    word_count = len(words)

    sentence_count = len([s for s in text.split(".") if s.strip()])

    # simple AI detection logic
    ai_score = min(95, max(5, word_count // 10))

    if ai_score < 30:
        risk_level = "Low"
    elif ai_score < 70:
        risk_level = "Medium"
    else:
        risk_level = "High"

    return {
        "ai_score": ai_score,
        "risk_level": risk_level,
        "word_count": word_count,
        "sentence_count": sentence_count
    }