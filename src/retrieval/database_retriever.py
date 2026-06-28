from src.database.chunk_repository import (
    ChunkRepository
)

from src.models.search_request import (
    SearchRequest
)


class DatabaseRetriever:

    def __init__(self):

        self.chunk_repo = (
            ChunkRepository()
        )

    def retrieve_chunks(
        self,
        faiss_results,
        request: SearchRequest
    ):

        chunks = []

        for result in faiss_results:

            chunk = (
                self.chunk_repo
                .get_active_chunk_by_id(
                    chunk_id=result["chunk_id"],
                    request=request
                )
            )

            if chunk:

                chunks.append(
                    chunk
                )

        return chunks