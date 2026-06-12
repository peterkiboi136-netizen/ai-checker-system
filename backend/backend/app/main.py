from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.auth.routes import router as auth_router
from app.uploads.routes import router as upload_router

# ----------------------------------------
# CREATE FASTAPI APP
# ----------------------------------------
app = FastAPI(
    title="AI Checker System",
    version="1.0.0"
)

# ----------------------------------------
# ENABLE CORS
# ----------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------------------
# SERVE UPLOADS FOLDER
# ----------------------------------------
app.mount(
    "/uploads",
    StaticFiles(directory="uploads"),
    name="uploads"
)

# ----------------------------------------
# ROOT ROUTE
# ----------------------------------------
@app.get("/")
def home():

    return {
        "message": "AI Checker Backend Running"
    }

# ----------------------------------------
# HEALTH CHECK
# ----------------------------------------
@app.get("/health")
def health():

    return {
        "status": "ok"
    }

# ----------------------------------------
# REGISTER ROUTERS
# ----------------------------------------
app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"]
)

app.include_router(
    upload_router,
    prefix="/files",
    tags=["Uploads"]
)