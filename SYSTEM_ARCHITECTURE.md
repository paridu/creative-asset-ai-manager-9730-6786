# OVERLORD: Scalable Asset Processing & Storage Architecture

## 1. High-Level Overview
The system follows a **Decoupled Event-Driven Architecture**. This ensures that heavy AI processing (OCR, Embedding, Thumbnailing) does not block the user interface and can scale horizontally based on the volume of files ingested.

## 2. Component Stack
- **API Gateway:** FastAPI (High performance, async support).
- **Task Queue:** Celery + Redis (Managing background processing).
- **Blob Storage:** MinIO (S3 compatible, local-first but cloud-ready).
- **Metadata Database:** PostgreSQL + PGVector (Relational data + Vector embeddings).
- **Search Engine:** Meilisearch (For lightning-fast keyword search) + PGVector (For semantic/vibe search).
- **Processing Workers:** Python-based workers utilizing:
    - `Pillow/Wand`: Image manipulation.
    - `OpenCV`: Visual analysis.
    - `Sentence-Transformers`: Multi-modal embeddings (CLIP).

## 3. Data Flow
1. **Ingestion:** User uploads or syncs a folder. API generates a `PendingAsset` record and stores the raw file in MinIO.
2. **Messaging:** API pushes a `PROCESS_ASSET` event to Redis.
3. **Processing Pipeline:**
    - Task A: Generate dynamic thumbnails (WebP).
    - Task B: Extract Metadata (EXIF, Dimensions, Color Palette).
    - Task C: Semantic Analysis (Generate CLIP vectors for "vibe" search).
    - Task D: OCR (Extract text from layers/images).
4. **Indexing:** Data is committed to PostgreSQL and the Vector index.
5. **Ready:** The asset is marked as `Active` and becomes searchable.