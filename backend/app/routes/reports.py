from fastapi import APIRouter

from sqlalchemy.orm import Session

from app.database import SessionLocal

from app.models import Report

router = APIRouter()


@router.get("/reports")
def get_reports():

    db: Session = SessionLocal()

    reports = db.query(Report).all()

    results = []

    for report in reports:

        results.append({

            "id": report.id,

            "filename": report.filename,

            "ai_score": report.ai_score,

            "risk_level": report.risk_level,

            "word_count": report.word_count,

            "sentence_count": report.sentence_count,

            "ai_report": report.ai_report,

            "similarity_report":
                report.similarity_report
        })

    db.close()

    return results