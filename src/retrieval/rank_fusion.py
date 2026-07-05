from collections import defaultdict


class ReciprocalRankFusion:

    def __init__(
        self,
        k: int = 60
    ):

        self.k = k

    def fuse(
        self,
        *result_lists
    ):

        scores = defaultdict(float)

        documents = {}

        for results in result_lists:

            for rank, result in enumerate(
                results,
                start=1
            ):

                score = (
                    1 / (self.k + rank)
                )

                scores[
                    result.chunk_id
                ] += score

                documents[
                    result.chunk_id
                ] = result

        fused_results = sorted(

            documents.values(),

            key=lambda result:
                scores[result.chunk_id],

            reverse=True

        )

        return fused_results