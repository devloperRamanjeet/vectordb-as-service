from pydantic import BaseModel
from typing import List

class MatchItem(BaseModel):
    id: str
    score: float

class SearchResponse(BaseModel):
    matches: List[MatchItem]

class EmbedResponse(BaseModel):
    embedded_ids: List[str]

class DeleteResponse(BaseModel):
    deleted_count: int

class HealthResponse(BaseModel):
    tenant_id: str
    model_name: str
    dimension: int
    document_count: int
    max_docs: int

    model_config = { "protected_namespaces": () }
