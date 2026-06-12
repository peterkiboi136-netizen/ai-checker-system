from fastapi import APIRouter, HTTPException
from app.core.security import hash_password, verify_password, create_access_token
from app.db.users import users_db

router = APIRouter(prefix="/auth", tags=["Auth"])


# --------------------
# REGISTER
# --------------------
@router.post("/register")
def register(email: str, password: str):

    if email in users_db:
        raise HTTPException(status_code=400, detail="User already exists")

    users_db[email] = {
        "email": email,
        "password": hash_password(password)
    }

    return {"message": "User registered successfully"}


# --------------------
# LOGIN
# --------------------
@router.post("/login")
def login(email: str, password: str):

    user = users_db.get(email)

    if not user:
        raise HTTPException(status_code=400, detail="User not found")

    if not verify_password(password, user["password"]):
        raise HTTPException(status_code=400, detail="Invalid password")

    token = create_access_token({"sub": email})

    return {"access_token": token, "token_type": "bearer"}