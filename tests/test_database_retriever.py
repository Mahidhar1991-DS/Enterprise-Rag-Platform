from src.vectorstore.faiss_client import (
    FAISSClient
)

from src.embeddings.embedding_manager import (
    EmbeddingManager
)

from src.retrieval.database_retriever import (
    DatabaseRetriever
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

faiss_results = (
    faiss_client.search(
        query_embedding
    )
)

retriever = (
    DatabaseRetriever()
)

chunks = (
    retriever.retrieve_chunks(
        faiss_results
    )
)

print("\nRetrieved Chunks:\n")

for chunk in chunks:

    print(chunk)