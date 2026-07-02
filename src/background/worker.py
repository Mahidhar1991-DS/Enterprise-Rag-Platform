import time
from src.background.job_manager import (
    JobManager
)

from src.orchestrator.ingestion_pipeline import (
    IngestionPipeline
)

from src.constants.job_status import (
    JobStatus
)

from src.configs.worker_config import (
    WORKER_POLL_INTERVAL
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
        ) -> None:

        jobs = (
            self.job_manager
            .get_pending_jobs()
        )

        for job in jobs:

            try:

                self.job_manager.update_status(
                    job["job_id"],
                    JobStatus.PROCESSING
                )

                self.pipeline.process_file(
                    file_path=job["file_path"],
                    category=job["category"],
                    access_level=job["access_level"]
                )

                self.job_manager.update_status(
                    job["job_id"],
                    JobStatus.COMPLETED
                )

            except Exception as e:

                print(
                        f"Job Processing Failed: {e}"
                    )

                self.job_manager.update_status(
                    job["job_id"],
                    JobStatus.FAILED
                )
                
                
    def start(
        self
    ) -> None:

        print(
            "Background Worker Started..."
        )

        while True:

            self.process_pending_jobs()

            time.sleep(WORKER_POLL_INTERVAL)