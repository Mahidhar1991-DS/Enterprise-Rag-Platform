import uuid

from src.database.postgres_client import DatabaseClient
from src.database.document_repository import DocumentRepository
from src.models.document import Document


def main():

    db = DatabaseClient()

    db.initialize_database()

    repo = DocumentRepository()

    document = Document(
        document_id=str(uuid.uuid4()),
        document_name="leave_policy.pdf",
        category="HR"
    )

    repo.create_document(document)

    result = repo.get_document_by_name(
        "leave_policy.pdf"
    )

    print(result)


if __name__ == "__main__":
    main()