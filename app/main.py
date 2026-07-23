from fastapi import FastAPI

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
