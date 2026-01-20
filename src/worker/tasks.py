import httpx
from .celery_app import celery_app
from ..database import SessionLocal
from ..services.storage import storage_service
from ..config import settings
# Assuming models are imported from a models module
# from ..models import Asset

@celery_app.task(name="process_asset_metadata")
def process_asset_metadata(asset_id: str, storage_key: str):
    """
    Background task to:
    1. Extract metadata
    2. Generate Embeddings via Vision Service
    3. Update PostgreSQL/PGVector
    """
    db = SessionLocal()
    try:
        # 1. Get Presigned URL for the vision service to download
        file_url = storage_service.get_presigned_url(storage_key)
        
        # 2. Call Vision Service (CLIP/OCR)
        # This calls the service defined in the previous "Computer Vision Models" step
        with httpx.Client() as client:
            response = client.post(
                f"{settings.CLIP_SERVICE_URL}/analyze",
                json={"file_url": file_url}
            )
            analysis = response.json()

        # 3. Update Database with tags and embeddings
        # db.execute(update_query, {"id": asset_id, "embedding": analysis['embedding'], "tags": analysis['tags']})
        # db.commit()
        
        print(f"Asset {asset_id} processed successfully with tags: {analysis.get('tags')}")
        
    except Exception as e:
        print(f"Error processing asset {asset_id}: {str(e)}")
    finally:
        db.close()