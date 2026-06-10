class RAGPrompt:

    @staticmethod
    def build(
        question,
        context
    ):

        return f"""
You are an enterprise document assistant.

Answer ONLY from the provided context.

If the answer is not available in the context,
say:

'I could not find this information in the documents.'

Context:
{context}

Question:
{question}

Answer:
"""