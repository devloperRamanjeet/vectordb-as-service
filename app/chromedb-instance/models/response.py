from pydantic import BaseModel
from typing import List, Dict

class EmbedResponse(BaseModel):
    embedded_ids: List[str]

class SearchResponse(BaseModel):
    matches: List[Dict[str, float]]

class DeleteResponse(BaseModel):
    deleted_count: int

class HealthResponse(BaseModel):
    tenant_id: str
    plan: str
    model_name: str
    dimension: int
    document_count: int
