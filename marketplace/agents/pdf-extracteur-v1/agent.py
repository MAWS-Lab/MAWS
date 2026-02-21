def run(input_data):
    """
    PDF-Extracteur-v1 - NanashiOS
    Extrait texte, tables et images d’un PDF (simulation simple)
    """
    pdf_path = input_data.get("pdf_file", "document.pdf")

    # Simulation simple (à remplacer par vrai traitement PDF plus tard)
    text = "Texte extrait du PDF : Ceci est un exemple de contenu extrait."
    tables = [{"table_1": "Données simulées"}]
    images = ["image_1_extrait.png"]

    return {
        "text": text,
        "tables": tables,
        "images": images,
        "status": "success"
    }
