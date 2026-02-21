def run(input_data):
    """
    Image-Caption-v1 - NanashiOS
    Génère une description textuelle d’une image (simulation simple)
    """
    image_path = input_data.get("image", "image.jpg")

    # Simulation simple (à remplacer par vrai modèle BLIP plus tard)
    caption = "Une image montrant un paysage cyberpunk avec des néons cyan et purple, style NanashiOS."
    keywords = ["cyberpunk", "néons", "paysage", "IA", "souverain"]

    return {
        "caption": caption,
        "keywords": keywords,
        "status": "success"
    }
