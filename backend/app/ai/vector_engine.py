from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")


def embed(text: str):
    return model.encode([text])[0]


def vector_similarity_check(text1: str, text2: str) -> float:
    v1 = embed(text1)
    v2 = embed(text2)

    score = cosine_similarity([v1], [v2])[0][0]
    return float(score)