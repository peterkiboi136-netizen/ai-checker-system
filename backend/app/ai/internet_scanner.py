def internet_scan(text: str):
    """
    Mock semantic internet plagiarism scan.
    Replace later with real scraping or search API.
    """

    keywords = text.lower().split()

    results = []

    for word in keywords:
        if len(word) > 6:
            results.append({
                "text": word,
                "score": 0.6
            })

    return results