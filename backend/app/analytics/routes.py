from fastapi import APIRouter, Depends
from app.database import SessionLocal
from app.models.document import Document

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/stats")
def get_stats(db=Depends(get_db)):

    docs = db.query(Document).all()

    data = []

    for doc in docs:

        data.append({
            "name": doc.filename,
            "similarity": doc.similarity_score
        })

    return data


@router.get("/history")
def get_history(db=Depends(get_db)):

    docs = db.query(Document).all()

    history = []

    for doc in docs:

        history.append({

            "filename": doc.filename,

            "plagiarism_score": doc.similarity_score,

            "ai_score": doc.ai_score,

            "upload_date": doc.created_at.strftime("%Y-%m-%d %H:%M")
        })

    return history