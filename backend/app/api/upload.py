from fastapi import APIRouter, UploadFile, File
import os
import uuid
import aiofiles

router = APIRouter()

UPLOAD_DIR = "app/uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_id = str(uuid.uuid4())

    file_path = os.path.join(
        UPLOAD_DIR,
        f"{file_id}_{file.filename}"
    )

    async with aiofiles.open(file_path, "wb") as f:
        content = await file.read()
        await f.write(content)

    return {
        "file_id": file_id,
        "filename": file.filename,
        "size": len(content),
        "status": "uploaded"
    }
