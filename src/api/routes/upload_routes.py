from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

import os

from src.orchestrator.ingestion_pipeline import (
    IngestionPipeline
)

router = APIRouter()


@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...)
):

    os.makedirs(
        "data/raw",
        exist_ok=True
    )

    file_path = (
        f"data/raw/{file.filename}"
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        content = await file.read()

        buffer.write(
            content
        )

    pipeline = (
        IngestionPipeline()
    )

    pipeline.process_file(
        file_path
    )

    return {
        "message":
            f"{file.filename} uploaded and processed successfully"
    }