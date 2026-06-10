from src.vectorstore.faiss_client import (
    FAISSClient
)

from src.embeddings.embedding_manager import (
    EmbeddingManager
)

from src.retrieval.retrieval_manager import (
    RetrievalManager
)


documents = [

    "Employees receive 30 annual leave days.",

    "Travel expenses are reimbursed.",

    "Medical insurance is provided."
]


embedding_manager = (
    EmbeddingManager()
)

faiss_client = FAISSClient()

for doc in documents:

    embedding = (
        embedding_manager
        .create_embedding(doc)
    )

    faiss_client.add_document(
        embedding,
        doc
    )

retrieval_manager = (
    RetrievalManager(
        faiss_client
    )
)

results = retrieval_manager.retrieve(
    "How many leave days do employees get?"
)

print("\nRetrieved Results:\n")

for result in results:

    print(result)