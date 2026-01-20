-- Seed a test project
INSERT INTO projects (name, description, client_name) 
VALUES ('Brand Refresh 2024', 'Internal rebranding assets', 'Self');

-- Seed a dummy asset
INSERT INTO assets (filename, original_path, storage_key, file_size, mime_type, extension)
VALUES ('hero_shot.jpg', '/Users/designer/Downloads/hero_shot.jpg', 'assets/2024/hero_shot.jpg', 2048000, 'image/jpeg', 'jpg');

-- Link asset to project
INSERT INTO project_assets (project_id, asset_id)
SELECT p.id, a.id FROM projects p, assets a LIMIT 1;

-- Add AI Metadata
INSERT INTO asset_metadata (asset_id, dominant_colors, ocr_content, ai_description)
SELECT id, ARRAY['#F3F3F3', '#000000'], 'FRESH COFFEE', 'A minimalist photo of a coffee cup on a white desk'
FROM assets LIMIT 1;

-- Add dummy embedding (3 dimensions for example, real is 512)
-- Note: This is for demonstration; actual vectors are inserted via Python/ORM
-- INSERT INTO asset_embeddings (asset_id, embedding)
-- SELECT id, '[0.1, 0.2, 0.3, ...]' FROM assets LIMIT 1;