from fastapi import APIRouter

from sqlalchemy.orm import Session

from app.database import SessionLocal

from app.models import User

from passlib.context import CryptContext

router = APIRouter()

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


@router.post("/register")
def register(data: dict):

    db: Session = SessionLocal()

    existing_user = db.query(User).filter(
        User.username == data["username"]
    ).first()

    if existing_user:

        return {
            "error": "Username already exists"
        }

    hashed_password = pwd_context.hash(
        data["password"]
    )

    new_user = User(
        username=data["username"],
        password=hashed_password
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    db.close()

    return {
        "message": "User registered successfully"
    }