def run(input_data):
    """
    Ethical-Reasoner-v1 - NanashiOS
    Aide à prendre des décisions avec un raisonnement éthique
    """
    context = input_data.get("decision_context", "")
    user_values = input_data.get("user_values", "respect, honnêteté, protection de la vie privée")

    # Simulation simple (à remplacer par vrai raisonnement éthique plus tard)
    if "mensonge" in context.lower() or "tromper" in context.lower():
        recommended_action = "Refuser la décision - Violation du principe d’honnêteté"
        ethical_score = 0.25
    else:
        recommended_action = "Accepter la décision avec vérification de l’impact sur la privacy"
        ethical_score = 0.82

    ethical_analysis = f"Analyse éthique basée sur les valeurs : {user_values}"

    return {
        "ethical_analysis": ethical_analysis,
        "recommended_action": recommended_action,
        "ethical_score": ethical_score,
        "status": "success"
    }
