# Body Measurement AI API

A production-ready FastAPI application that utilizes **Segment Anything Model 2 (SAM 2)** and **MediaPipe** to extract precise body measurements (Height, Shoulder Width, Chest, Waist, and Hips) from video or image data.

## 🚀 Live Deployed Demo

The API is live and publicly accessible at:
**[https://yinkaaaaaaa-body-measurement-api.hf.space/docs](https://yinkaaaaaaa-body-measurement-api.hf.space/docs)**

*(Note: You can test the endpoint directly via the Swagger UI without installing anything locally.)*

---

## 🛠 Model Weights

Due to GitHub's file size limits, the SAM 2 model weights (`sam2_l.pt`) are not included in this repository.

**To run this project locally:**

1. Download `sam2_l.pt` (449 MB) from the **Files** tab of my [Hugging Face Space](https://huggingface.co/spaces/yinkaaaaaaa/body-measurement-api/tree/main).
2. Place the `sam2_l.pt` file in the **root directory** of this project.

---

## 💻 Setup & Running

This project is containerized with **Docker** to ensure environmental consistency and avoid Python version conflicts (specifically with MediaPipe on Python 3.13+).

### Option 1: Docker (Recommended)

*Ensure `sam2_l.pt` is in the project root before building.*

```bash
# Build the image
docker build -t body-measurement-api .

# Run the container
docker run -p 7860:7860 body-measurement-api

```

*Access the API at: `http://localhost:7860/docs`

### Option 2: Local Manual Setup

*Requires **Python 3.10** and **FFmpeg***

```bash
# Clone the repository 
git clone https://github.com/olayinkajohnsonige/body-measurement-api
cd body-measurement-api

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn app.main:app --host 0.0.0.0 --port 8000

```

---

## 📂 Project Structure

```text
.
├── app/
│   ├── api/
│   │   └── endpoints.py         # API Route definitions
│   ├── services/
│   │   ├── sam_service.py       # SAM 2 Model Logic
│   │   ├── landmark_service.py  # MediaPipe Pose Logic
│   │   └── measurement_service.py # Calculation Logic
│   ├── extraction/
│   │   └── video_utils.py       # Frame extraction logic
│   └── main.py                  # FastAPI entry point
├── Dockerfile                   # Container configuration
├── requirements.txt             # Python dependencies
├── sam2_l.pt                    # (Manual download required)
└── .gitignore                   # Excludes venv and weights

```

---

## 📡 API Usage

### **POST** `/api/v1/measure`

Estimates body measurements from a video or image file using an elliptical cross-section model.

**Parameters (Multipart/Form-Data):**

* `height`: (Number) The actual height of the person in cm (used for scaling).
* `video`: (File) An MP4/MOV video or image file.

**Sample Response:**

```json
{
  "status": "success",
  "measurements": {
    "height_cm": 165,
    "shoulder_width_cm": 75.02,
    "chest_circumference_cm": 193.26,
    "waist_circumference_cm": 172.92,
    "hip_circumference_cm": 101.66,
    "unit": "cm"
  }
}

```

---

