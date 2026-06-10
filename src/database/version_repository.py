from typing import Optional

from src.models.version import DocumentVersion
from src.database.postgres_client import DatabaseClient


class VersionRepository:

    def __init__(self):
        self.db = DatabaseClient()

    def create_version(
        self,
        version: DocumentVersion
    ):

        conn = self.db.get_connection()

        try:

            conn.execute(
                """
                INSERT INTO document_versions(
                    version_id,
                    document_id,
                    version_number,
                    file_hash,
                    file_size,
                    active
                )
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    version.version_id,
                    version.document_id,
                    version.version_number,
                    version.file_hash,
                    version.file_size,
                    int(version.active),
                ),
            )

            conn.commit()

        finally:
            conn.close()

    def deactivate_versions(
        self,
        document_id: str
    ):

        conn = self.db.get_connection()

        try:

            conn.execute(
                """
                UPDATE document_versions
                SET active = 0
                WHERE document_id = ?
                """,
                (document_id,),
            )

            conn.commit()

        finally:
            conn.close()

    def get_latest_version(
        self,
        document_id: str
    ) -> Optional[dict]:

        conn = self.db.get_connection()

        try:

            cursor = conn.execute(
                """
                SELECT *
                FROM document_versions
                WHERE document_id = ?
                ORDER BY version_number DESC
                LIMIT 1
                """,
                (document_id,),
            )

            row = cursor.fetchone()

            return dict(row) if row else None

        finally:
            conn.close()

    def get_versions_by_document(
        self,
        document_id: str
    ):

        conn = self.db.get_connection()

        try:

            cursor = conn.execute(
                """
                SELECT *
                FROM document_versions
                WHERE document_id = ?
                ORDER BY version_number DESC
                """,
                (document_id,),
            )

            rows = cursor.fetchall()

            return [dict(row) for row in rows]

        finally:
            conn.close()

    def get_active_version(
        self,
        document_id: str
    ):

        conn = self.db.get_connection()

        try:

            cursor = conn.execute(
                """
                SELECT *
                FROM document_versions
                WHERE document_id = ?
                AND active = 1
                LIMIT 1
                """,
                (document_id,),
            )

            row = cursor.fetchone()

            return dict(row) if row else None

        finally:
            conn.close()