import joblib
import os

MODEL_PATH = os.path.join("app", "ai", "ai_model.pkl")

model = joblib.load(MODEL_PATH)


def predict_ai_probability(text: str) -> float:
    try:
        proba = model.predict_proba([text])[0][1]
        return round(proba * 100, 2)
    except Exception:
        return 0