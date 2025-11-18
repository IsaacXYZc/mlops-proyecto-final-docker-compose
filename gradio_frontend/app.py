import gradio as gr
import requests
import os
import dotenv
dotenv.load_dotenv()

llm_base_url = os.getenv("LLM_BASE_URL", "http://llm_conector:8000")
skmodel_base_url = os.getenv("SKMODEL_BASE_URL", "http://sklearn_model:8100")

def check_status(base_url):
    try:
        r = requests.get(f"{base_url}/")
        if r.status_code == 200:
            return "🟢 Online"
        return "🟡 No OK"
    except:
        return "🔴 Offline"

def chat_with_llm(message, chat_history):
    try:
        response = requests.post(f"{llm_base_url}/chat/", json={"prompt": message, "chat_history": chat_history})
        response.raise_for_status()
        answer = response.json().get("generated_text", "Sin respuesta")
        chat_history.append((message, answer))
        return "", chat_history
    except Exception as e:
        raise gr.Error(f"Error al llamar a la API del LLM: {e}")

with gr.Blocks(title="mlops final", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# Proyecto final MLOps")
    gr.Markdown("## LLM + ML + CNN:")

    with gr.Tab("Chat con LLM"):
        with gr.Row():
            gr.Markdown("### LLM Connector con gemini 2.0")
            with gr.Row(scale=1):
                status_llm = gr.Markdown("**Estado del LLM:** " + check_status(llm_base_url))
                status_button = gr.Button("Actualizar estado", size="sm")

        chat = gr.Chatbot()
        msg = gr.Textbox(
            label="Mensaje",    
            placeholder="Escribe tu mensaje aqui...", 
            submit_btn=True
        )
        msg.submit(chat_with_llm, [msg, chat],[msg, chat])


if __name__ == "__main__":
    demo.launch(server_port=7860)
