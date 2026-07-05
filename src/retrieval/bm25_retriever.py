from rank_bm25 import (
    BM25Okapi
)

from src.database.chunk_repository import (
    ChunkRepository
)

from src.retrieval.retrieval_result import (
    RetrievalResult
)


class BM25Retriever:

    def __init__(self):

        self.chunk_repo = (
            ChunkRepository()
        )

        self.bm25 = None

        self.chunks = []

        self.build_index()

    def build_index(
        self
    ):

        self.chunks = (
            self.chunk_repo.get_all_chunks()
        )

        corpus = [

            chunk["chunk_text"].lower().split()

            for chunk in self.chunks
        ]

        self.bm25 = (
            BM25Okapi(corpus)
        )

    def rebuild_index(
        self
    ):

        self.build_index()

    def search(
        self,
        query: str,
        top_k: int = 5
    ):

        query_tokens = (
            query.lower().split()
        )

        scores = (
            self.bm25.get_scores(
                query_tokens
            )
        )

        results = []

        for chunk, score in zip(
            self.chunks,
            scores
        ):

            if score > 0:

                results.append(

                    RetrievalResult(

                        chunk_id=chunk["chunk_id"],

                        chunk_text=chunk["chunk_text"],

                        score=float(score),

                        source="BM25"

                    )

                )

        results.sort(
            key=lambda x: x.score,
            reverse=True
        )

        return results[:top_k]