import requests
import os
import sys

API_KEY = os.getenv("NEWS_API_KEY")
BASE_URL = "https://newsapi.org/v2/top-headlines"

def get_headlines(country="us"):
    params = {
        "apiKey": API_KEY,
        "country": country,
        "pageSize": 5,
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        for i, article in enumerate(articles, start=1):
            print(f"{i}. {article['title']}")
    else:
        print(f"Failed to fetch news: {response.status_code}, {response.text}")

if __name__ == "__main__":
    country = sys.argv[1] if len(sys.argv) > 1 else "us"
    get_headlines(country)

### script 
