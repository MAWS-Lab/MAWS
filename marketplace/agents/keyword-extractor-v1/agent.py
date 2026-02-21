def run(input_data):
    """
    Keyword-Extractor-v1 - NanashiOS
    Extrait mots-clés et entités nommées d’un texte
    """
    text = input_data.get("text", "")

    # Simulation simple (à remplacer par spaCy/KeyBERT plus tard)
    keywords = ["IA", "souveraineté", "privacy", "agent", "NanashiOS"]
    entities = [
        {"type": "ORG", "value": "NanashiOS-Lab"},
        {"type": "TECH", "value": "BSL 1.1"}
    ]

    return {
        "keywords": keywords,
        "entities": entities,
        "status": "success"
    }
