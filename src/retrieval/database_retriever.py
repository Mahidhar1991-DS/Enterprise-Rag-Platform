from src.database.chunk_repository import (
    ChunkRepository
)

from src.models.search_request import (
    SearchRequest
)

from src.authorization.permission_engine import (
    PermissionEngine
)


class DatabaseRetriever:

    def __init__(self):

        self.chunk_repo = (
            ChunkRepository()
        )

        self.permission_engine = (
            PermissionEngine()
        )

    def retrieve_chunks(
        self,
        retrieval_results,
        request: SearchRequest
    ):

        chunks = []

        for result in retrieval_results:

            chunk = (
                self.chunk_repo
                .get_active_chunk_by_id(
                    chunk_id=result.chunk_id,
                    request=request
                )
            )

            if not chunk:
                continue

            allowed = self.permission_engine.has_access(
                chunk=chunk,
                request=request
            )

            print(
                f"{chunk['document_name']} | {chunk['access_level']} | Allowed: {allowed}"
            )

            if allowed:

                chunks.append(
                    chunk
                )

        print(
            "Final Chunks:",
            [c["document_name"] for c in chunks]
        )

        return chunks