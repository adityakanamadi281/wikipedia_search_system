import faiss
import numpy as np
from utils.data_loader import load_wikipedia_articles
from utils.embedding_utils import embed_text
import pickle

index_file = "semantic_search/faiss_index.pkl"
articles_file = "semantic_search/articles.pkl"

def build_vector_index():
    articles = load_wikipedia_articles()
    corpus = [a["content"] for a in articles]
    embeddings = embed_text(corpus)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    # Save index and articles
    faiss.write_index(index, index_file)
    with open(articles_file, "wb") as f:
        pickle.dump(articles, f)
    print("Vector index created!")

if __name__ == "__main__":
    build_vector_index()
