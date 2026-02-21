def run(input_data):
    """
    Energy-Optimizer-v1 - NanashiOS
    Optimise la consommation énergétique des agents
    """
    current_usage = input_data.get("current_usage", 100.0)
    process_list = input_data.get("process_list", [])

    # Simulation simple (à remplacer par vraie optimisation plus tard)
    if current_usage > 70:
        optimization_plan = "Réduction de la fréquence CPU + mise en veille de processus non essentiels"
        estimated_savings = 35.0
    else:
        optimization_plan = "Aucune optimisation nécessaire"
        estimated_savings = 5.0

    return {
        "optimization_plan": optimization_plan,
        "estimated_savings": estimated_savings,
        "status": "success"
    }
