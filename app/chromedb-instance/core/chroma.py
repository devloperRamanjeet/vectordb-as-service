from core.config import TENANT_ID
from typing import List

# Simulate tenant-local vector store
VECTOR_STORE = {}

def embed_documents(docs: List[str]) -> List[str]:
    ids = [f"{TENANT_ID}_doc_{i}" for i in range(len(docs))]
    for doc_id, content in zip(ids, docs):
        VECTOR_STORE[doc_id] = content
    return ids

def search_documents(query: str, top_k: int = 5):
    return [{"id": k, "score": 1.0} for k in list(VECTOR_STORE.keys())[:top_k]]

def delete_documents(ids: List[str]) -> int:
    deleted = 0
    for doc_id in ids:
        if doc_id in VECTOR_STORE:
            del VECTOR_STORE[doc_id]
            deleted += 1
    return deleted
