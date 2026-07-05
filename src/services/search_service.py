import time

from src.orchestrator.retrieval_pipeline import (
    RetrievalPipeline
)

from src.llm.chains.rag_chain import (
    RAGChain
)

from src.monitoring.monitoring_manager import (
    MonitoringManager
)

from src.constants.metric_names import (
    MetricNames
)

from src.constants.metric_types import (
    MetricTypes
)


class SearchService:

    def __init__(self):

        self.pipeline = (
            RetrievalPipeline()
        )

        self.rag = (
            RAGChain()
        )

        self.monitoring = (
            MonitoringManager()
        )
        
    def search(
        self,
        request
    ):

        start_time = time.perf_counter()

        self.monitoring.record_metric(
            metric_name=MetricNames.SEARCH,
            metric_value=1,
            metric_type=MetricTypes.COUNTER
        )

        chunks = self.pipeline.retrieve(
            request
        )

        response = self.rag.run(
            request.question,
            chunks
        )

        elapsed_time = (
            time.perf_counter() - start_time
        )

        self.monitoring.record_metric(
            metric_name=MetricNames.SEARCH_TIME,
            metric_value=elapsed_time,
            metric_type=MetricTypes.GAUGE
        )

        return {
            "answer": response
        }