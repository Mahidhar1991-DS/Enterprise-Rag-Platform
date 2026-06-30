import uuid

from src.models.job import (
    Job
)

from src.database.job_repository import (
    JobRepository
)


class JobManager:

    def __init__(self):

        self.job_repo = (
            JobRepository()
        )

    def create_job(
        self,
        file_path: str,
        category: str,
        access_level: str
    ):

        job = Job(
            job_id=str(uuid.uuid4()),
            file_path=file_path,
            category=category,
            access_level=access_level
        )

        self.job_repo.create_job(
            job
        )

        return job

    def get_job(
        self,
        job_id: str
    ):

        return (
            self.job_repo.get_job(
                job_id
            )
        )

    def update_status(
        self,
        job_id: str,
        status: str
    ):

        self.job_repo.update_status(
            job_id,
            status
        )

    def get_pending_jobs(
        self
    ):

        return (
            self.job_repo
            .get_pending_jobs()
        )