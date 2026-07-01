from typing import Optional

from src.database.postgres_client import (
    DatabaseClient
)

from src.models.metric import (
    Metric
)


class MetricRepository:

    def __init__(self):

        self.db = DatabaseClient()

    def create_metric(
        self,
        metric: Metric
    ):

        conn = self.db.get_connection()

        try:

            conn.execute(
                """
                INSERT INTO metrics(
                    metric_id,
                    metric_name,
                    metric_value,
                    metric_type
                )
                VALUES (?, ?, ?, ?)
                """,
                (
                    metric.metric_id,
                    metric.metric_name,
                    metric.metric_value,
                    metric.metric_type
                )
            )

            conn.commit()

        finally:

            conn.close()

    def get_metric(
        self,
        metric_name: str
    ) -> Optional[dict]:

        conn = self.db.get_connection()

        try:

            cursor = conn.execute(
                """
                SELECT *
                FROM metrics
                WHERE metric_name = ?
                ORDER BY created_at DESC
                LIMIT 1
                """,
                (metric_name,)
            )

            row = cursor.fetchone()

            return dict(row) if row else None

        finally:

            conn.close()

    def get_all_metrics(
        self
    ):

        conn = self.db.get_connection()

        try:

            cursor = conn.execute(
                """
                SELECT *
                FROM metrics
                ORDER BY created_at DESC
                """
            )

            rows = cursor.fetchall()

            return [dict(row) for row in rows]

        finally:

            conn.close()