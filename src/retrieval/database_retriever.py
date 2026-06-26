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
        faiss_results
    ):

        chunks = []

        for result in faiss_results:

            chunk = (
                self.chunk_repo
                .get_active_chunk_by_id(
                    result["chunk_id"]
                )
            )

            if chunk:

                chunks.append(
                    chunk
                )

        return chunks