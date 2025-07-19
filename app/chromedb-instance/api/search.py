from fastapi import APIRouter
from models.request import SearchRequest
from models.response import SearchResponse, MatchItem
from core.chroma import search_documents

router = APIRouter()

@router.post("/", response_model=SearchResponse)
def search(req: SearchRequest):
    # Query ChromaDB
    raw_matches = search_documents(req.query, req.top_k)

    # Convert list of dicts → list of MatchItem objects
    structured_matches = [MatchItem(**match) for match in raw_matches]

    return SearchResponse(matches=structured_matches)
