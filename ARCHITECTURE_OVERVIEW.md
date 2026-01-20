# System Architecture: AssetFlow AI

## 1. Input Layer (The Chaos)
- Local File System (Watchdog service)
- Cloud Storage APIs (S3, Google Drive, Dropbox)

## 2. Processing Layer (The Brain)
- **Worker 1 (Metadata):** Extract EXIF, Dimensions, File Version.
- **Worker 2 (Vision):** TensorFlow.js model for object detection & aesthetic scoring.
- **Worker 3 (Vibrant):** Color quantization to extract primary HEX codes.

## 3. Storage Layer (The Memory)
- **SQLite (Local):** Fast, relational indexing for instant queries.
- **Vector DB (ChromaDB):** For semantic "vibe-based" search.

## 4. Interaction Layer (The Interface)
- **Electron App:** Cross-platform desktop utility.
- **System Tray:** Quick-access search bar (Cmd + Shift + Space).