import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

# ---------------- EMBEDDING SCORE ----------------
def embedding_score(text: str) -> float:
    sentences = [s.strip() for s in text.split(".") if s.strip()]

    if len(sentences) < 2:
        return 0

    embeddings = model.encode(sentences)
    sim_matrix = cosine_similarity(embeddings)

    total, count = 0, 0

    for i in range(len(sim_matrix)):
        for j in range(len(sim_matrix)):
            if i != j:
                total += sim_matrix[i][j]
                count += 1

    avg = total / count if count else 0
    return min(max(avg * 100, 0), 100)

# ---------------- LINGUISTIC SCORE ----------------
def linguistic_score(text: str) -> float:
    words = text.split()
    sentences = text.split(".")

    if len(words) == 0:
        return 0

    repetition = len(words) / max(len(set(words)), 1)

    lengths = [len(s.split()) for s in sentences if s.strip()]
    variance = np.var(lengths) if lengths else 0

    score = 0

    if repetition > 1.8:
        score += 30
    if variance < 10:
        score += 25

    return min(score, 100)

# ---------------- FINAL SCORE ----------------
def final_ai_score(text: str) -> dict:
    emb = embedding_score(text)
    ling = linguistic_score(text)

    final = (0.7 * emb) + (0.3 * ling)

    return {
        "embedding_score": round(emb, 2),
        "linguistic_score": round(ling, 2),
        "final_score": round(final, 2),
        "verdict": "Likely AI-generated" if final > 55 else "Likely Human-written"
    }