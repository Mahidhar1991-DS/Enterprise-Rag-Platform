import uuid
from pathlib import Path

from src.models.document import Document

from src.models.chunk import Chunk

from src.database.chunk_repository import (
    ChunkRepository
)

from src.preprocessing.chunkers.recursive_chunker import (
    RecursiveChunker
)

from src.embeddings.embedding_manager import (
    EmbeddingManager
)

from src.vectorstore.faiss_client import (
    FAISSClient
)

from src.ingestion.ingestion_manager import (
    IngestionManager
)

from src.sync.hash_generator import (
    HashGenerator
)

from src.database.document_repository import (
    DocumentRepository
)

from src.database.version_repository import (
    VersionRepository
)

from src.database.audit_repository import (
    AuditRepository
)

from src.versioning.version_manager import (
    VersionManager
)


class IngestionPipeline:

    def __init__(self):

        self.document_repo = DocumentRepository()

        self.version_repo = VersionRepository()

        self.audit_repo = AuditRepository()

        self.version_manager = VersionManager()

        self.chunk_repo = ChunkRepository()

        self.chunker = RecursiveChunker()

        self.embedding_manager = (
        EmbeddingManager()
        )

        self.faiss_client = (
        FAISSClient()
        )

    def process_file(
    self,
    file_path: str,
    category: str = "GENERAL",
    access_level: str = "PUBLIC"
    ):

        file_name = Path(
            file_path
        ).name

        print(
            f"Processing: {file_name}"
        )

        content = (
            IngestionManager.load_document(
                file_path
            )
        )

        file_hash = (
            HashGenerator.generate(
                content
            )
        )

        existing_document = (
            self.document_repo.get_document_by_name(
                file_name
            )
        )

        if existing_document:

            document_id = (
                existing_document[
                    "document_id"
                ]
            )

            latest_version = (
                self.version_repo
                .get_latest_version(
                    document_id
                )
            )

            if (
                latest_version
                and
                latest_version["file_hash"]
                == file_hash
            ):

                print(
                    "No changes detected."
                )

                return

            version = (
                self.version_manager
                .create_new_version(
                    document_id=document_id,
                    file_hash=file_hash,
                    file_size=len(content)
                )
            )

            self.audit_repo.create_audit_log(
                document_id=document_id,
                event_type="UPDATE",
                old_version=version.version_number - 1,
                new_version=version.version_number,
                description=f"{file_name} updated"
            )

            print(
                f"Created Version {version.version_number}"
            )
            self.create_chunks_and_embeddings(
                content,
                version.version_id
            )
            
        else:

            document_id = str(
                uuid.uuid4()
            )

            document = Document(
                document_id=document_id,
                document_name=file_name,
                category=category,
                source_type="LOCAL",
                source_path=file_path,
                access_level=access_level
            )

            self.document_repo.create_document(
                document
            )

            version = (
                self.version_manager
                .create_new_version(
                    document_id=document_id,
                    file_hash=file_hash,
                    file_size=len(content)
                )
            )

            self.audit_repo.create_audit_log(
                document_id=document_id,
                event_type="UPLOAD",
                new_version=1,
                description=f"{file_name} uploaded"
            )

            print(
                "Document created."
            )

            print(
                    "Version 1 created."
                )

            self.create_chunks_and_embeddings(
                content,
                version.version_id
            )
             
    def create_chunks_and_embeddings(
        self,
        content,
        version_id
    ):

        chunks = self.chunker.split(
            content
        )

        for index, chunk_text in enumerate(chunks):

            chunk = Chunk(
                chunk_id=str(uuid.uuid4()),
                version_id=version_id,
                chunk_index=index,
                chunk_text=chunk_text
            )

            self.chunk_repo.create_chunk(
                chunk
            )

            embedding = (
                self.embedding_manager
                .create_embedding(
                    chunk_text
                )
            )

            self.faiss_client.add_document(
                embedding=embedding,
                chunk_id=chunk.chunk_id
            )

        print(
            f"Created {len(chunks)} chunks"
        )