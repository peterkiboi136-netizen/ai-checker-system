from sqlalchemy import Column, Integer, String, Float, Text, DateTime
from datetime import datetime

from app.database import Base

class Document(Base):

    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String, nullable=False)

    content = Column(Text, nullable=False)

    plagiarism_score = Column(Float, default=0)

    ai_score = Column(Float, default=0)

    highlighted_pdf = Column(String, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)