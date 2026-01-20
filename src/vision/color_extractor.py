import cv2
import numpy as np
from sklearn.cluster import KMeans
from PIL import Image

class ColorAnalyzer:
    """
    Extracts dominant color palettes and identifies color profiles.
    """
    @staticmethod
    def get_dominant_colors(image: Image.Image, k=5):
        """
        Uses KMeans clustering to find the dominant colors in the image.
        Returns a list of HEX codes.
        """
        # Convert PIL to OpenCV format
        img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        img = cv2.resize(img, (150, 150), interpolation=cv2.INTER_AREA)
        img = img.reshape((img.shape[0] * img.shape[1], 3))

        clt = KMeans(n_clusters=k, n_init=10)
        clt.fit(img)

        hist = ColorAnalyzer._centroid_histogram(clt)
        colors = ColorAnalyzer._sort_colors(hist, clt.cluster_centers_)
        
        return [ColorAnalyzer._rgb_to_hex(color) for color in colors]

    @staticmethod
    def _centroid_histogram(clt):
        num_labels = np.arange(0, len(np.unique(clt.labels_)) + 1)
        (hist, _) = np.histogram(clt.labels_, bins=num_labels)
        hist = hist.astype("float")
        hist /= hist.sum()
        return hist

    @staticmethod
    def _sort_colors(hist, centroids):
        # Sort colors based on frequency
        aux = sorted(zip(hist, centroids), key=lambda x: x[0], reverse=True)
        return [color[1] for color in aux]

    @staticmethod
    def _rgb_to_hex(color):
        return "#{:02x}{:02x}{:02x}".format(int(color[2]), int(color[1]), int(color[0]))