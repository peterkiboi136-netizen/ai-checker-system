from fastapi import APIRouter, UploadFile, File

from sqlalchemy.orm import Session

from app.database import SessionLocal

from app.models import Report

from app.services.ai_scoring import analyze_text

from app.services.text_extractor import (
    extract_text_from_docx,
    extract_text_from_pdf
)

from app.services.report_generator import (
    generate_reports
)

import shutil
import os

router = APIRouter()

os.makedirs("app/uploads", exist_ok=True)

os.makedirs(
    "app/generated_reports",
    exist_ok=True
)


@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):

    try:

        file_location = f"app/uploads/{file.filename}"

        # Save uploaded file
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        extracted_text = ""

        # DOCX support
        if file.filename.endswith(".docx"):

            extracted_text = extract_text_from_docx(
                file_location
            )

        # PDF support
        elif file.filename.endswith(".pdf"):

            extracted_text = extract_text_from_pdf(
                file_location
            )

        else:

            return {
                "error": "Unsupported file type"
            }

        # Analyze text
        result = analyze_text(extracted_text)

        # Generate reports
        reports = generate_reports(
            file.filename,
            result,
            extracted_text
        )

        # Save to database
        db: Session = SessionLocal()

        new_report = Report(

            filename=file.filename,

            ai_score=result["ai_score"],

            risk_level=result["risk_level"],

            word_count=result["word_count"],

            sentence_count=result[
                "sentence_count"
            ],

            ai_report=reports["ai_report"],

            similarity_report=reports[
                "similarity_report"
            ]
        )

        db.add(new_report)

        db.commit()

        db.refresh(new_report)

        db.close()

        return {

            "filename": file.filename,

            "extracted_characters": len(
                extracted_text
            ),

            "ai_score": result["ai_score"],

            "risk_level": result["risk_level"],

            "word_count": result["word_count"],

            "sentence_count": result[
                "sentence_count"
            ],

            "ai_report": reports[
                "ai_report"
            ],

            "similarity_report": reports[
                "similarity_report"
            ]
        }

    except Exception as e:

        return {
            "error": str(e)
        }