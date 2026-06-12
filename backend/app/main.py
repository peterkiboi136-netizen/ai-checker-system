from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from app.services.ai_detector import final_ai_score
from docx import Document
from PyPDF2 import PdfReader
from io import BytesIO

app = FastAPI(title="AI Checker System")

# ---------------- CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- HEALTH ----------------
@app.get("/api/health")
def health():
    return {"status": "backend working"}

# ---------------- TEXT EXTRACTION ----------------
def extract_pdf(file_bytes):
    reader = PdfReader(BytesIO(file_bytes))
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def extract_docx(file_bytes):
    doc = Document(BytesIO(file_bytes))
    return "\n".join([p.text for p in doc.paragraphs])

# ---------------- UPLOAD API ----------------
@app.post("/api/upload")
async def upload_file(file: UploadFile = File(...)):
    file_bytes = await file.read()
    text = ""

    # PDF
    if file.filename.endswith(".pdf"):
        text = extract_pdf(file_bytes)

    # DOCX
    elif file.filename.endswith(".docx"):
        text = extract_docx(file_bytes)

    # TXT fallback
    else:
        text = file_bytes.decode("utf-8", errors="ignore")

    # AI detection
    result = final_ai_score(text)

    return {
        "filename": file.filename,
        "extracted_text_preview": text[:600],
        **result
    }