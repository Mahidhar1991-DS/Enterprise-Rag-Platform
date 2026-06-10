import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class OpenAIClient:

    def __init__(self):

        self.client = OpenAI(
            api_key=os.getenv(
                "OPENAI_API_KEY"
            )
        )

    def generate_response(
        self,
        prompt: str
    ):

        response = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        return (
            response
            .choices[0]
            .message
            .content
        )