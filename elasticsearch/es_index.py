from elasticsearch import Elasticsearch
from utils.data_loader import load_wikipedia_articles

es = Elasticsearch("http://localhost:9200")

def create_index(index_name="wikipedia"):
    es.indices.create(index=index_name, ignore=400)

def index_articles(index_name="wikipedia"):
    articles = load_wikipedia_articles()
    for i, article in enumerate(articles):
        es.index(index=index_name, id=i, document=article)
    print("Indexing complete!")

if __name__ == "__main__":
    create_index()
    index_articles()
