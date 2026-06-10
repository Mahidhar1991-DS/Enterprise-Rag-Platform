from src.database.chunk_repository import (
    ChunkRepository
)


class ChunkLookup:

    def __init__(self):

        self.repo = (
            ChunkRepository()
        )

    def get_chunk(
        self,
        chunk_id
    ):

        return (
            self.repo
            .get_chunk_by_id(
                chunk_id
            )
        )