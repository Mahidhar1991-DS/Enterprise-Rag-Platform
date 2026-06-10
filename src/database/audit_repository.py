import uuid

from src.database.postgres_client import DatabaseClient


class AuditRepository:

    def __init__(self):
        self.db = DatabaseClient()

    def create_audit_log(
        self,
        document_id: str,
        event_type: str,
        old_version: int = None,
        new_version: int = None,
        description: str = None
    ):

        conn = self.db.get_connection()

        try:

            conn.execute(
                """
                INSERT INTO audit_logs(
                    audit_id,
                    document_id,
                    event_type,
                    old_version,
                    new_version,
                    description
                )
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    str(uuid.uuid4()),
                    document_id,
                    event_type,
                    old_version,
                    new_version,
                    description,
                ),
            )

            conn.commit()

        finally:
            conn.close()