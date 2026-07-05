from src.vectorstore.faiss_client import (
    FAISSClient
)

from src.retrieval.retrieval_result import (
    RetrievalResult
)


class SemanticRetriever:

    def __init__(self):

        self.faiss = (
            FAISSClient()
        )

    def search(
        self,
        query_embedding,
        top_k: int = 5
    ):

        faiss_results = (
            self.faiss.search(
                query_embedding=query_embedding,
                top_k=top_k
            )
        )

        results = []

        for result in faiss_results:

            results.append(

                RetrievalResult(

                    chunk_id=result["chunk_id"],

                    chunk_text="",

                    score=0.0,

                    source="SEMANTIC"

                )

            )

        return results