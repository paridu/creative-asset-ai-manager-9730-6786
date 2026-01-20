# Specialized image for AI/CV processing
FROM python:3.10-slim

WORKDIR /app

# Install system dependencies for OpenCV and AI models
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements-cv.txt .
RUN pip install --no-cache-dir -r requirements-cv.txt

COPY src/vision ./src/vision
COPY src/config.py ./src/

# Start Celery worker for processing assets
CMD ["celery", "-A", "src.vision.worker", "worker", "--loglevel=info", "-Q", "vision_tasks"]