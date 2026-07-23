from fastapi import FastAPI
from sqlalchemy import text

from app.db.database import engine

app = FastAPI(
  title="AIVOA Complaint Backend",
  version="1.0.0",
)

@app.get("/health")
def health():
  return {
    "status": "healthy",
    "message": "Backend is running"
  }

@app.on_event("startup")
def startup():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    print("Database connected successfully!")
