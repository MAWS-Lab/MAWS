def run(input_data):
    """
    Traduction-v1 - NanashiOS
    Traduit un texte dans la langue cible (simulation simple)
    """
    text = input_data.get("text", "")
    target_lang = input_data.get("target_lang", "en").lower()

    # Simulation simple (à remplacer par un vrai modèle plus tard)
    if target_lang == "en":
        translated = text + " (traduit en anglais)"
    elif target_lang == "es":
        translated = text + " (traduit en espagnol)"
    elif target_lang == "de":
        translated = text + " (traduit en allemand)"
    else:
        translated = text + f" (traduit en {target_lang})"

    return {
        "translated_text": translated,
        "status": "success"
    }
