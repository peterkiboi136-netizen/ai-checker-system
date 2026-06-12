import math
import re
from transformers import pipeline

# ----------------------------
# Lightweight transformer model (stable)
# ----------------------------
classifier = pipeline(
    "text-classification",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)


# ----------------------------
# BASIC TEXT CLEANING
# ----------------------------
def clean_text(text: str) -> str:
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text


# ----------------------------
# SENTENCE SPLIT
# ----------------------------
def split_sentences(text: str):
    return [s.strip() for s in re.split(r"[.!?]", text) if len(s.strip()) > 5]


# ----------------------------
# PERPLEXITY APPROXIMATION
# (lower = more human-like randomness)
# ----------------------------
def fake_perplexity(text: str) -> float:
    words = text.split()
    if len(words) < 5:
        return 10.0

    unique_words = len(set(words))
    total_words = len(words)

    diversity = unique_words / total_words

    # lower diversity = more AI-like
    return max(1.0, min(20.0, 20 * (1 - diversity)))


# ----------------------------
# BURSTINESS SCORE
# (AI tends to have uniform sentence lengths)
# ----------------------------
def burstiness(sentences):
    if len(sentences) < 2:
        return 0

    lengths = [len(s.split()) for s in sentences]
    avg = sum(lengths) / len(lengths)

    variance = sum((l - avg) ** 2 for l in lengths) / len(lengths)

    return math.sqrt(variance)


# ----------------------------
# TRANSFORMER SIGNAL
# ----------------------------
def transformer_score(text: str) -> float:
    try:
        result = classifier(text[:512])[0]

        label = result["label"].lower()
        score = result["score"]

        if "negative" in label:
            return score * 100 * 0.7
        else:
            return score * 100 * 0.3

    except Exception:
        return 50


# ----------------------------
# FINAL ENSEMBLE DETECTOR
# ----------------------------
def detect_ai_text(text: str) -> float:

    text = clean_text(text)

    if not text:
        return 0

    sentences = split_sentences(text)

    # components
    t_score = transformer_score(text)
    p_score = fake_perplexity(text) * 5
    b_score = min(100, burstiness(sentences) * 10)

    # weighted ensemble
    ai_score = (
        0.5 * t_score +
        0.3 * p_score +
        0.2 * b_score
    )

    # normalize
    ai_score = max(5, min(95, ai_score))

    return round(ai_score, 2)