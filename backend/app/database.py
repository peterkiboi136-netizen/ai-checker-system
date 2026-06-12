from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

DATABASE_URL = (
    "postgresql://postgres:password@db:5432/aichecker"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# ----------------------------------------
# DB SESSION
# ----------------------------------------
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()