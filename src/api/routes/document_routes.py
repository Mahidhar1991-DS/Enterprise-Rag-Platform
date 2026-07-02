from fastapi import APIRouter

from src.database.document_repository import (
    DocumentRepository
)

from src.database.version_repository import (
    VersionRepository
)

router = APIRouter()

document_repo = DocumentRepository()

version_repo = VersionRepository()


@router.get("/documents")
def get_documents():

    return (
        document_repo.get_all_documents()
    )


@router.get(
    "/documents/{document_id}/versions"
)
def get_document_versions(
    document_id: str
):

    return (
        version_repo.get_versions_by_document(
            document_id
        )
    )


@router.get(
    "/documents/{document_id}"
)
def get_document(
    document_id: str
):

    document = (
        document_repo.get_document_by_id(
            document_id
        )
    )

    versions = (
        version_repo.get_versions_by_document(
            document_id
        )
    )

    active_version = None

    for version in versions:

        if version["active"]:

            active_version = version
            break

    return {
        "document": document,
        "active_version": active_version,
        "versions": versions
    }


@router.delete(
    "/documents/{document_id}"
)
def delete_document(
    document_id: str
):

    document_repo.delete_document(
        document_id
    )

    return {
        "message": "Document deleted"
    }