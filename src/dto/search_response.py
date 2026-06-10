from pydantic import BaseModel


class SearchResponse(BaseModel):

    answer: str