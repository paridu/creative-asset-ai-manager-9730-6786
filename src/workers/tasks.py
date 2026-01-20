import celery
from PIL import Image
import torch
from sentence_transformers import SentenceTransformer
import io

app = celery.Celery('tasks', broker='redis://redis:6379/0')

# Load model once on worker startup
model = SentenceTransformer('clip-ViT-B-32')

@app.task(name="process_asset_pipeline")
def process_asset_pipeline(asset_id, file_blob):
    """
    Orchestrates the processing of a single asset.
    """
    # 1. Generate Thumbnail
    thumb_path = generate_thumbnail(asset_id, file_blob)
    
    # 2. Extract Color Palette
    colors = extract_colors(file_blob)
    
    # 3. Generate Semantic Embedding (The "Vibe" Vector)
    image = Image.open(io.BytesIO(file_blob))
    embedding = model.encode(image)
    
    # 4. Save to Database
    save_to_db(asset_id, thumb_path, colors, embedding.tolist())
    
    return {"status": "success", "asset_id": asset_id}

def generate_thumbnail(asset_id, blob):
    img = Image.open(io.BytesIO(blob))
    img.thumbnail((400, 400))
    # Logic to upload back to MinIO /thumbs/ path
    return f"thumbs/{asset_id}.webp"

def extract_colors(blob):
    # Logic to get dominant hex codes using KMeans
    return ["#FFFFFF", "#000000"]

def save_to_db(asset_id, thumb, colors, vector):
    # Logic to update PGVector and Assets table
    pass