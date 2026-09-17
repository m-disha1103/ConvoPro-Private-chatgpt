from config.settings import Settings
from llama_index.llms.openai import OpenAI

settings = Settings()

_current_model_name = None
_current_llm_instance = None


def get_groq_llm(model_name: str):
    global _current_model_name, _current_llm_instance

    if (
        _current_model_name == model_name
        and _current_llm_instance is not None
    ):
        return _current_llm_instance

    llm = OpenAI(
        model=model_name,
        api_key=settings.GROQ_API_KEY,
        api_base="https://api.groq.com/openai/v1",
        context_window=8192,
    )

    _current_model_name = model_name
    _current_llm_instance = llm

    return llm