import os

TENANT_ID = os.getenv("TENANT_ID", "default")
MODEL_NAME = os.getenv("MODEL_NAME", "all-MiniLM-L6-v2")
DIMENSION = int(os.getenv("DIMENSION", "384"))
EMBEDDING_MODE = os.getenv("EMBEDDING_MODE", "auto")
MAX_DOCS = int(os.getenv("MAX_DOCS", "100000"))

PERSIST_PATH = f"./db/{TENANT_ID}"
COLLECTION_NAME = "tenant-vectors"
