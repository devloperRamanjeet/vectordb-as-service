# 🛠 Infra Deployment Guide

## ☁️ AWS Services Used

- EC2 (t3.large+) — App hosting
- ECR — ChromaDB vector image
- S3 — Optional storage
- DynamoDB — Tenant metadata
- CloudWatch — Logs and metrics

## 🔁 Deployment Steps

### EC2 Setup

1. Provision instance with NGINX, Gunicorn
2. Place frontend assets and backend routes
3. Secure with SSL (Let’s Encrypt)

### ECR Workflow

```bash
docker build -t vector-chroma .
docker tag vector-chroma <ecr-url>:v1
docker push <ecr-url>:v1
