from src.embeddings.embedding_manager import (
    EmbeddingManager
)

from src.retrieval.database_retriever import (
    DatabaseRetriever
)

from src.retrieval.hybrid_retriever import (
    HybridRetriever
)

from src.models.search_request import (
    SearchRequest
)


class RetrievalPipeline:

    def __init__(self):

        self.hybrid = (
            HybridRetriever()
        )

        self.embedding_manager = (
            EmbeddingManager()
        )

        self.database_retriever = (
            DatabaseRetriever()
        )

    def retrieve(
        self,
        request: SearchRequest
    ):

        query_embedding = (
            self.embedding_manager
            .create_embedding(
                request.question
            )
        )

        retrieval_results = (
            self.hybrid.search(
                query_embedding=query_embedding,
                query_text=request.question
            )
        )

        chunks = (
            self.database_retriever
            .retrieve_chunks(
                retrieval_results=retrieval_results,
                request=request
            )
        )

        return chunks