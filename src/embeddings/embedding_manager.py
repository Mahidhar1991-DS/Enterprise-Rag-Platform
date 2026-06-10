from src.embeddings.transformer_embedding import (
    TransformerEmbedding
)


class EmbeddingManager:

    def __init__(self):

        self.embedding_model = (
            TransformerEmbedding()
        )

    def create_embedding(
        self,
        text: str
    ):

        return (
            self.embedding_model
            .generate_embedding(text)
        )