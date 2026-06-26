from src.database.postgres_client import DatabaseClient
from src.models.chunk import Chunk


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

    def get_chunk_by_id(
        self,
        chunk_id: str
    ):

        conn = self.db.get_connection()

        try:

            cursor = conn.execute(
                """
                SELECT *
                FROM document_chunks
                WHERE chunk_id = ?
                """,
                (chunk_id,),
            )

            row = cursor.fetchone()

            return dict(row) if row else None

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
        chunk_id: str
    ):

        conn = self.db.get_connection()

        try:

            cursor = conn.execute(
                """
                SELECT dc.*
                FROM document_chunks dc
                JOIN document_versions dv
                ON dc.version_id = dv.version_id
                WHERE
                    dc.chunk_id = ?
                    AND dv.active = 1
                """,
                (chunk_id,)
            )

            row = cursor.fetchone()

            return dict(row) if row else None

        finally:
            conn.close()