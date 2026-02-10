from fastapi import FastAPI

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

# Allow frontend (Vercel) to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later we can restrict
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}

