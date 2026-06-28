from src.vectorstore.faiss_client import (
    FAISSClient
)

from src.embeddings.embedding_manager import (
    EmbeddingManager
)

from src.retrieval.database_retriever import (
    DatabaseRetriever
)

from src.models.search_request import (
    SearchRequest
)


class RetrievalPipeline:

    def __init__(self):

        self.faiss = (
            FAISSClient()
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

        faiss_results = (
            self.faiss.search(
                query_embedding
            )
        )

        chunks = (
            self.database_retriever
            .retrieve_chunks(
                faiss_results=faiss_results,
                request=request
            )
        )

        return chunks