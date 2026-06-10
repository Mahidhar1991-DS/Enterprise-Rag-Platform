import uuid

from src.models.chunk import Chunk
from src.database.chunk_repository import (
    ChunkRepository
)


repo = ChunkRepository()

version_id = str(uuid.uuid4())

chunk = Chunk(
    chunk_id=str(uuid.uuid4()),
    version_id=version_id,
    chunk_index=0,
    chunk_text="Employees receive 30 annual leave days."
)

repo.create_chunk(chunk)

chunks = repo.get_chunks_by_version(
    version_id
)

for chunk in chunks:
    print(chunk)