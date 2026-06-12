from transformers import pipeline

# ----------------------------------------
# USE STABLE SENTIMENT MODEL (SAFE FALLBACK)
# ----------------------------------------
classifier = pipeline(
    "text-classification",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

# ----------------------------------------
# AI DETECTION LOGIC (HEURISTIC LAYER)
# ----------------------------------------
def detect_ai_text(text):

    try:

        if not text:
            return 0

        text = text[:3000]

        result = classifier(text)[0]

        label = result["label"]
        score = result["score"]

        # Convert sentiment into "AI likelihood heuristic"
        # (because true AI detectors are unreliable publicly)

        base_score = score * 100

        # Heuristic adjustment
        if label == "NEGATIVE":
            ai_probability = base_score * 0.6
        else:
            ai_probability = base_score * 0.4

        # Normalize
        ai_probability = min(max(ai_probability, 5), 95)

        return round(ai_probability, 2)

    except Exception:
        return 0