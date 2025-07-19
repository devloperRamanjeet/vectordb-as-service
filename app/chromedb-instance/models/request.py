from pydantic import BaseModel
from typing import List

class EmbedRequest(BaseModel):
    documents: List[str]

class SearchRequest(BaseModel):
    query: str
    top_k: int = 5

class DeleteRequest(BaseModel):
    vector_ids: List[str]
