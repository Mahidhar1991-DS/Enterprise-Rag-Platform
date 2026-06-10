from src.llm.openai_client import (
    OpenAIClient
)


class ResponseGenerator:

    def __init__(self):

        self.client = OpenAIClient()

    def generate(
        self,
        prompt
    ):

        return self.client.generate_response(
            prompt
        )