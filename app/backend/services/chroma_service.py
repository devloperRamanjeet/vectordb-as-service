def embed_documents(documents):
    return [f"doc_{i}" for i in range(len(documents))]

def search_vectors(query, top_k):
    return [{"doc_id": f"doc_{i}", "score": 0.95 - i * 0.01} for i in range(top_k)]

def delete_vectors(vector_ids):
    return {"deleted_count": len(vector_ids)}
