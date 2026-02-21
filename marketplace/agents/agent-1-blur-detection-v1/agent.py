import cv2
import numpy as np

def run(input_data):
    """
    Blur Detection Agent - NanashiOS
    Détecte le flou sur une image
    """
    # Simulation simple (à remplacer par vrai traitement OpenCV plus tard)
    blur_score = 0.35  # Exemple : 0 = très net, 1 = très flou
    is_blurry = blur_score > 0.6

    return {
        "blur_score": blur_score,
        "is_blurry": is_blurry,
        "status": "success"
    }
