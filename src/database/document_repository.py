from typing import Optional

from src.models.document import (
    Document
)

from src.database.postgres_client import (
    DatabaseClient
)


class DocumentRepository:

    def __init__(self):

        self.db = DatabaseClient()

    def create_document(
        self,
        document: Document
    ) -> None:

        conn = self.db.get_connection()

        try:

            conn.execute(
                """
                INSERT INTO documents(
                    document_id,
                    document_name,
                    category,
                    source_type,
                    source_path,
                    status,
                    access_level
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    document.document_id,
                    document.document_name,
                    document.category,
                    document.source_type,
                    document.source_path,
                    document.status,
                    document.access_level,
                ),
            )

            conn.commit()

        finally:

            conn.close()

    def get_document_by_id(
        self,
        document_id: str
    ) -> Optional[dict]:

        conn = self.db.get_connection()

        try:

            cursor = conn.execute(
                """
                SELECT *
                FROM documents
                WHERE document_id = ?
                """,
                (document_id,),
            )

            row = cursor.fetchone()

            return dict(row) if row else None

        finally:

            conn.close()

    def get_document_by_name(
        self,
        document_name: str
    ) -> Optional[dict]:

        conn = self.db.get_connection()

        try:

            cursor = conn.execute(
                """
                SELECT *
                FROM documents
                WHERE document_name = ?
                """,
                (document_name,),
            )

            row = cursor.fetchone()

            return dict(row) if row else None

        finally:

            conn.close()

    def get_all_documents(
        self
    ) -> list[dict]:

        conn = self.db.get_connection()

        try:

            cursor = conn.execute(
                """
                SELECT *
                FROM documents
                ORDER BY created_at DESC
                """
            )

            rows = cursor.fetchall()

            return [
                dict(row)
                for row in rows
            ]

        finally:

            conn.close()

    def delete_document(
        self,
        document_id: str
    ) -> None:

        conn = self.db.get_connection()

        try:

            cursor = conn.execute(
                """
                DELETE
                FROM documents
                WHERE document_id = ?
                """,
                (document_id,)
            )

            print(
                "Rows Deleted:",
                cursor.rowcount
            )

            conn.commit()

        finally:

            conn.close()