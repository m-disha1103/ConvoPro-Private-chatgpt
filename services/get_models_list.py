import os


def get_ollama_models_list():
    models = os.getenv(
        "GROQ_MODELS",
        "llama-3.3-70b-versatile"
    )

    return [
        model.strip()
        for model in models.split(",")
        if model.strip()
    ]