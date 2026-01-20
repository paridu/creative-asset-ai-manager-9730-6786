# Computer Vision Strategy for OVERLORD

## Model Selection Logic
1. **CLIP (Contrastive Language-Image Pre-training):** Used as the backbone. Unlike standard classifiers, CLIP understands concepts. This allows the "Semantic Search" feature where a user can search for "A cozy cafe layout" and find relevant assets even if they aren't tagged with those specific words.
2. **ViT (Vision Transformer):** Used for standard object classification to provide baseline tags (e.g., "chair", "webpage", "logo").
3. **EasyOCR:** Chosen for its balance between speed and accuracy, specifically supporting multi-language environments common in design.
4. **KMeans:** Provides a deterministic way to extract the actual color palette used in the asset, which is stored for "Search by Color" functionality.

## Data Flow
1. **Ingestion:** File is uploaded/synced.
2. **Worker:** Celery worker picks up the job and calls `AssetAnalyzer.process_asset`.
3. **Vector Store:** The 512-d embedding is saved into `pgvector` in PostgreSQL.
4. **Search:** When a user types a query, the query is embedded via CLIP and a cosine similarity search is performed in the DB.