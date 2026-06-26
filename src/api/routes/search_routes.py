from fastapi import APIRouter

from src.models.search_request import (
    SearchRequest
)

from src.orchestrator.retrieval_pipeline import (
    RetrievalPipeline
)

from src.llm.chains.rag_chain import (
    RAGChain
)

router = APIRouter()

pipeline = RetrievalPipeline()

rag = RAGChain()


@router.post("/search")
def search(
    request: SearchRequest
):

    chunks = (
        pipeline.retrieve(
            question = request.question,
            category= request.category
        )
    )

    response = (
        rag.run(
            request.question,
            chunks
        )
    )

    return {
        "answer": response
    }