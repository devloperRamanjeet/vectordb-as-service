from flask import Blueprint, request, jsonify
from services.chroma_service import delete_vectors

delete_bp = Blueprint("delete", __name__)

@delete_bp.route("/delete", methods=["POST"])
def delete():
    data = request.get_json()
    deleted = delete_vectors(data["vector_ids"])
    return jsonify({"status": "success", **deleted})
