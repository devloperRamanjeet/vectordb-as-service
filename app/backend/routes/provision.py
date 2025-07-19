from flask import Blueprint, request, jsonify
from services.tenant_service import provision_tenant

provision_bp = Blueprint("provision", __name__)

@provision_bp.route("/provision", methods=["POST"])
def provision():
    data = request.get_json()
    result = provision_tenant(data["tenant_id"], data["plan"])
    return jsonify({"status": "success", **result})
