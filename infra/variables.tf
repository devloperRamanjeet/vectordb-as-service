variable "app_name" {
  default = "vectordb-app"
}

variable "aws_account_id" {
  default = "123456789012"
}

variable "region" {
  default = "ap-south-1"
}

variable "cpu" {
  default = "256"
}

variable "memory" {
  default = "512"
}

variable "container_port" {
  default = 80
}

variable "task_family" {
  default = "vectordb-task-family"
}
