from fastapi import FastAPI
from app.routes import audio

app = FastAPI(
    title="AcousticSpace API",
    version="1.0.0",
    description="Backend API for Deepfake Audio Detection"
)

app.include_router(audio.router)

@app.get("/")
def root():
    return {
        "message": "AcousticSpace Backend Running Successfully"
    }