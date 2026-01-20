# User Workflows: Seamless Ingestion & Semantic Search

## 1. Flow: The "Set and Forget" Ingestion (Background Sync)
**Objective:** Capture assets without interrupting the designer's creative rhythm.

1.  **Onboarding/Connection:** User connects a source (Google Drive, Dropbox, or Local "Work" Folder).
2.  **Initial Crawl:** OVERLORD scans the directory. 
3.  **Metadata Extraction:** 
    *   Extracts EXIF data, file dimensions, and color profiles.
    *   Generates low-res thumbnails for instant preview.
4.  **AI Analysis (The "Invisible" Step):**
    *   **Computer Vision:** Identifies objects (e.g., "coffee cup," "minimalist chair").
    *   **OCR:** Reads text inside images/PDFs.
    *   **Vectorization:** Creates a mathematical "semantic map" of the asset.
5.  **Completion:** Assets appear in the "Recently Added" tray with auto-generated smart tags.

## 2. Flow: The "Drop & Tag" Ingestion (Manual Upload)
**Objective:** Direct ingestion of specific assets for an active project.

1.  **Trigger:** User drags a file into the OVERLORD floating widget or dashboard.
2.  **Processing State:** UI shows a subtle pulse animation (AI is "understanding" the file).
3.  **Smart Suggestions:** System displays 3-5 high-confidence tags (e.g., #Neon, #Cyberpunk, #Typography).
4.  **Manual Override:** User can optionally add a "Client Name" or "Project ID" via a single shortcut key.
5.  **Placement:** File is indexed and instantly searchable across all connected devices.

## 3. Flow: Semantic Discovery (The "Vibe" Search)
**Objective:** Finding assets when the user doesn't remember the filename.

1.  **Input:** User types a conceptual query: *"Warm sunset vibes with negative space."*
2.  **Vector Retrieval:** Instead of looking for the word "sunset," the engine looks for images with high-warmth color values and specific compositional patterns.
3.  **Result Display:**
    *   Primary results: Direct matches.
    *   "Vibe" matches: Assets with similar emotional or stylistic signatures.
4.  **Refinement:** User clicks a "More like this" button on a result to initiate a visual similarity search.
5.  **Action:** User drags the result directly into Photoshop/Figma.