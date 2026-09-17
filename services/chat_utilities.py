from llm_factory.get_llm import get_groq_client


def get_answer(model_name, chat_history):
    client = get_groq_client()

    messages = [
        {
            "role": "system",
            "content": "You are a helpful chat assistant."
        }
    ]

    for msg in chat_history:
        messages.append({
            "role": msg["role"],
            "content": msg["content"]
        })

    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        temperature=0.7,
    )

    return response.choices[0].message.content