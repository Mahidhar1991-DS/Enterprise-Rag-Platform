import sqlite3
from pathlib import Path


class DatabaseClient:
    """
    Database connection manager.

    Currently uses SQLite.

    Can be replaced later with PostgreSQL
    without changing repository code.
    """

    def __init__(self, db_path: str = "database/rag.db"):
        self.db_path = db_path

    def get_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def initialize_database(self):
        schema_file = Path("database/schema.sql")

        if not schema_file.exists():
            raise FileNotFoundError(
                f"Schema file not found: {schema_file}"
            )

        with open(schema_file, "r", encoding="utf-8") as f:
            schema = f.read()

        conn = self.get_connection()

        try:
            conn.executescript(schema)
            conn.commit()
        finally:
            conn.close()

        print("Database initialized successfully.")