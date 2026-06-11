import uuid

from src.models.version import DocumentVersion
from src.database.version_repository import VersionRepository


class VersionManager:

    def __init__(self):

        self.version_repo = VersionRepository()

    def create_new_version(
        self,
        document_id: str,
        file_hash: str,
        file_size: int
    ):

        latest = self.version_repo.get_latest_version(
            document_id
        )

        if latest:

            version_number = (
                latest["version_number"] + 1
            )

            self.version_repo.deactivate_versions(
                document_id
            )

        else:

            version_number = 1

        version = DocumentVersion(
            version_id=str(uuid.uuid4()),
            document_id=document_id,
            version_number=version_number,
            file_hash=file_hash,
            file_size=file_size,
            active=True
        )

        self.version_repo.create_version(
            version
        )

        return version
    