from flask import Blueprint, request, jsonify
from services.chroma_service import search_vectors

search_bp = Blueprint("search", __name__)

@search_bp.route("/search", methods=["POST"])
def search():
    data = request.get_json()
    query = data["query"]
    top_k = data.get("top_k", 5)
    results = search_vectors(query, top_k)
    return jsonify({"status": "success", "matches": results})
