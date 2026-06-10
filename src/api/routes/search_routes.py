from fastapi import APIRouter

from src.dto.search_request import (
    SearchRequest
)

from src.dto.search_response import (
    SearchResponse
)

from src.orchestrator.retrieval_pipeline import (
    RetrievalPipeline
)

from src.llm.chains.rag_chain import (
    RAGChain
)

router = APIRouter()


@router.post(
    "/search",
    response_model=SearchResponse
)
def search(
    request: SearchRequest
):

    question = request.question

    pipeline = (
        RetrievalPipeline()
    )

    rag = (
        RAGChain()
    )

    chunks = (
        pipeline.retrieve(
            question
        )
    )

    response = (
        rag.run(
            question,
            chunks
        )
    )

    return SearchResponse(
        answer=response
    )