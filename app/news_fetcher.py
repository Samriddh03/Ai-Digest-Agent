import requests
from app.config import NEWS_API_KEY

BASE_URL = "https://newsapi.org/v2/everything"

def fetch_ai_news():
    params = {
        "q": "(AI OR artificial intelligence OR machine learning OR OpenAI OR LLM)",
        "sortBy": "publishedAt",
        "language": "en",
        "pageSize": 10,
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()
    articles = data.get("articles", [])

    filtered = []

    for article in articles:
        text = (article.get("title", "") + str(article.get("description", ""))).lower()
        
        if any(keyword in text for keyword in ["ai", "artificial intelligence", "machine learning", "openai", "llm"]):
            filtered.append(article)

    return filtered[:5]