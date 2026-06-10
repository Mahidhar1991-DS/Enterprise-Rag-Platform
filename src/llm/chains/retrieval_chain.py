class RetrievalChain:

    @staticmethod
    def build_context(results):

        contexts = []

        for item in results:

            if isinstance(item, dict):

                contexts.append(
                    item["chunk_text"]
                )

            else:

                contexts.append(
                    str(item)
                )

        return "\n\n".join(
            contexts
        )