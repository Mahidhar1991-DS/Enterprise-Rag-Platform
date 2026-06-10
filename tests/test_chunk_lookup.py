from src.database.chunk_repository import (
    ChunkRepository
)

repo = ChunkRepository()

chunks = repo.get_all_chunks()

print()

for chunk in chunks:

    print(chunk)