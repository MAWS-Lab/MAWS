def run(input_data):
    """
    Prompt-Optimizer-v1 - NanashiOS
    Optimise un prompt pour génération d’images
    """
    prompt = input_data.get("prompt", "")
    style = input_data.get("style", "")

    # Simulation simple (à remplacer par vrai optimisation plus tard)
    optimized = prompt.strip()
    if style:
        optimized += f", {style} style, highly detailed, 8k, masterpiece"
    else:
        optimized += ", highly detailed, cinematic lighting, 8k, masterpiece"

    improvement_score = 0.78

    return {
        "optimized_prompt": optimized,
        "improvement_score": improvement_score,
        "status": "success"
    }
