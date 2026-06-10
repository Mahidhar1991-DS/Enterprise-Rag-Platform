from src.embeddings.embedding_manager import (
    EmbeddingManager
)

from src.vectorstore.faiss_client import (
    FAISSClient
)


documents = [

    "Employees receive 30 annual leave days.",

    "Travel expenses are reimbursed.",

    "Medical insurance is provided."
]


embedding_manager = (
    EmbeddingManager()
)

vectors = []

for doc in documents:

    vector = (
        embedding_manager
        .create_embedding(doc)
    )

    vectors.append(vector)

faiss_client = FAISSClient()

faiss_client.add_vectors(
    vectors
)

query = (
    embedding_manager
    .create_embedding(
        "How many leave days do employees get?"
    )
)

distances, indices = (
    faiss_client.search(
        query,
        top_k=2
    )
)

print(indices)
print(distances)