# Use a version where MediaPipe is stable
FROM python:3.10-slim

# Install system dependencies for OpenCV and MediaPipe
# Switched libgl1-mesa-glx to libgl1 for newer compatibility
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything else into /app
COPY . .

# Run the app - using port 7860 for Hugging Face
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]