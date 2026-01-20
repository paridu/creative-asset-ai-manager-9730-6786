-- Enable the vector extension for semantic search
CREATE EXTENSION IF NOT EXISTS vector;

-- Assets Table: Core reference for files
CREATE TABLE assets (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    filename TEXT NOT NULL,
    file_path TEXT NOT NULL, -- Path in MinIO
    mime_type TEXT,
    file_size BIGINT,
    width INTEGER,
    height INTEGER,
    dominant_colors TEXT[], -- Array of Hex codes
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Metadata Table: Extracted searchable text/OCR
CREATE TABLE asset_metadata (
    asset_id UUID REFERENCES assets(id) ON DELETE CASCADE,
    extracted_text TEXT,
    ai_tags JSONB, -- AI suggested tags
    source_context TEXT -- Which project/folder it came from
);

-- Vector Table: For "Vibe" and Semantic search
CREATE TABLE asset_embeddings (
    asset_id UUID REFERENCES assets(id) ON DELETE CASCADE,
    embedding vector(512), -- Dimensions for CLIP model
    model_version TEXT
);

CREATE INDEX ON asset_embeddings USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);