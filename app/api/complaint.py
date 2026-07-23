import json
from io import BytesIO

from fastapi import APIRouter, Depends, File, UploadFile
from pypdf import PdfReader
from sqlalchemy.orm import Session

from app.ai.groq_client import extract_complaint
from app.db.database import get_db
from app.models.complaint import Complaint
from app.schemas.complaint import ComplaintCreate, ComplaintResponse

router = APIRouter(
    prefix="/api/v1/complaints",
    tags=["Complaints"],
)


@router.get("/")
def get_complaints(db: Session = Depends(get_db)):
    complaints = db.query(Complaint).all()
    return complaints


@router.post("/", response_model=ComplaintResponse)
def create_complaint(complaint: ComplaintCreate, db: Session = Depends(get_db)):
    db_complaint = Complaint(**complaint.model_dump())
    db.add(db_complaint)
    db.commit()
    db.refresh(db_complaint)
    return db_complaint


@router.post("/upload")
async def upload_complaint(file: UploadFile = File(...)):
    pdf_bytes = await file.read()

    render = PdfReader(BytesIO(pdf_bytes))

    text = ""

    for page in render.pages:
        extracted_text = page.extract_text()

        if extracted_text:
            text += extracted_text + "\n"

    result = extract_complaint(text)
    return json.loads(result)


@router.get("/ai-test")
def ai_test():
    return {
        "response": test_groq(),
    }
