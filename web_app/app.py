from flask import Flask, request, render_template
from elasticsearch.es_search import keyword_search
from semantic_search.semantic_query import semantic_search

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def search():
    results = []
    if request.method == "POST":
        query = request.form["query"]
        mode = request.form.get("mode", "keyword")
        if mode == "semantic":
            results = semantic_search(query)
        else:
            results = keyword_search(query)
    return render_template("search.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
