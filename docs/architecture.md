# 📐 Architecture Overview: VectorDB-as-a-Service

## 🔧 Core Components

- **React Native Frontend**: Document uploads, semantic search, token dashboard
- **Flask Backend**: Tenant provisioning, plan enforcement, API orchestration
- **Vector Engine**: ChromaDB + Docker, deployed on EC2 via ECR
- **AWS Services**:
  - EC2: Hosts frontend/backend
  - DynamoDB: Metadata + plan usage
  - S3: Optional backups & logs
  - CloudWatch: Logging & alerts

## 🧱 Infra Flow

1. Tenant signs up → Flask provisions config
2. Vector container pulled from ECR → launched on EC2
3. ENV injected (embedding model, metric type, plan limits)
4. `/embed`, `/search`, `/delete` APIs activated
5. Usage metered via backend → alerts & plan logic

## 🔐 Security

- Token-based access (`api_key`, `secret_token`)
- ENV-level tenant isolation
- IAM and role-scoped access control
