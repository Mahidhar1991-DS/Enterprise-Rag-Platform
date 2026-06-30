from src.background.worker import (
    BackgroundWorker
)

worker = BackgroundWorker()

worker.process_pending_jobs()

print(
    "All pending jobs processed."
)