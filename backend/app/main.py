from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/pdf/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        return {"error": "Only PDF allowed"}

    data = await file.read()
    size_mb = len(data) / (1024 * 1024)

    if size_mb <= 1:
        price = 4
    elif size_mb <= 10:
        price = 40
    else:
        price = 500

    return {
        "filename": file.filename,
        "size_mb": round(size_mb, 2),
        "price_inr": price,
        "pay_link": "https://rzp.io/l/demo-link"
    }
