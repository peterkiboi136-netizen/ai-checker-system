from jose import jwt
from jose import JWTError

from passlib.context import CryptContext

SECRET_KEY = "supersecretkey"

ALGORITHM = "HS256"

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

# ----------------------------------------
# HASH PASSWORD
# ----------------------------------------
def hash_password(password):

    return pwd_context.hash(password)

# ----------------------------------------
# VERIFY PASSWORD
# ----------------------------------------
def verify_password(
    plain_password,
    hashed_password
):

    return pwd_context.verify(
        plain_password,
        hashed_password
    )

# ----------------------------------------
# CREATE TOKEN
# ----------------------------------------
def create_access_token(data):

    return jwt.encode(
        data,
        SECRET_KEY,
        algorithm=ALGORITHM
    )