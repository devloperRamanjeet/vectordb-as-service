from fastapi import APIRouter
from models.request import EmbedRequest
from models.response import EmbedResponse
from core.chroma import embed_documents

router = APIRouter()

@router.post("/", response_model=EmbedResponse)
def embed(req: EmbedRequest):
    ids = embed_documents(req.documents)
    return EmbedResponse(embedded_ids=ids)
