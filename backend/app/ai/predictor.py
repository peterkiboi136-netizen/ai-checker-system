import joblib

model = joblib.load("app/ai/ai_model.pkl")
vectorizer = joblib.load("app/ai/vectorizer.pkl")


def predict_ai_probability(text: str):

    X = vectorizer.transform([text])

    prob = model.predict_proba(X)[0][1]  # AI probability

    return round(prob * 100, 2)