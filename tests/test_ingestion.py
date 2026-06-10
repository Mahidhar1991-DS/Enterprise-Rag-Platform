from src.ingestion.ingestion_manager import (
    IngestionManager
)


content = IngestionManager.load_document(
    "data/raw/sample.txt"
)

print(content)