from src.embeddings.embedding_manager import (
    EmbeddingManager
)


class FAISSRetriever:

    def __init__(
        self,
        faiss_client
    ):

        self.faiss_client = faiss_client

        self.embedding_manager = (
            EmbeddingManager()
        )

    def retrieve(
        self,
        query: str,
        top_k=3
    ):

        query_embedding = (
            self.embedding_manager
            .create_embedding(query)
        )

        return (
            self.faiss_client.search(
                query_embedding,
                top_k
            )
        )