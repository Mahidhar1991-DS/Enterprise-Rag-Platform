from src.retrieval.retrievers.faiss_retriever import (
    FAISSRetriever
)


class RetrievalManager:

    def __init__(
        self,
        faiss_client
    ):

        self.retriever = (
            FAISSRetriever(
                faiss_client
            )
        )

    def retrieve(
        self,
        query: str
    ):

        return (
            self.retriever.retrieve(
                query
            )
        )