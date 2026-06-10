from src.orchestrator.retrieval_pipeline import (
    RetrievalPipeline
)

from src.llm.chains.rag_chain import (
    RAGChain
)

question = (
    "How many leave days do employees get?"
)

pipeline = (
    RetrievalPipeline()
)

chunks = (
    pipeline.retrieve(
        question
    )
)

rag = (
    RAGChain()
)

response = (
    rag.run(
        question,
        chunks
    )
)

print("\nResponse:\n")

print(response)