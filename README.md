# 🤖 ConvoPro – Private ChatGPT Clone

ConvoPro is a private ChatGPT-style conversational AI application built with Python and Streamlit. It allows users to interact with Large Language Models (LLMs), select available models, and maintain their conversations using MongoDB.

The project is designed to support both **local LLMs through Ollama** and **cloud-based LLMs through Groq**.

## 🚀 Live Demo

🔗 https://convopro-app-chatgpt.streamlit.app/

## ✨ Features

- 💬 ChatGPT-style conversational interface
- 🤖 Multiple LLM model selection
- ☁️ Cloud-based inference using Groq
- 🖥️ Local LLM support using Ollama
- 💾 Conversation storage using MongoDB
- 📝 Automatic conversation title generation
- 📚 Chat history
- ➕ Create new conversations
- 🔄 Load previous conversations
- 🔐 API keys and database credentials stored securely using environment variables / Streamlit Secrets
- 🌐 Deployed using Streamlit Community Cloud

## 🧠 Models

### Cloud Models – Groq

The deployed application currently uses Groq-hosted models, including:

- `openai/gpt-oss-20b`
- `openai/gpt-oss-120b`

### Local Models – Ollama

The project also supports local Ollama models:

- `llama3:latest`
- `gemma2:2b`
- `mistral:7b`

Local Ollama models require Ollama to be installed and running on the local machine.

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Frontend:** Streamlit
- **LLM Framework:** LlamaIndex
- **LLM Providers:** Groq, Ollama
- **Database:** MongoDB
- **Database Driver:** PyMongo
- **Configuration:** Python Dotenv / Pydantic Settings
- **Deployment:** Streamlit Community Cloud
- **Version Control:** Git & GitHub

## 📂 Project Structure

```text
ConvoPro-Private-chatgpt/
│
├── main.py
├── requirements.txt
├── README.md
│
├── config/
│   └── settings.py
│
├── db/
│   └── conversations.py
│
├── llm_factory/
│   └── get_llm.py
│
└── services/
    ├── chat_utilities.py
    ├── get_models_list.py
    └── get_title.py
