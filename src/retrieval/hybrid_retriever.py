from src.retrieval.keyword_retriever import (
    KeywordRetriever
)

from src.vectorstore.faiss_client import (
    FAISSClient
)


class HybridRetriever:

    def __init__(self):

        self.keyword = (
            KeywordRetriever()
        )

        self.faiss = (
            FAISSClient()
        )

    def search(
        self,
        query_embedding,
        query_text,
        top_k: int = 5
    ):

        semantic_results = (
            self.faiss.search(
                embedding=query_embedding,
                top_k=top_k
            )
        )

        keyword_results = (
            self.keyword.search(
                query=query_text,
                top_k=top_k
            )
        )

        return (
            semantic_results,
            keyword_results
        )