resource "aws_ecs_service" "backend_service" {
  name            = "${var.app_name}-backend-service"
  cluster         = aws_ecs_cluster.main.id
  task_definition = aws_ecs_task_definition.backend.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    subnets          = module.network.public_subnet_ids
    security_groups  = [module.network.ecs_security_group_id]
    assign_public_ip = true
  }

  deployment_controller {
    type = "ECS"
  }

  depends_on = [
    aws_iam_role_policy_attachment.ecs_execution_role_policy
  ]
}
