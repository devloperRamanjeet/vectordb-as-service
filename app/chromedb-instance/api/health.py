from fastapi import APIRouter
from models.response import HealthResponse
from core.config import TENANT_ID, MODEL_NAME, DIMENSION, MAX_DOCS
from core.chroma import get_vector_count

router = APIRouter()

@router.get("/", response_model=HealthResponse)
def health():
    return HealthResponse(
        tenant_id=TENANT_ID,
        model_name=MODEL_NAME,
        dimension=DIMENSION,
        document_count=get_vector_count(),
        max_docs=MAX_DOCS
    )
