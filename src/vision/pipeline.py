from PIL import Image
import io
from .models import VisionModelLoader
from .color_extractor import ColorAnalyzer
from .ocr_engine import OCREngine

class AssetAnalyzer:
    """
    The main entry point for analyzing a digital asset.
    Ties together Embeddings, Tagging, Color Analysis, and OCR.
    """
    def __init__(self):
        self.models = VisionModelLoader()
        self.colors = ColorAnalyzer()
        self.ocr = OCREngine()

    def process_asset(self, file_bytes: bytes, filename: str):
        """
        Runs the full visual analysis suite on an image file.
        """
        image = Image.open(io.BytesIO(file_bytes)).convert("RGB")
        
        # 1. Generate Semantic Embedding (for Vector Search)
        embedding = self.models.generate_embeddings(image)
        
        # 2. Extract Generic Tags
        tags = self.models.get_tags(image)
        
        # 3. Extract Dominant Palette
        palette = self.colors.get_dominant_colors(image)
        
        # 4. Perform OCR
        text_data = self.ocr.extract_text(image)
        
        # 5. Determine 'Vibe' via Zero-Shot
        # (This helps freelancers find 'Minimalist', 'Grungy', or 'Corporate' assets)
        vibe_candidates = ["minimalist", "brutalist", "corporate", "vibrant", "vintage", "dark", "flat design"]
        vibe_scores = self.models.zero_shot_tags(image, vibe_candidates)
        top_vibe = vibe_scores[0][0] if vibe_scores[0][1] > 0.3 else "neutral"

        return {
            "filename": filename,
            "metadata": {
                "dimensions": image.size,
                "format": image.format,
                "mode": image.mode
            },
            "analysis": {
                "embedding": embedding,
                "tags": tags + [top_vibe],
                "palette": palette,
                "extracted_text": text_data["full_text"],
                "vibe": top_vibe
            }
        }

# Example Usage
if __name__ == "__main__":
    analyzer = AssetAnalyzer()
    # result = analyzer.process_asset(open("poster.jpg", "rb").read(), "poster.jpg")
    # print(result)