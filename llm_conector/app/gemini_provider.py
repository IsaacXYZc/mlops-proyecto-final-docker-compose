import os
from openai import OpenAI

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

def chat(prompt, chat_history):
    messages = [{"role": "system", "content": "You are a helpful assistant for answering questions."}]
    for user_msg, bot_msg in chat_history:
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

if __name__ == "__main__":
    print(get_response("¿Qué es la inteligencia artificial?"))