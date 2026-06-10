from src.vectorstore.faiss_client import (
    FAISSClient
)

client = FAISSClient()

print(
    client.get_total_vectors()
)