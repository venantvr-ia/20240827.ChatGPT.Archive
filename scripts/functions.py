import json
import os
import re

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

api_key = os.getenv("LLM-KEY")
model = os.getenv("LLM-MODEL")

conversations_json = os.getenv("CONVERSATIONS-JSON")
static_conversations_json = os.getenv("STATIC-CONVERSATIONS-JSON")
prompts_todo_json = os.getenv("PROMPTS-TODO-JSON")
prompts_done_json = os.getenv("PROMPTS-DONE-JSON")
chat_html = os.getenv("CHAT-HTML")

llm = ChatOpenAI(
    model=model,
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=api_key,  # if you prefer to pass api key in directly instaed of using env vars
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Tu vas reformater les phrases suivantes qui correspondent à des prompts en corrigeant la ponctuation et "
            "l'orthographe et en ne touchant pas à des morceaux de code et en veillant à respecter les informations "
            "techniques. Je veux que tu produises une vraie question à partir de mon texte.",
        ),
        ("human", "{text}"),
    ]
)


def override_file(target, data):
    open(target, "w").close()
    with open(target, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def sanitize_filename(filename):
    # Remplacer les caractères non autorisés par un tiret bas
    sanitized = re.sub(r'[\/\\\:\*\?\"\<\>\|]', ' ', filename)
    # Optionnel : Trimmer les espaces au début et à la fin
    sanitized = sanitized.strip()
    # Optionnel : Limiter la longueur du nom de fichier
    max_length = 255
    if len(sanitized) > max_length:
        sanitized = sanitized[:max_length]
    return sanitized


def get_unique_filename(directory, base_filename, extension):
    # Commence par le nom de fichier de base
    filename = f"{base_filename}{extension}"
    counter = 2

    # Tant que le fichier existe, ajoute un compteur
    while os.path.exists(os.path.join(directory, filename)):
        filename = f"{base_filename} (v{counter}.0){extension}"
        counter += 1

    filename = filename.replace("  ", " ")

    return "{0}/{1}".format(directory, filename)
