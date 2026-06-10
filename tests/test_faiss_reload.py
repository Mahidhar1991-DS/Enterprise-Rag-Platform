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

query_embedding = (
    embedding_manager.create_embedding(
        "How many leave days do employees get?"
    )
)

results = (
    faiss_client.search(
        query_embedding,
        top_k=3
    )
)

print("\nRetrieved Results:\n")

for result in results:

    print(result)