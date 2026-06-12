from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

import os
import shutil
import uuid

from app.ai.detector import check_plagiarism
from app.pdf.highlighter import highlight_pdf

router = APIRouter()

# ----------------------------------------
# CREATE FOLDERS
# ----------------------------------------
UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

# ----------------------------------------
# UPLOAD ROUTE
# ----------------------------------------
@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...)
):

    try:

        # ----------------------------------------
        # UNIQUE FILE NAME
        # ----------------------------------------
        unique_filename = (
            str(uuid.uuid4())
            + "_"
            + file.filename
        )

        file_path = os.path.join(
            UPLOAD_DIR,
            unique_filename
        )

        # ----------------------------------------
        # SAVE FILE
        # ----------------------------------------
        with open(file_path, "wb") as buffer:

            shutil.copyfileobj(
                file.file,
                buffer
            )

        # ----------------------------------------
        # RUN DETECTOR
        # ----------------------------------------
        results = check_plagiarism(
            file_path
        )

        plagiarism_score = results.get(
            "plagiarism_score",
            0
        )

        ai_score = results.get(
            "ai_score",
            0
        )

        matches = results.get(
            "matches",
            []
        )

        chunk_matches = results.get(
            "chunk_matches",
            []
        )

        internet_matches = results.get(
            "internet_matches",
            []
        )

        suspicious_sentences = []

        for match in chunk_matches:

            suspicious_sentences.append(
                match.get(
                    "input_chunk",
                    ""
                )
            )

        # ----------------------------------------
        # HIGHLIGHT PDF
        # ----------------------------------------
        highlighted_filename = (
            "highlighted_"
            + unique_filename
        )

        highlighted_pdf_path = os.path.join(
            UPLOAD_DIR,
            highlighted_filename
        )

        highlight_pdf(
            file_path,
            suspicious_sentences,
            highlighted_pdf_path
        )

        # ----------------------------------------
        # RESPONSE
        # ----------------------------------------
        return {

            "filename": unique_filename,

            "plagiarism_score":
                plagiarism_score,

            "ai_score":
                ai_score,

            "matches":
                matches,

            "chunk_matches":
                chunk_matches,

            "internet_matches":
                internet_matches,

            "highlighted_pdf":
                highlighted_filename
        }

    except Exception as e:

        return {
            "error": str(e)
        }