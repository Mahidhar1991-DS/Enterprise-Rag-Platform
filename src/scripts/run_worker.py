from src.background.worker import (
    BackgroundWorker
)

worker = BackgroundWorker()

worker.start()

print(
    "All pending jobs processed."
)