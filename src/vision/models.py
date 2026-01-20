import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel, pipeline

class VisionModelLoader:
    """
    Loads and provides interfaces for Computer Vision models.
    Uses CLIP for semantic embeddings and zero-shot tagging,
    and a standard pipeline for general object classification.
    """
    def __init__(self, device="cuda" if torch.cuda.is_available() else "cpu"):
        self.device = device
        print(f"Initializing Vision Models on {self.device}...")
        
        # CLIP for Semantic Search & Vibe Analysis
        self.clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(self.device)
        self.clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
        
        # General Image Classification for Auto-Tagging
        self.classifier = pipeline("image-classification", model="google/vit-base-patch16-224", device=0 if device=="cuda" else -1)

    def generate_embeddings(self, image: Image.Image):
        """Generates a 512-dimension vector embedding of the image."""
        inputs = self.clip_processor(images=image, return_tensors="pt").to(self.device)
        with torch.no_grad():
            image_features = self.clip_model.get_image_features(**inputs)
        return image_features.cpu().numpy().tolist()[0]

    def get_tags(self, image: Image.Image, top_k=5):
        """Predicts standard object tags."""
        predictions = self.classifier(image)
        return [p['label'] for p in predictions[:top_k]]

    def zero_shot_tags(self, image: Image.Image, candidate_labels: list):
        """Custom tagging based on a list of creative keywords."""
        inputs = self.clip_processor(text=candidate_labels, images=image, return_tensors="pt", padding=True).to(self.device)
        with torch.no_grad():
            outputs = self.clip_model(**inputs)
            logits_per_image = outputs.logits_per_image
            probs = logits_per_image.softmax(dim=1)
        
        results = zip(candidate_labels, probs[0].cpu().numpy())
        return sorted(results, key=lambda x: x[1], reverse=True)