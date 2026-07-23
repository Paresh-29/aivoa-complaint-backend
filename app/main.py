from fastapi import FastAPI

from app.api.complaint import router as complaint_router

app = FastAPI(
  title="AIVOA Complaint Backend",
  version="1.0.0",
)

app.include_router(complaint_router)

@app.get("/health")
def health():
  return {
    "status": "healthy",
    "message": "Backend is running"
  }
