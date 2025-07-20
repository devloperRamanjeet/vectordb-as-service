from flask import Blueprint, request, jsonify
from services.ecs_manager import launch_instance, stop_instance
from models.container import Container, db

container_bp = Blueprint("containers", __name__)

@container_bp.route("/launch", methods=["POST"])
def launch_container():
    data = request.json
    user_id = data["user_id"]
    port = data.get("port", 8080)
    response = launch_instance(user_id, port)
    task_arn = response['tasks'][0]['taskArn']
    c = Container(user_id=user_id, task_arn=task_arn, port=port, status="running")
    db.session.add(c)
    db.session.commit()
    return jsonify({"task_arn": task_arn, "status": "launched"})

@container_bp.route("/stop/<int:user_id>", methods=["POST"])
def stop_container(user_id):
    container = Container.query.filter_by(user_id=user_id).first()
    stop_instance(container.task_arn)
    container.status = "stopped"
    db.session.commit()
    return jsonify({"message": "stopped"})
