from typing import Optional
from pydantic import BaseModel


class SearchRequest(BaseModel):

    question: str

    category: Optional[str] = None

    document_name: Optional[str] = None