from transformers import pipeline

# lightweight pretrained detector (no training needed yet)
ai_detector = pipeline(
    "text-classification",
    model="roberta-base-openai-detector"
)


def predict_ai_probability(text: str):

    # truncate long text safely
    text = text[:2000]

    result = ai_detector(text)[0]

    label = result["label"]
    score = result["score"]

    # convert to AI probability
    if "AI" in label.upper():
        return round(score * 100, 2)
    else:
        return round((1 - score) * 100, 2)