from src.vectorstore.faiss_client import (
    FAISSClient
)

from src.embeddings.embedding_manager import (
    EmbeddingManager
)


faiss_client = FAISSClient()

embedding_manager = (
    EmbeddingManager()
)

embedding = (
    embedding_manager.create_embedding(
        "Employees receive 30 annual leave days."
    )
)

faiss_client.add_document(
    embedding=embedding,
    chunk_id= '374a9fd2-a3b2-49f0-852e-a44c027d6f63'
)

print(
    "Saved successfully"
)
   
print(
    f"Total Vectors: {faiss_client.get_total_vectors()}"
)