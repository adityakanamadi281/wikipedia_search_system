from elasticsearch import Elasticsearch
es = Elasticsearch("http://localhost:9200")

def keyword_search(query, index_name="wikipedia", top_k=5):
    response = es.search(
        index=index_name,
        query={"match": {"content": query}},
        size=top_k
    )
    results = [{"title": hit["_source"]["title"], "content": hit["_source"]["content"]} 
               for hit in response['hits']['hits']]
    return results
