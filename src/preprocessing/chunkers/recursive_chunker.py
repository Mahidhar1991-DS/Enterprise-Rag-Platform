from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)


class RecursiveChunker:

    def __init__(
        self,
        chunk_size=500,
        chunk_overlap=100
    ):

        self.splitter = (
            RecursiveCharacterTextSplitter(
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap
            )
        )

    def split(
        self,
        text: str
    ):

        return self.splitter.split_text(
            text
        )