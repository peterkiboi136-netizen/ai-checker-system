import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from dataset import human_texts, ai_texts

# -------------------------
# COMBINE DATA
# -------------------------
texts = human_texts + ai_texts
labels = [0] * len(human_texts) + [1] * len(ai_texts)

# -------------------------
# FEATURE EXTRACTION
# -------------------------
vectorizer = TfidfVectorizer(ngram_range=(1, 2))
X = vectorizer.fit_transform(texts)

# -------------------------
# MODEL TRAINING
# -------------------------
model = LogisticRegression()
model.fit(X, labels)

# -------------------------
# SAVE MODEL
# -------------------------
joblib.dump(model, "ai_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Custom AI model trained successfully!")