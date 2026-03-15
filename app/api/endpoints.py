from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.services.sam_service import SAMService
from app.services.landmark_service import LandmarkService
from app.services.measurement_service import MeasurementService
from app.extraction import video_utils
import shutil
import os

router = APIRouter()

# Initialize tools
sam_tool = SAMService()
landmark_tool = LandmarkService()

@router.post("/measure")
async def estimate_measurements(height: float = Form(...), video: UploadFile = File(...)):
    temp_path = f"temp/{video.filename}"
    if not os.path.exists("temp"): os.makedirs("temp")

    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(video.file, buffer)

    try:
        # 1. Get Frames & Landmarks
        output_folder = "temp_frames"
        os.makedirs(output_folder, exist_ok=True)
        frames = video_utils.extract_frames(temp_path, output_folder)
        landmarks = landmark_tool.get_landmarks(frames[0])
        
        if not landmarks:
            raise HTTPException(status_code=400, detail="Could not detect person")

        # 2. Get Measurements
        measurer = MeasurementService(user_height_cm=height)
        results = measurer.get_all_measurements(landmarks)

        return {"status": "success", "measurements": results}
    finally:
        if os.path.exists(temp_path): os.remove(temp_path)