from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os

from app.api.routes import router as api_routher

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
FRONTEND_DIR = os.path.join(PROJECT_ROOT,"frontend")

app = FastAPI(title="Skin Lesion Diagnosis API")

app.add_middleware(
    CORSMiddleware,
    allow_origin=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(api_routher,prefix="/api/v1")

if os.path.isdir(FRONTEND_DIR):
    app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

@app.get("/")
async def read_root():
    index_path = os.path.join(FRONTEND_DIR,"index.html")
    if os.path.isfile(index_path):
        return FileResponse(index_path)
    return {"status": "Server live. Awaiting index.html in the frontend folder."}
