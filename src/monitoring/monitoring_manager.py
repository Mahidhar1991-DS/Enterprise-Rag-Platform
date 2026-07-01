import uuid

from src.models.metric import (
    Metric
)

from src.database.metric_repository import (
    MetricRepository
)


class MonitoringManager:

    def __init__(self):

        self.metric_repo = (
            MetricRepository()
        )

    def record_metric(
        self,
        metric_name: str,
        metric_value: float,
        metric_type: str
    ):

        metric = Metric(
            metric_id=str(uuid.uuid4()),
            metric_name=metric_name,
            metric_value=metric_value,
            metric_type=metric_type
        )

        self.metric_repo.create_metric(
            metric
        )

    def get_all_metrics(
        self
    ):

        return (
            self.metric_repo
            .get_all_metrics()
        )

    def get_metric(
        self,
        metric_name: str
    ):

        return (
            self.metric_repo
            .get_metric(
                metric_name
            )
        )