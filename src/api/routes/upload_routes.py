from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Form

import os

from src.background.job_manager import (
    JobManager
)

router = APIRouter()

job_manager = JobManager()


@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    category: str = Form(...),
    access_level: str = Form("PUBLIC")
):

    os.makedirs(
        "data/raw",
        exist_ok=True
    )

    file_path = f"data/raw/{file.filename}"

    with open(
        file_path,
        "wb"
    ) as buffer:

        content = await file.read()

        buffer.write(content)

    job = job_manager.create_job(
        file_path=file_path,
        category=category,
        access_level=access_level.upper()
    )

    return {
        "message": "Upload accepted",
        "job_id": job.job_id,
        "status": job.status
    }