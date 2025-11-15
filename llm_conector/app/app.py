from typing import Union
from gemini_provider import get_response

from fastapi import FastAPI

app = FastAPI(title="LLM Connector", version="1.0.0")



@app.get("/")
def read_root():
    return {"Hello": "World"}
    
@app.get("/generate/")
def generate_response(prompt: str):
    answer = get_response(prompt)
    return {"response": answer}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}