from pathlib import Path

from src.orchestrator.ingestion_pipeline import (
    IngestionPipeline
)


class DocumentWatcher:

    def __init__(self):

        self.pipeline = IngestionPipeline()

    def scan_folder(
        self,
        folder_path: str
    ):

        folder = Path(folder_path)

        files = folder.glob("*")

        for file in files:

            if file.is_file():

                print(
                    f"Found: {file.name}"
                )

                self.pipeline.process_file(
                    str(file)
                )