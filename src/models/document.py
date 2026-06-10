from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Document:
    """
    Represents a logical document.

    Example:
        leave_policy.pdf

    A document can have multiple versions.
    """

    document_id: str
    document_name: str
    category: str

    source_type: Optional[str] = None
    source_path: Optional[str] = None

    status: str = "ACTIVE"

    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def to_dict(self) -> dict:
        return {
            "document_id": self.document_id,
            "document_name": self.document_name,
            "category": self.category,
            "source_type": self.source_type,
            "source_path": self.source_path,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }