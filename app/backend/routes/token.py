from flask import Blueprint, request, jsonify, current_app
from services.token_service import create_token_bundle

token_bp = Blueprint("token", __name__)

@token_bp.route("/generate-token", methods=["POST"])
def generate_token():
    data = request.get_json()
    bundle = create_token_bundle(data["tenant_id"], data["plan"], current_app.config["TOKEN_SECRET"])
    return jsonify(bundle)
