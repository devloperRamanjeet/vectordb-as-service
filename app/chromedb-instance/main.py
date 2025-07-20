from fastapi import FastAPI
from api.embed import router as embed_router
from api.search import router as search_router
from api.delete import router as delete_router
from api.health import router as health_router
from api.home import router as home_router

app = FastAPI(title="Tenant VectorDB")


app.include_router(embed_router, prefix="/embed")
app.include_router(search_router, prefix="/search")
app.include_router(delete_router, prefix="/delete")
app.include_router(health_router, prefix="/healthz")
