-- Create an HNSW index for high-speed semantic search
-- HNSW (Hierarchical Navigable Small World) is much faster than IVFFlat for large datasets
-- We use cosine distance (vector_cosine_ops) as it is standard for CLIP embeddings

CREATE INDEX ON asset_embeddings USING hnsw (embedding vector_cosine_ops)
WITH (m = 16, ef_construction = 64);

-- Comment: m = 16 (max connections per layer), ef_construction = 64 (accuracy vs speed trade-off)

-- Example Query: Semantic Search for "Minimalist coffee shop vibe"
-- SELECT asset_id, 1 - (embedding <=> '[0.12, -0.05, ...]') AS similarity
-- FROM asset_embeddings
-- ORDER BY similarity DESC
-- LIMIT 20;

-- Example Query: Search by Dominant Color (Simple matching)
-- SELECT asset_id FROM asset_metadata WHERE '#FFFFFF' = ANY(dominant_colors);