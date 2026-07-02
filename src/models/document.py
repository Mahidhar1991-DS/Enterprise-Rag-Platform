from dataclasses import dataclass

from src.constants.access_levels import (
    AccessLevel
)

from src.constants.document_status import (
    DocumentStatus
)

from src.constants.source_types import (
    SourceType
)


@dataclass
class Document:

    document_id: str

    document_name: str

    category: str

    source_type: str = SourceType.LOCAL

    source_path: str = ""

    access_level: str = AccessLevel.PUBLIC

    status: str = DocumentStatus.ACTIVE