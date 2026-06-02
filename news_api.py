import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")


def get_news(category=None):

    query_map = {
        "business": "business",
        "technology": "technology",
        "sports": "sports",
        None: "breaking news"
    }

    query = query_map.get(category, "breaking news")

    url = (
        f"https://newsapi.org/v2/everything"
        f"?q={query}"
        f"&language=en"
        f"&sortBy=publishedAt"
        f"&pageSize=20"
        f"&apiKey={API_KEY}"
    )

    response = requests.get(url)

    data = response.json()

    return data.get("articles", [])