from dataclasses import dataclass

from src.constants.job_status import (
    JobStatus
)

from src.constants.access_levels import (
    AccessLevel
)


@dataclass
class Job:

    job_id: str

    file_path: str

    category: str

    access_level: str = AccessLevel.PUBLIC

    status: str = JobStatus.PENDING