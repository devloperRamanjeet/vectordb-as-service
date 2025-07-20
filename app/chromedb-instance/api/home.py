from fastapi import APIRouter


router = APIRouter()

@router.get("/")
def home_router():
    return "hello world"
