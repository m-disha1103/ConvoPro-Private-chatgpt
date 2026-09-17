from groq import Groq
from config.settings import Settings

settings = Settings()

client = Groq(api_key=settings.GROQ_API_KEY)


def get_groq_client():
    return client