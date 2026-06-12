from fastapi import APIRouter

from sqlalchemy.orm import Session

from app.database import SessionLocal

from app.models import User

from passlib.context import CryptContext

from jose import jwt

from datetime import datetime, timedelta

router = APIRouter()

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

SECRET_KEY = "MY_SECRET_KEY"

ALGORITHM = "HS256"


# =========================
# REGISTER
# =========================

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


# =========================
# LOGIN
# =========================

@router.post("/login")
def login(data: dict):

    db: Session = SessionLocal()

    user = db.query(User).filter(
        User.username == data["username"]
    ).first()

    if not user:

        return {
            "error": "Invalid username"
        }

    valid_password = pwd_context.verify(
        data["password"],
        user.password
    )

    if not valid_password:

        return {
            "error": "Invalid password"
        }

    payload = {

        "sub": user.username,

        "exp": datetime.utcnow() +
        timedelta(hours=24)
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    db.close()

    return {

        "message": "Login successful",

        "token": token
    }