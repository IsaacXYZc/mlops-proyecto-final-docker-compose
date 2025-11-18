from typing import Union
from pydantic import BaseModel
from gemini_provider import get_response, chat

from fastapi import FastAPI, HTTPException

class Prompt(BaseModel):
    prompt: str

class chatRequest(BaseModel):
    prompt: str
    chat_history: Union[list, None] = None

app = FastAPI(title="LLM Connector", version="1.0.0")

@app.get("/")
def read_root():
    return {"Hello": "World"}
    
@app.post("/generate/")
def generate_response(request: Prompt):
    try:
        prompt = request.prompt
        if not prompt:
            raise HTTPException(status_code=400, detail="Prompt is required")
        answer = get_response(prompt)
        return {"generated_text": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error inesperado generando la respuesta.")
    
@app.post("/chat/")
def chat_endpoint(request: chatRequest):
    print(request)
    try:
        prompt = request.prompt
        if not prompt:
            raise HTTPException(status_code=400, detail="Prompt is required")

        chat_history = request.chat_history
        if chat_history is None:
            chat_history = []

        answer = chat(prompt, chat_history)
        return {"generated_text": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error inesperado en el chat.")