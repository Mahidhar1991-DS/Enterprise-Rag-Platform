from src.vectorstore.faiss_client import (
    FAISSClient
)

from src.embeddings.embedding_manager import (
    EmbeddingManager
)

from src.retrieval.database_retriever import (
    DatabaseRetriever
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
        question
    ):

        query_embedding = (
            self.embedding_manager
            .create_embedding(
                question
            )
        )

        faiss_results = (
            self.faiss.search(
                query_embedding
            )
        )

        return (
            self.database_retriever
            .retrieve_chunks(
                faiss_results
            )
        )