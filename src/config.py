from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    REDIS_URL: str
    
    MINIO_ENDPOINT: str
    MINIO_ACCESS_KEY: str
    MINIO_SECRET_KEY: str
    MINIO_BUCKET_NAME: str = "assets"
    
    CLIP_SERVICE_URL: str = "http://localhost:8000"

    class Config:
        env_file = ".env"

settings = Settings()