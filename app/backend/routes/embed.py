from flask import Blueprint, request, jsonify
from services.chroma_service import embed_documents

embed_bp = Blueprint("embed", __name__)

@embed_bp.route("/embed", methods=["POST"])
def embed():
    data = request.get_json()
    docs = data.get("documents", [])
    result_ids = embed_documents(docs)
    return jsonify({
        "status": "success",
        "embedded_count": len(docs),
        "vector_ids": result_ids
    })
