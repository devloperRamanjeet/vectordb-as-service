locals {
  backend_image = "${aws_ecr_repository.orchestration_backend.repository_url}:latest"
}

resource "aws_ecs_task_definition" "backend" {
  family                   = "${var.app_name}-backend"
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  cpu                      = var.cpu
  memory                   = var.memory
  execution_role_arn       = aws_iam_role.ecs_task_execution.arn

  runtime_platform {
    operating_system_family = "LINUX"
    cpu_architecture        = "ARM64" # or "X86_64"
  }

  container_definitions = jsonencode([
    {
      name      = "orchestration-backend"
      image     = local.backend_image
      essential = true
      portMappings = [
        { containerPort = var.container_port }
      ]
      environment = [
        { name = "ENV",         value = "dev" },
        { name = "SERVICE",     value = "orchestration-backend" },
        { name = "LOG_LEVEL",   value = "INFO" }
      ]
    }
  ])
}
