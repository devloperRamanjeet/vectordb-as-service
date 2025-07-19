from flask import Blueprint, request, jsonify
import boto3

delete_instance_bp = Blueprint("delete_instance", __name__)

@delete_instance_bp.route("/delete-instance", methods=["POST"])
def delete_instance():
    data = request.get_json()
    tenant_id = data.get("tenant_id")

    ecs = boto3.client("ecs")
    cluster = "your-ecs-cluster"

    # Find running tasks for tenant
    tasks = ecs.list_tasks(cluster=cluster, launchType="FARGATE")
    if not tasks["taskArns"]:
        return jsonify({"status": "error", "message": "No running task found"}), 404

    # Filter by tenant (you can enhance this with task tags)
    stopped = []
    for arn in tasks["taskArns"]:
        desc = ecs.describe_tasks(cluster=cluster, tasks=[arn])["tasks"][0]
        env_vars = desc["overrides"]["containerOverrides"][0].get("environment", [])
        match = any(var["name"] == "TENANT_ID" and var["value"] == tenant_id for var in env_vars)
        if match:
            ecs.stop_task(cluster=cluster, task=arn, reason="Tenant deletion requested")
            stopped.append(arn)

    return jsonify({
        "status": "terminated",
        "stopped_tasks": stopped,
        "tenant_id": tenant_id
    })
