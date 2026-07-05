from src.retrieval.semantic_retriever import (
    SemanticRetriever
)

from src.retrieval.bm25_retriever import (
    BM25Retriever
)

from src.retrieval.rank_fusion import (
    ReciprocalRankFusion
)


class HybridRetriever:

    def __init__(self):

        self.semantic = (
            SemanticRetriever()
        )

        self.bm25 = (
            BM25Retriever()
        )

        self.rrf = (
            ReciprocalRankFusion()
        )

    def search(
        self,
        query_embedding,
        query_text,
        top_k: int = 5
    ):

        semantic_results = (
            self.semantic.search(
                query_embedding=query_embedding,
                top_k=top_k
            )
        )

        bm25_results = (
            self.bm25.search(
                query=query_text,
                top_k=top_k
            )
        )

        fused_results = (
            self.rrf.fuse(
                semantic_results,
                bm25_results
            )
        )

        return fused_results[:top_k]