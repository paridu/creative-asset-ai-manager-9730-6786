from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
import uuid
from ...database import get_db
from ...services.storage import storage_service
from ...worker.tasks import process_asset_metadata

router = APIRouter(prefix="/assets", tags=["assets"])

@router.post("/upload")
async def upload_asset(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # 1. Create unique ID and storage key
    asset_id = str(uuid.uuid4())
    extension = file.filename.split(".")[-1]
    storage_key = f"raw/{asset_id}.{extension}"
    
    # 2. Upload to MinIO
    content = await file.read()
    storage_service.upload_file(content, storage_key, file.content_type)
    
    # 3. Initial Database Entry (Status: Processing)
    # Placeholder for SQLAlchemy Model execution
    # new_asset = Asset(id=asset_id, filename=file.filename, storage_key=storage_key...)
    # db.add(new_asset)
    # db.commit()
    
    # 4. Trigger Background Processing
    process_asset_metadata.delay(asset_id, storage_key)
    
    return {
        "asset_id": asset_id,
        "status": "upload_complete",
        "message": "Asset is being processed asynchronously."
    }

@router.get("/{asset_id}")
async def get_asset_details(asset_id: str, db: Session = Depends(get_db)):
    # Retrieve asset and return details + presigned URL
    # asset = db.query(Asset).filter(Asset.id == asset_id).first()
    # if not asset: raise HTTPException(404)
    url = storage_service.get_presigned_url(f"raw/{asset_id}") # simplified
    return {"id": asset_id, "preview_url": url}