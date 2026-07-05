from dataclasses import dataclass


@dataclass
class RetrievalResult:

    chunk_id: str

    chunk_text: str

    score: float

    source: str