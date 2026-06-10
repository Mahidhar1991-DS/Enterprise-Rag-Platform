from src.embeddings.embedding_manager import (
    EmbeddingManager
)

manager = EmbeddingManager()

embedding = manager.create_embedding(
    "Employees receive 30 annual leave days."
)

print(
    f"Vector Length: {len(embedding)}"
)

print(
    embedding[:10]
)