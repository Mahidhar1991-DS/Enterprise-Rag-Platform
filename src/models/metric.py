from dataclasses import dataclass


@dataclass
class Metric:

    metric_id: str

    metric_name: str

    metric_value: float

    metric_type: str