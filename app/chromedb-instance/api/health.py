from fastapi import APIRouter
from models.response import HealthResponse
from core.config import TENANT_ID, PLAN, MODEL_NAME, DIMENSION
from core.chroma import VECTOR_STORE

router = APIRouter()

@router.get("/", response_model=HealthResponse)
def health():
    return HealthResponse(
        tenant_id=TENANT_ID,
        plan=PLAN,
        model_name=MODEL_NAME,
        dimension=DIMENSION,
        document_count=len(VECTOR_STORE)
    )
