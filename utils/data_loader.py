import json

def load_wikipedia_articles(file_path="data/wikipedia_articles.json"):
    with open(file_path, "r", encoding="utf-8") as f:
        articles = json.load(f)
    return articles
