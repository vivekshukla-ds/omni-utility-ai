from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS (allow frontend access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Backend is running"}

@app.get("/health")
def health():
    return {"status": "ok"}
from fastapi import UploadFile, File
import os

@app.post("/pdf/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        return {"error": "Only PDF files allowed"}

    contents = await file.read()
    size_mb = len(contents) / (1024 * 1024)

    if size_mb <= 10:
        price = 1
    elif size_mb <= 20:
        price = 10
    else:
        price = 20

    return {
        "filename": file.filename,
        "size_mb": round(size_mb, 2),
        "price_inr": price,
        "payment_required": True
    }
# PDF UPLOAD ENDPOINT TEST
