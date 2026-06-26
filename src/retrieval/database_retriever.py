from src.database.chunk_repository import (
    ChunkRepository
)


class DatabaseRetriever:

    def __init__(self):

        self.chunk_repo = (
            ChunkRepository()
        )

    def retrieve_chunks(
        self,
        faiss_results,
        category = None
    ):

        chunks = []

        for result in faiss_results:

            chunk = (
                    self.chunk_repo
                    .get_active_chunk_by_id(
                        chunk_id=result["chunk_id"],
                        category=category
                    )
            )

            if chunk:

                chunks.append(
                    chunk
                )

        return chunks