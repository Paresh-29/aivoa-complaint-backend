import json

from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app.ai.groq_client import extract_complaint
from app.db.database import get_db
from app.models.complaint import Complaint
from app.pdf.parser import extract_text_from_pdf
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

    text = extract_text_from_pdf(pdf_bytes)
    result = extract_complaint(text)
    return json.loads(result)
