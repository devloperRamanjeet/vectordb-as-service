locals {
  container_image = "${aws_ecr_repository.app_repo.repository_url}:latest"
}

resource "aws_ecs_task_definition" "app" {
  family                   = var.task_family
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  cpu                      = var.cpu
  memory                   = var.memory
  execution_role_arn       = aws_iam_role.ecs_task_execution.arn
    runtime_platform {
    operating_system_family = "LINUX"
    cpu_architecture        = "ARM64" #"X86_64" # or "ARM64"
  }
  container_definitions = jsonencode([
    {
      name      = "sample-container",
      image     = local.container_image,
      essential = true,
      portMappings = [{ containerPort = var.container_port }],
            environment = [
        { name = "TENANT_ID",       value = "acme" },
        { name = "MODEL_NAME",      value = "all-MiniLM-L6-v2" },
        { name = "DIMENSION",       value = "384" },
        { name = "EMBEDDING_MODE",  value = "auto" },
        { name = "MAX_DOCS",        value = "100000" }
      ]
    }
  ])
}
