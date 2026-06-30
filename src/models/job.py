from dataclasses import dataclass


@dataclass
class Job:

    job_id: str

    file_path: str

    category: str

    access_level: str

    status: str = "PENDING"