## 🚀 chromedb-instance

This is the containerized FastAPI application that runs **per tenant** as part of your VectorDB-as-a-Service platform. It exposes RESTful endpoints for vector operations powered by ChromaDB, and uses environment variables for tenant-level configuration injected by ECS.

---

### 🧩 Key Features

- 🧠 Embedding, searching, and deleting vectors via ChromaDB interface
- 📡 Containerized via Docker and deployable through ECS tasks
- 🔐 Tenant-specific config through environment variables
- 🌐 Clean REST API with automatic FastAPI docs (`/docs`)
- ✅ Unit-testable and modular app layout

---

### 📁 Folder Structure

```
chromedb-instance/
├── main.py                  # FastAPI app entrypoint
├── api/                     # API route handlers
├── core/                    # Business logic and ENV config
├── models/                  # Pydantic request/response schemas
├── tests/                   # Unit tests
├── requirements.txt         # Python dependencies
├── Dockerfile               # Container build config
└── .env.example             # Example env vars for local run
```

---

### ⚙️ Environment Variables (injected via ECS)

| Variable      | Description                         | Default                      |
|---------------|--------------------------------------|------------------------------|
| `TENANT_ID`    | Unique tenant identifier             | `"default"`                  |
| `PLAN`         | Subscription tier                   | `"starter"`                  |
| `MODEL_NAME`   | Embedding model for ChromaDB         | `"all-MiniLM-L6-v2"`         |
| `DIMENSION`    | Vector dimension                     | `"384"`                      |
| `MAX_DOCS`     | Optional doc quota                   | `"100000"`                   |

These are loaded from `core/config.py` and used to scope vector operations and metadata.

---

### 📦 Installation

```bash
cd chromedb-instance
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Create `.env` file based on `.env.example` for local testing.

---

### 🚀 Run Locally

```bash
uvicorn main:app --reload
```

Then visit [http://localhost:8000/docs](http://localhost:8000/docs) for interactive API documentation.

---

### 📬 API Endpoints

| Method | Endpoint       | Description                       |
|--------|----------------|-----------------------------------|
| POST   | `/embed/`      | Add new documents to store        |
| POST   | `/search/`     | Perform semantic vector search    |
| POST   | `/delete/`     | Delete vectors by ID              |
| GET    | `/healthz/`    | Show ENV config + instance status |

---

### 🧪 Testing

```bash
pytest tests/
```

Includes sample unit test for `/healthz`.

---

### 🐳 Docker Build & Push

```bash
docker build -t vector-chroma-instance .
docker tag vector-chroma-instance:latest <ECR_URL>:v1.0.0
docker push <ECR_URL>:v1.0.0
```

This image will be referenced by your ECS launch logic per tenant.

---

### 💡 Usage in SaaS Platform

Once launched by ECS with injected environment variables, each tenant gets their own ChromaDB API instance scoped by:

- Their unique `TENANT_ID`
- Dedicated memory + runtime container
- Configured embedding model + plan limits

Your main backend returns this container's URL to clients so they can hit the `/embed`, `/search`, and `/delete` endpoints directly.

---
