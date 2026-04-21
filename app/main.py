from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router as api_routher

app = FastAPI(
    title="Skin Lesion Diagnosis API",
    description="Backend API for deep learning based skin lesion classification",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origin=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_routher, prefix="/api/v1")


@app.get("/")
async def read_root():

    return {
        "status": "Server live.",
        "message": "Skin Lesion API is running. Ready for inference requests.",
    }
