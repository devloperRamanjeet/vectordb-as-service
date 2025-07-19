## 📦 Backend: VectorDB-as-a-Service

This is the Flask-based multi-tenant backend powering VectorDB-as-a-Service. It handles provisioning, token generation, container orchestration via ECS, and vector operations (embed/search/delete) for tenant-isolated ChromaDB instances.

---

### 🚀 Core Features

- 🔧 Launch & terminate ECS-backed ChromaDB containers per client
- 🔐 API key & JWT issuance for secure tenant auth
- 📁 Full vector operation suite: `/embed`, `/search`, `/delete`
- 🔒 Instance lifecycle management: `/launch-instance`, `/delete-instance`
- ✅ Mypy, Flake8, and Pytest integration for code quality
- ⚙️ DynamoDB integration for tenant metadata persistence

---

### 🗃 Folder Structure

```
backend/
├── app.py                    # Entrypoint and route registration
├── config/                   # ENV config loading
│   └── settings.py
├── routes/                   # Flask Blueprint routes
│   ├── embed.py
│   ├── search.py
│   ├── delete.py
│   ├── provision.py
│   ├── token.py
│   ├── launch_instance.py
│   └── delete_instance.py
├── services/                 # Business logic separation
│   ├── chroma_service.py
│   ├── tenant_service.py
│   └── token_service.py
├── utils/                    # Auth, Dynamo, secrets
│   ├── auth.py
│   ├── dynamo.py
│   └── secrets.py
├── models/                   # Request/Response typing (optional)
├── tests/                    # Unit tests per route
├── requirements.txt
└── .env.example
```

---

### 🧪 Dev Quality Checks

Run locally before committing:

```bash
mypy . --strict          # Type validation
flake8 .                 # Linting
pytest tests/            # Unit tests
```

Or use the bundled CI workflow for PRs.

---

### 🔁 GitHub Actions (CI)

Located in `.github/workflows/backend-check.yml`

- Triggered on pull requests to `main`
- Validates code with mypy, flake8, pytest
- Requires Python 3.10 environment

---

### ⚙️ Setup Instructions

1. Clone the repo and navigate to backend:

   ```bash
   cd app/backend
   ```

2. Install dependencies:

   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. Create `.env` file based on `.env.example`

4. Run the app locally:

   ```bash
   python app.py
   ```

---

### 📬 API Endpoints

| Method | Path                  | Description                        |
|--------|-----------------------|------------------------------------|
| POST   | `/provision`          | Create tenant metadata             |
| POST   | `/generate-token`     | Get token + API key bundle         |
| POST   | `/launch-instance`    | Start tenant container via ECS     |
| POST   | `/delete-instance`    | Stop tenant ECS container          |
| POST   | `/embed`              | Add documents to ChromaDB          |
| POST   | `/search`             | Semantic vector search             |
| POST   | `/delete`             | Delete vectors by ID               |

---
