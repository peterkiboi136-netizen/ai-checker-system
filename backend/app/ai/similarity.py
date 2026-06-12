from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")


def compute_similarity(text_a, text_b):
    emb1 = model.encode(text_a, convert_to_tensor=True)
    emb2 = model.encode(text_b, convert_to_tensor=True)

    return float(util.pytorch_cos_sim(emb1, emb2)[0][0])


def find_matches(document_words, sources):
    matches = []

    for page in document_words:
        for w in page["words"]:
            for src in sources:

                score = compute_similarity(w["text"], src)

                if score > 0.75:
                    matches.append({
                        "text": w["text"],
                        "page": page["page"],
                        "score": score,
                        "severity": (
                            "high" if score > 0.9 else
                            "medium" if score > 0.8 else
                            "low"
                        ),
                        "bbox": w["bbox"]
                    })

    return matches