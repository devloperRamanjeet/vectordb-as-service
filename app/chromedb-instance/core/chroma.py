import chromadb
from chromadb.config import Settings
from core.config import PERSIST_PATH, COLLECTION_NAME

settings = Settings(
    is_persistent=True,
    persist_directory=PERSIST_PATH
)

client = chromadb.Client(settings)
collection = client.get_or_create_collection(name=COLLECTION_NAME)

def embed_documents(docs: list[str]) -> list[str]:
    ids = [f"doc_{i}" for i in range(len(docs))]
    collection.add(documents=docs, ids=ids)
    return ids

def search_documents(query: str, top_k: int = 5):
    results = collection.query(query_texts=[query], n_results=top_k)
    return [
        {"id": id_, "score": score}
        for id_, score in zip(results["ids"][0], results["distances"][0])
    ]

def delete_documents(ids: list[str]) -> int:
    collection.delete(ids=ids)
    return len(ids)

def get_vector_count() -> int:
    return len(collection.get()["ids"])
