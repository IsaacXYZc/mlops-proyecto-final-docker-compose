import gradio as gr
import requests
import os
import dotenv
dotenv.load_dotenv()

llm_base_url = os.getenv("LLM_BASE_URL", "http://localhost:8000")
skmodel_base_url = os.getenv("SKMODEL_BASE_URL", "http://localhost:8100")
port = int(os.getenv("PORT", 7860))

skmodel_features = [
    "Store", "Day", "Month", "Year", "Holiday_Flag", "Temperature", 
    "Fuel_Price", "CPI", "Unemployment"
]

def check_status(base_url):
    try:
        r = requests.get(f"{base_url}/")
        if r.status_code == 200:
            return "🟢 Online"
        return "🟡 No OK"
    except:
        return "🔴 Offline"
    
def individual_prediction(*features):
    try:
        response = requests.post(f"{skmodel_base_url}/predict/", json={
            "Store": features[0],
            "Date": f"{int(features[1]):02d}-{int(features[2]):02d}-{int(features[3])}",
            "Holiday_Flag": features[4],
            "Temperature": features[5],
            "Fuel_Price": features[6],
            "CPI": features[7],
            "Unemployment": features[8]
        })
        response.raise_for_status()
        prediction = response.json().get("prediction", "No prediction found")
        return f"Predicción: {prediction}"
    except Exception as e:
        raise gr.Error("Error al llamar a la API del modelo sklearn: {e}")

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
            with gr.Row(scale=2):
                gr.Markdown("### LLM Connector con gemini 2.0")
            with gr.Row(scale=1):
                status_label = gr.Markdown("**Estado del LLM:** ")
                status = gr.Markdown(""+check_status(llm_base_url))
                status_button = gr.Button("Actualizar estado", size="sm")

                status_button.click(
                    fn=lambda: check_status(llm_base_url),
                    inputs=[],
                    outputs=[status]
                )
        chat = gr.Chatbot(type="messages")
        msg = gr.Textbox(
            label="Mensaje",    
            placeholder="Escribe tu mensaje aqui...", 
            submit_btn=True
        )
        msg.submit(chat_with_llm, [msg, chat],[msg, chat])
    with gr.Tab("Predicción con modelo sklearn"):
        with gr.Row():
            with gr.Row(scale=2):
                gr.Markdown("### Predicción de ventas semanales en USD de Walmart")
            with gr.Row(scale=1):
                status_label = gr.Markdown("**Estado de modelo sklearn:** ")
                status = gr.Markdown(""+check_status(skmodel_base_url))
                status_button = gr.Button("Actualizar estado", size="sm")

                status_button.click(
                    fn=lambda: check_status(skmodel_base_url),
                    inputs=[],
                    outputs=[status]
                )
        with gr.Row(scale=1):
            features = [gr.Number(label=f, scale=0, min_width=160) for f in skmodel_features]
        
        with gr.Column(scale=1):
            output = gr.Textbox(label="Predicción", placeholder="Resultado aqui...", lines=2, interactive=False)
        
        button_predict = gr.Button("Predecir")
        button_predict.click(individual_prediction, inputs=[*features], outputs=output)
        gr.Markdown("#### Significado de las variables")
        gr.Markdown("""
        - Store: Identificador de la tienda. 
        Valores normales [1 - 45].
        - Date: Fecha de la observación.
        Valor en formato MM-DD-AAAA.
        - Holiday_Flag: Indicador de si la fecha es un feriado (1) o no (0).
        Valores posibles: 0 o 1.
        - Temperature: Temperatura en grados Fahrenheit de la región.
        Valores típicos entre -2.06 y 100.
        - Fuel_Price: Precio del combustible en la región.
        Valores típicos entre 2.47 y 4.47.
        - CPI: Índice de Precios al Consumidor.
        Valores típicos entre 126 y 227.
        - Unemployment: Tasa de desempleo de la región.
        Valores típicos entre 3.88 y 14.3.
        """)
        
if __name__ == "__main__":
    print(f"Gradio frontend running on port {port}", flush=True)
    demo.launch(server_name="0.0.0.0", server_port=port)
