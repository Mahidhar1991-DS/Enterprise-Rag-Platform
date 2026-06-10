class CitationPrompt:

    @staticmethod
    def build(results):

        citations = []

        for item in results:

            citations.append(
                f"""
Source: {item['document_name']}
Version: {item['version_number']}
"""
            )

        return "\n".join(
            citations
        )