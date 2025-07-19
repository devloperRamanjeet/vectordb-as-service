import os

TENANT_ID = os.getenv("TENANT_ID", "default")
PLAN = os.getenv("PLAN", "starter")
MODEL_NAME = os.getenv("MODEL_NAME", "all-MiniLM-L6-v2")
DIMENSION = int(os.getenv("DIMENSION", "384"))
MAX_DOCS = int(os.getenv("MAX_DOCS", "100000"))
