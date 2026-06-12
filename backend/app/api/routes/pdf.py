from fastapi import APIRouter

router = APIRouter(
    prefix="/pdf",
    tags=["PDF"]
)


@router.get("/")
def pdf_status():
    return {
        "status": "PDF router active"
    }