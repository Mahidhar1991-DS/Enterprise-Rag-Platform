from src.llm.prompts.rag_prompt import RAGPrompt
from src.llm.response_generator import ResponseGenerator
from src.llm.chains.retrieval_chain import RetrievalChain


class RAGChain:

    def __init__(self):
        self.generator = ResponseGenerator()

    def run(
        self,
        question,
        results
    ):

        context = (
            RetrievalChain.build_context(
                results
            )
        )

        prompt = (
            RAGPrompt.build(
                question,
                context
            )
        )

        answer = (
            self.generator.generate(
                prompt
            )
        )

        citations = []

        for item in results:

            if isinstance(item, dict):

                citations.append(
                    f"Chunk ID: {item['chunk_id']}"
                )

        citation_text = "\n".join(
            citations
        )

        return f"""
{answer}

Sources:
{citation_text}
"""