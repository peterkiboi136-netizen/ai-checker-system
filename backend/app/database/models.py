from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from .db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String, unique=True, index=True)

    password_hash = Column(String)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, nullable=True)

    filename = Column(String)

    original_pdf = Column(String)

    highlighted_pdf = Column(String)

    ai_score = Column(Float)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )