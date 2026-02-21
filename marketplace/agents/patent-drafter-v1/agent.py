def run(input_data):
    """
    Patent-Drafter-v1 - NanashiOS
    Rédige une description de brevet conforme OEB/INPI
    """
    description = input_data.get("invention_description", "Aucune description fournie.")
    claims = input_data.get("claims", "")

    draft = f"""DESCRIPTION DE BREVET (OEB / INPI)

État de la technique :
{description}

Revendications principales :
{claims or 'À rédiger selon les règles OEB/INPI'}

Nouveauté et activité inventive :
À évaluer selon les critères de brevetabilité.

Note : Ce draft est généré automatiquement par NanashiOS. Il doit être revu par un professionnel du droit."""

    patentability_score = 0.65  # Exemple simple

    return {
        "draft": draft,
        "patentability_score": patentability_score,
        "status": "success"
    }
