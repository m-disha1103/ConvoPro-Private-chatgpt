from llm_factory.get_llm import get_groq_client


def get_chat_title(model, user_query):
    client = get_groq_client()

    prompt = f"""
Create a short, clear title for this user query.

Rules:
- Maximum 7 words
- No "Title:" prefix
- Keep it simple and professional

User query:
{user_query}
"""

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "You generate concise chat titles."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content.strip()