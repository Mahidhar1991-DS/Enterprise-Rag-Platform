from src.database.chunk_repository import (
    ChunkRepository
)

from src.retrieval.retrieval_result import (
    RetrievalResult
)


class KeywordRetriever:

    def __init__(self):

        self.chunk_repo = (
            ChunkRepository()
        )

    def search(
        self,
        query: str,
        top_k: int = 5
    ):

        chunks = (
            self.chunk_repo.get_all_chunks()
        )

        query_words = (
            query.lower().split()
        )

        results = []

        for chunk in chunks:

            chunk_text = (
                chunk["chunk_text"].lower()
            )

            score = 0

            for word in query_words:

                if word in chunk_text:

                    score += 1

            if score > 0:

                results.append(

                    RetrievalResult(

                        chunk_id=chunk["chunk_id"],

                        chunk_text=chunk["chunk_text"],

                        score=score,

                        source="KEYWORD"

                    )

                )

        results.sort(
            key=lambda x: x.score,
            reverse=True
        )

        return results[:top_k]