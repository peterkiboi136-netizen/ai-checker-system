from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String,
        unique=True
    )

    password = Column(String)


class Report(Base):

    __tablename__ = "reports"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    filename = Column(String)

    ai_score = Column(Integer)

    risk_level = Column(String)

    word_count = Column(Integer)

    sentence_count = Column(Integer)

    ai_report = Column(String)

    similarity_report = Column(String)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )