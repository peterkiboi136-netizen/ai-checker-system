from app.database.db import Base, engine
from app.models import document  # noqa: F401

def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
    print("Database created successfully")