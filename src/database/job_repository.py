from typing import Optional

from src.database.postgres_client import (
    DatabaseClient
)

from src.models.job import (
    Job
)


class JobRepository:

    def __init__(self):

        self.db = DatabaseClient()

    def create_job(
        self,
        job: Job
    ):

        conn = self.db.get_connection()

        try:

            conn.execute(
                """
                INSERT INTO jobs(
                    job_id,
                    file_path,
                    category,
                    access_level,
                    status
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    job.job_id,
                    job.file_path,
                    job.category,
                    job.access_level,
                    job.status
                )
            )

            conn.commit()

        finally:

            conn.close()

    def get_job(
        self,
        job_id: str
    ) -> Optional[dict]:

        conn = self.db.get_connection()

        try:

            cursor = conn.execute(
                """
                SELECT *
                FROM jobs
                WHERE job_id = ?
                """,
                (job_id,)
            )

            row = cursor.fetchone()

            return dict(row) if row else None

        finally:

            conn.close()

    def update_status(
        self,
        job_id: str,
        status: str
    ):

        conn = self.db.get_connection()

        try:

            conn.execute(
                """
                UPDATE jobs
                SET
                    status = ?,
                    completed_at = CURRENT_TIMESTAMP
                WHERE job_id = ?
                """,
                (
                    status,
                    job_id
                )
            )

            conn.commit()

        finally:

            conn.close()

    def get_pending_jobs(self):

        conn = self.db.get_connection()

        try:

            cursor = conn.execute(
                """
                SELECT *
                FROM jobs
                WHERE status = 'PENDING'
                ORDER BY created_at
                """
            )

            rows = cursor.fetchall()

            return [dict(row) for row in rows]

        finally:

            conn.close()