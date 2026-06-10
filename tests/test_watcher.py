from src.sync.document_watcher import (
    DocumentWatcher
)

watcher = DocumentWatcher()

watcher.scan_folder(
    "data/raw"
)