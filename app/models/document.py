from sqlalchemy import Column, Integer, String, Float, Text
from app.database.db import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    content = Column(Text)

    ai_score = Column(Float, default=0)
    plagiarism_score = Column(Float, default=0)