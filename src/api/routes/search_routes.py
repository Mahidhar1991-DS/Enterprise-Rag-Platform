from fastapi import APIRouter

from src.models.search_request import (
    SearchRequest
)

from src.services.search_service import (
    SearchService
)

router = APIRouter()

search_service = SearchService()


@router.post("/search")
def search(
    request: SearchRequest
):

    return search_service.search(
        request
    )