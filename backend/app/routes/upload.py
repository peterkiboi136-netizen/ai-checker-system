from fastapi import APIRouter, UploadFile, File
import shutil
import os
from uuid import uuid4

router = APIRouter()

UPLOAD_DIR = "app/uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    ext = file.filename.split(".")[-1]

    unique_name = f"{uuid4()}.{ext}"

    file_path = os.path.join(UPLOAD_DIR, unique_name)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "filename": unique_name,
        "original_name": file.filename,
        "status": "uploaded"
    }