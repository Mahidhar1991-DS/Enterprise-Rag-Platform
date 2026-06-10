from src.ingestion.ingestion_manager import (
    IngestionManager
)

from src.preprocessing.chunkers.recursive_chunker import (
    RecursiveChunker
)


content = (
    IngestionManager.load_document(
        "data/raw/sample.txt"
    )
)

chunker = RecursiveChunker()

chunks = chunker.split(content)

print(
    f"Total Chunks: {len(chunks)}"
)

for i, chunk in enumerate(chunks):

    print(
        f"\nChunk {i+1}\n"
    )

    print(chunk)