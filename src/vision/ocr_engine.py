import easyocr
import numpy as np
from PIL import Image

class OCREngine:
    """
    Extracts text from design assets, posters, and screenshots.
    """
    def __init__(self):
        # Supports English and Thai for the freelance market
        self.reader = easyocr.Reader(['en', 'th'])

    def extract_text(self, image: Image.Image):
        """Returns a concatenated string of all detected text and raw results."""
        img_array = np.array(image)
        results = self.reader.readtext(img_array)
        
        # Extract just the text strings
        extracted_text = " ".join([res[1] for res in results])
        
        return {
            "full_text": extracted_text,
            "raw_data": [{"text": res[1], "confidence": float(res[2])} for res in results]
        }