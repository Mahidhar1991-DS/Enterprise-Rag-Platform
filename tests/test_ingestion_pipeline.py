from src.orchestrator.ingestion_pipeline import (
    IngestionPipeline
)


pipeline = IngestionPipeline()

pipeline.process_file(
    "data/raw/sample.txt",
    category="HR"
)