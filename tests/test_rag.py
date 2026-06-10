from src.llm.chains.rag_chain import (
    RAGChain
)

chunks = [
    "Employees receive 30 annual leave days."
]

question = (
    "How many leave days do employees get?"
)

rag = RAGChain()

response = rag.run(
    question,
    chunks
)

print("\nRAG Response:\n")

print(response)