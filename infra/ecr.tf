resource "aws_ecr_repository" "orchestration_backend" {
  name                 = "${var.app_name}-backend"
  image_tag_mutability = "MUTABLE"
  force_delete         = true

  tags = {
    Name        = "${var.app_name}-backend-ecr"
    Environment = "dev"
  }
}

resource "aws_ecr_repository" "orchestration_worker" {
  name                 = "${var.app_name}-worker"
  image_tag_mutability = "MUTABLE"
  force_delete         = true

  tags = {
    Name        = "${var.app_name}-worker-ecr"
    Environment = "dev"
  }
}
