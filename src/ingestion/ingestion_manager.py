from pathlib import Path

from src.ingestion.loaders.pdf_loader import PDFLoader
from src.ingestion.loaders.docx_loader import DOCXLoader
from src.ingestion.loaders.txt_loader import TXTLoader


class IngestionManager:

    @staticmethod
    def load_document(
        file_path: str
    ) -> str:

        extension = Path(
            file_path
        ).suffix.lower()

        if extension == ".pdf":
            return PDFLoader.load(file_path)

        if extension == ".docx":
            return DOCXLoader.load(file_path)

        if extension == ".txt":
            return TXTLoader.load(file_path)

        raise ValueError(
            f"Unsupported file type: {extension}"
        )