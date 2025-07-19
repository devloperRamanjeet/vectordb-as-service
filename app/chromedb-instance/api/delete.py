from fastapi import APIRouter
from models.request import DeleteRequest
from models.response import DeleteResponse
from core.chroma import delete_documents

router = APIRouter()

@router.post("/", response_model=DeleteResponse)
def delete(req: DeleteRequest):
    count = delete_documents(req.vector_ids)
    return DeleteResponse(deleted_count=count)
