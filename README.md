# VectorDB-as-a-Service 🧠

A scalable, multi-tenant vector search platform for generative AI applications—built using React Native, Flask, ChromaDB, AKS, and AWS.

## 🚀 Tech Stack
- Frontend: React Native
- Backend: Flask (includes SaaS orchestration)
- Vector Engine: ChromaDB + Docker, deployed on AKS
- Infra: AWS EC2, DynamoDB, CloudWatch

## 🧱 Architecture
- Frontend & backend co-hosted on EC2
- Per-tenant vector container pods on ecs
- Usage tracking + SaaS plans (Starter, Pro, Enterprise)

## 🛠 Features
- Document upload + semantic search
- Tenant provisioning with scoped configs
- API key and token generation
- INR-based pricing with cost simulation

## 🌍 Community
This project is open-source. Contributions, feedback, and collaboration are welcome!

👉 💬 Join the conversation on [Discord](https://discord.gg/mTbE44sm) – we’d love to have you! 
📣 Follow build progress on [LinkedIn](https://www.linkedin.com/in/ramanjeet-singh-b769ba88/)


## 📂 Repo Structure
apps/ ── react-native-frontend 
      ── flask-backend 
      ── chromadb-instance


infra/ ── aws-ec2-setup 
       ── azure-aks-helm-chart


## 📃 License
Licensed under the MIT License.
