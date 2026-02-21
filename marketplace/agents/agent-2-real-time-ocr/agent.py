def run(input_data):
    """
    Real-time OCR Agent - NanashiOS
    Extrait du texte en temps réel à partir d’une image
    """
    image_path = input_data.get("image", "frame.jpg")

    # Simulation simple (à remplacer par vrai pytesseract + OpenCV plus tard)
    extracted_text = "Texte extrait en temps réel : NanashiOS est un framework souverain."
    confidence = 0.87

    return {
        "extracted_text": extracted_text,
        "confidence": confidence,
        "status": "success"
    }
