from src.llm.openai_client import (
    OpenAIClient
)

client = OpenAIClient()

response = client.generate_response(
    "What is 2 + 2?"
)

print(response)