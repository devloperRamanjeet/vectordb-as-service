from fastapi import APIRouter
from models.request import SearchRequest
from models.response import SearchResponse
from core.chroma import search_documents

router = APIRouter()

@router.post("/", response_model=SearchResponse)
def search(req: SearchRequest):
    matches = search_documents(req.query, req.top_k)
    return SearchResponse(matches=matches)
