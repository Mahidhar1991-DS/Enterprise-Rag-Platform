from src.llm.chains.rag_chain import (
    RAGChain
)

results = [
    {
        "chunk_id": "chunk_001",
        "document_name": "leave_policy.pdf",
        "version_number": 2,
        "chunk_text": "Employees receive 30 annual leave days."
    }
]

question = (
    "How many leave days do employees get?"
)

rag = RAGChain()

response = rag.run(
    question,
    results
)

print(response)