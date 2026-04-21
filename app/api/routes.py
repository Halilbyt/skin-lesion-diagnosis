import io

from fastapi import APIRouter, File, HTTPException, UploadFile
from PIL import Image

router = APIRouter()


@router.post("/predict")
async def predict_lesion(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image.")
    try:
        iamge_data = await file.read()
        image = Image.open(io.BytesIO(iamge_data)).convert("RGB")

        # ML Pipline

        return {
            "filename": file.filename,
            "status": "success",
            "prediction": "xxxx-placeholder",
            "confidence": 0.94,  # another placeholder
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing image: {str(e)}")
