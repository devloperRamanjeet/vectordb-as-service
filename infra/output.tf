output "ecs_cluster_name" {
  description = "Name of the ECS cluster"
  value       = aws_ecs_cluster.main.name
}


output "task_definition_arn" {
  description = "ARN of the ECS task definition"
  value       = aws_ecs_task_definition.app.arn
}

output "security_group_id" {
  description = "Security group used by ECS tasks"
  value       = aws_security_group.ecs_sg.id
}

output "public_subnet_ids" {
  description = "Public subnet IDs used by ECS service"
  value       = [
    aws_subnet.public_subnet_1.id,
    aws_subnet.public_subnet_2.id
  ]
}

output "backend_ecr_url" {
  value = aws_ecr_repository.orchestration_backend.repository_url
}

output "worker_ecr_url" {
  value = aws_ecr_repository.orchestration_worker.repository_url
}

