from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from src.constants.embedding_status import (
    EmbeddingStatus
)


@dataclass
class Chunk:

    chunk_id: str

    version_id: str

    chunk_index: int

    chunk_text: str

    vector_id: Optional[str] = None

    embedding_status: str = EmbeddingStatus.PENDING

    created_at: Optional[datetime] = None

    def to_dict(
        self
    ) -> dict:

        return {
            "chunk_id": self.chunk_id,
            "version_id": self.version_id,
            "chunk_index": self.chunk_index,
            "chunk_text": self.chunk_text,
            "vector_id": self.vector_id,
            "embedding_status": self.embedding_status,
            "created_at": self.created_at,
        }