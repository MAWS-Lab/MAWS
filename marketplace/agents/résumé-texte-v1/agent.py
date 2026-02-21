def run(input_data):
    """
    Résumé-Texte-v1 - NanashiOS
    Résume un texte long en phrases clés
    """
    text = input_data.get("text", "")
    max_sentences = input_data.get("max_sentences", 5)

    # Simulation simple (à remplacer par un vrai modèle plus tard)
    sentences = text.split(". ")
    summary = ". ".join(sentences[:max_sentences]) + "."

    key_points = [s.strip() for s in sentences[:3] if s.strip()]

    return {
        "summary": summary,
        "key_points": key_points,
        "status": "success"
    }
