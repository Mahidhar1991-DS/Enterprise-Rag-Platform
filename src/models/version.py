from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class DocumentVersion:
    """
    Represents a specific version of a document.

    Example:

    leave_policy.pdf

    Version 1
    Version 2
    Version 3
    """

    version_id: str

    document_id: str

    version_number: int

    file_hash: str

    file_size: Optional[int] = None

    active: bool = True

    uploaded_at: Optional[datetime] = None

    def to_dict(self) -> dict:
        return {
            "version_id": self.version_id,
            "document_id": self.document_id,
            "version_number": self.version_number,
            "file_hash": self.file_hash,
            "file_size": self.file_size,
            "active": self.active,
            "uploaded_at": self.uploaded_at,
        }