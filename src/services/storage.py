import boto3
from botocore.client import Config
from ..config import settings

class StorageService:
    def __init__(self):
        self.s3 = boto3.client(
            's3',
            endpoint_url=f"http://{settings.MINIO_ENDPOINT}",
            aws_access_key_id=settings.MINIO_ACCESS_KEY,
            aws_secret_access_key=settings.MINIO_SECRET_KEY,
            config=Config(signature_version='s3v4'),
            region_name='us-east-1'
        )
        self.bucket = settings.MINIO_BUCKET_NAME

    def upload_file(self, file_data, object_name, content_type):
        self.s3.put_object(
            Bucket=self.bucket,
            Key=object_name,
            Body=file_data,
            ContentType=content_type
        )
        return object_name

    def get_presigned_url(self, object_name, expiration=3600):
        return self.s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': self.bucket, 'Key': object_name},
            ExpiresIn=expiration
        )

storage_service = StorageService()