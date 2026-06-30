from src.background.job_manager import (
    JobManager
)

from src.orchestrator.ingestion_pipeline import (
    IngestionPipeline
)


class BackgroundWorker:

    def __init__(self):

        self.job_manager = (
            JobManager()
        )

        self.pipeline = (
            IngestionPipeline()
        )

    def process_pending_jobs(
        self
    ):

        jobs = (
            self.job_manager
            .get_pending_jobs()
        )

        for job in jobs:

            try:

                self.job_manager.update_status(
                    job["job_id"],
                    "PROCESSING"
                )

                self.pipeline.process_file(
                    file_path=job["file_path"],
                    category=job["category"],
                    access_level=job["access_level"]
                )

                self.job_manager.update_status(
                    job["job_id"],
                    "COMPLETED"
                )

            except Exception as e:

                print(e)

                self.job_manager.update_status(
                    job["job_id"],
                    "FAILED"
                )