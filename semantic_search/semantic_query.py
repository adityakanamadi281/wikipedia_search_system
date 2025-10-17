import faiss
import pickle
from utils.embedding_utils import embed_text

index_file = "semantic_search/faiss_index.pkl"
articles_file = "semantic_search/articles.pkl"

# Load index and articles
index = faiss.read_index(index_file)
with open(articles_file, "rb") as f:
    articles = pickle.load(f)

def semantic_search(query, top_k=5):
    query_vec = embed_text([query])
    D, I = index.search(query_vec, top_k)
    results = [articles[i] for i in I[0]]
    return results
