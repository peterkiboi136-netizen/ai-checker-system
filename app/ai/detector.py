from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import docx
import PyPDF2


# -------------------------
# EXTRACT TEXT
# -------------------------
def extract_text(file_path):

    # PDF
    if file_path.endswith(".pdf"):

        text = ""

        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)

            for page in reader.pages:
                extracted = page.extract_text()

                if extracted:
                    text += extracted

        return text

    # DOCX
    elif file_path.endswith(".docx"):

        doc = docx.Document(file_path)

        return "\n".join([para.text for para in doc.paragraphs])

    # TXT
    else:

        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()


# -------------------------
# SIMILARITY CHECK
# -------------------------
def calculate_similarity(text1, text2):

    documents = [text1, text2]

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]

    return round(similarity * 100, 2)


# -------------------------
# MAIN AI SCANNER
# -------------------------
def check_plagiarism(file_path):

    uploaded_text = extract_text(file_path)

    # SAMPLE DATABASE
    database_texts = [
        "Artificial intelligence is transforming education.",
        "Machine learning improves automated systems.",
        "Turnitin compares documents for similarity detection."
    ]

    scores = []

    for db_text in database_texts:

        score = calculate_similarity(uploaded_text, db_text)

        scores.append(score)

    highest_score = max(scores) if scores else 0

    return {
        "similarity_score": highest_score,
        "all_scores": scores
    }