from fastapi import FastAPI

from src.api.routes.health_routes import (
    router as health_router
)

from src.api.routes.search_routes import (
    router as search_router
)

from src.api.routes.upload_routes import (
    router as upload_router
)

from src.api.routes.document_routes import (
    router as document_router
)


app = FastAPI(
    title="Enterprise RAG Platform"
)

app.include_router(
    upload_router
)

app.include_router(
    document_router
)

app.include_router(
    health_router
)

app.include_router(
    search_router
)

@app.get("/")
def root():

    return {
        "application": "Enterprise RAG Platform",
        "status": "Running"
    }