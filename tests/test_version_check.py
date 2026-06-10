from src.database.postgres_client import DatabaseClient

db = DatabaseClient()

conn = db.get_connection()

cursor = conn.execute("""
SELECT *
FROM document_versions
ORDER BY version_number
""")

rows = cursor.fetchall()

for row in rows:
    print(dict(row))

conn.close()