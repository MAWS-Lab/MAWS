def run(input_data):
    task = input_data.get("task", "Aucune tâche spécifiée.")
    language = input_data.get("language", "python").lower()

    if language == "python":
        code = f'''# Code généré par NanashiOS Code-Writer-v1
# Tâche : {task}

def main():
    print("Code généré par NanashiOS")
    # TODO: Implémenter la tâche : {task}
    pass

if __name__ == "__main__":
    main()
'''
    elif language == "javascript":
        code = f'''// Code généré par NanashiOS Code-Writer-v1
// Tâche : {task}

function main() {{
    console.log("Code généré par NanashiOS");
    // TODO: Implémenter la tâche : {task}
}}

main();
'''
    else:
        code = f"# Langage {language} non supporté par Code-Writer-v1\\n# Tâche : {task}"

    explanation = f"Code généré pour : {task} ({language})"

    return {{
        "code": code,
        "explanation": explanation,
        "language": language,
        "status": "success"
    }}
