from src.database.postgres_client import DatabaseClient
from src.models.chunk import Chunk
from src.models.search_request import SearchRequest


class ChunkRepository:

    def __init__(self):
        self.db = DatabaseClient()

    def create_chunk(
        self,
        chunk: Chunk
    ):

        conn = self.db.get_connection()

        try:

            conn.execute(
                """
                INSERT INTO document_chunks(
                    chunk_id,
                    version_id,
                    chunk_index,
                    chunk_text,
                    vector_id,
                    embedding_status
                )
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    chunk.chunk_id,
                    chunk.version_id,
                    chunk.chunk_index,
                    chunk.chunk_text,
                    chunk.vector_id,
                    chunk.embedding_status,
                ),
            )

            conn.commit()

        finally:
            conn.close()

    def get_chunks_by_version(
        self,
        version_id: str
    ):

        conn = self.db.get_connection()

        try:

            cursor = conn.execute(
                """
                SELECT *
                FROM document_chunks
                WHERE version_id = ?
                ORDER BY chunk_index
                """,
                (version_id,),
            )

            rows = cursor.fetchall()

            return [dict(row) for row in rows]

        finally:
            conn.close()

    def delete_chunks_by_version(
        self,
        version_id: str
    ):

        conn = self.db.get_connection()

        try:

            conn.execute(
                """
                DELETE
                FROM document_chunks
                WHERE version_id = ?
                """,
                (version_id,),
            )

            conn.commit()

        finally:
            conn.close()

    def get_all_chunks(self):

        conn = self.db.get_connection()

        try:

            cursor = conn.execute(
                """
                SELECT *
                FROM document_chunks
                """
            )

            rows = cursor.fetchall()

            return [dict(row) for row in rows]

        finally:
            conn.close()

    def get_active_chunk_by_id(
        self,
        chunk_id: str,
        request: SearchRequest
    ):

        conn = self.db.get_connection()

        try:

            query = """
                SELECT
                dc.*,
                d.category,
                d.document_name,
                d.access_level
                FROM document_chunks dc
                JOIN document_versions dv
                    ON dc.version_id = dv.version_id
                JOIN documents d
                    ON dv.document_id = d.document_id
                WHERE
                    dc.chunk_id = ?
                    AND dv.active = 1
            """

            params = [chunk_id]

            if request.category:

                query += """
                    AND d.category = ?
                """

                params.append(
                    request.category
                )

            if request.document_name:

                query += """
                    AND d.document_name = ?
                """

                params.append(
                    request.document_name
                )

            cursor = conn.execute(
                query,
                params
            )

            row = cursor.fetchone()

            return dict(row) if row else None

        finally:

            conn.close()