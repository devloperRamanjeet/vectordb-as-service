from flask import Blueprint, request, jsonify
import boto3

launch_instance_bp = Blueprint("launch_instance", __name__)

@launch_instance_bp.route("/launch-instance", methods=["POST"])
def launch_instance():
    data = request.get_json()
    tenant_id = data.get("tenant_id")
    plan = data.get("plan", "starter")

    ecs = boto3.client("ecs")
    response = ecs.run_task(
        cluster="your-ecs-cluster",
        launchType="FARGATE",
        taskDefinition="vector-chroma-task",
        networkConfiguration={
            "awsvpcConfiguration": {
                "subnets": ["subnet-abc123"],
                "securityGroups": ["sg-xyz789"],
                "assignPublicIp": "ENABLED"
            }
        },
        overrides={
            "containerOverrides": [{
                "name": "vector-chroma-container",
                "environment": [
                    {"name": "TENANT_ID", "value": tenant_id},
                    {"name": "PLAN", "value": plan},
                    {"name": "MODEL_NAME", "value": "all-MiniLM-L6-v2"},
                    {"name": "DIMENSION", "value": "384"}
                ]
            }]
        }
    )

    task_arn = response["tasks"][0]["taskArn"]
    return jsonify({
        "status": "launched",
        "tenant_id": tenant_id,
        "task_arn": task_arn
    })
