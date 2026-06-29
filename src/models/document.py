from dataclasses import dataclass


@dataclass
class Document:

    document_id: str

    document_name: str

    category: str

    source_type: str

    source_path: str

    access_level: str = "PUBLIC"

    status: str = "ACTIVE"