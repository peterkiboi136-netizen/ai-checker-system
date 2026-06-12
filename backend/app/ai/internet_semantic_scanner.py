import requests


# ----------------------------------------
# INTERNET SEMANTIC PLAGIARISM SCANNER
# ----------------------------------------
def internet_semantic_scan(text: str):

    try:

        # NOTE:
        # Real production version would use:
        # - Google Custom Search API
        # - SerpAPI
        # - Bing API
        # - vector embedding comparison

        # For now we simulate a real scan result safely

        keywords = text.split()[:5]

        results = []

        for word in keywords:

            results.append({
                "source": "internet_match",
                "matched_text": word,
                "similarity": 0.72
            })

        return results

    except Exception as e:

        return [{
            "source": "error",
            "message": str(e)
        }]
        
        import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def fetch_web_text(query: str):
    url = f"https://html.duckduckgo.com/html/?q={query}"
    res = requests.get(url, timeout=10)
    soup = BeautifulSoup(res.text, "html.parser")
    return soup.get_text()


def internet_semantic_scan(text: str):
    web_text = fetch_web_text(text[:100])

    docs = [text, web_text]

    vectorizer = TfidfVectorizer().fit_transform(docs)
    vectors = vectorizer.toarray()

    score = cosine_similarity([vectors[0]], [vectors[1]])[0][0]

    return {
        "internet_similarity": float(score),
        "source": "duckduckgo_scrape"
    }