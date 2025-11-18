import os
from openai import OpenAI
from typing import List, Union
from dotenv import load_dotenv
load_dotenv(override=True)

gemini_api_key = os.getenv("GEMINI_API_KEY")

# Config Gemini usando el endpoint OpenAI-compatible
gemini = OpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
model_name = "gemini-2.0-flash"


def get_response(prompt):
    response =  gemini.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant for answering questions."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.5,
    )
    answer = response.choices[0].message.content
    return answer

def chat(prompt: str, chat_history: Union[List, None]):
    messages = [{"role": "system", "content": "You are a helpful assistant for answering questions."}]

    if chat_history:
        for entry in chat_history:
            if isinstance(entry, dict) and "role" in entry and "content" in entry:
                messages.append({"role": entry["role"], "content": entry["content"]})
            elif isinstance(entry, (list, tuple)) and len(entry) == 2:
                user_msg, bot_msg = entry
                messages.append({"role": "user", "content": user_msg})
                messages.append({"role": "assistant", "content": bot_msg})

    messages.append({"role": "user", "content": prompt})

    response = gemini.chat.completions.create(
        model=model_name,
        messages=messages,
        temperature=0.5,
    )
    answer = response.choices[0].message.content
    return answer