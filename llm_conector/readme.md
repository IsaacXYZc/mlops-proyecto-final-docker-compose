# LLM Conector

## Ejecutar directamente
1. Crear un entorno virtual con el comando `python -m venv venv`
2. Activar el entorno virtual con el comando `source venv/bin/activate` (Linux/Mac) o `venv\Scripts\activate` (Windows)
3. Instalar las dependencias con el comando `pip install -r requirements.txt`
4. Iniciar la api con el comando `fastapi run ./app/app.py`
6. Configurar la variable `GEMINI_API_KEY` en un archivo `.env` en la raíz del proyecto llm_conector

## Ejecutar con Docker
1. Construir la imagen de Docker con el comando `docker build -t llm_conector .`
2. Ejecutar el contenedor con el comando `docker run -d -p 8000:8000 -e GEMINI_API_KEY=tu_api_key --name llm_conector llm_conector`. Recuerda reemplazar `tu_api_key` con tu clave real de API.

## Endpoints disponibles
- `POST /generate`: Genera texto basado en el prompt proporcionado en el cuerpo de la petición.
cuerpo de la petición en formato json:
```json
{
    "prompt": "Hola"
}
```
respuesta esperada:
```json
{
    "generated_text": "Hola, ¿qué tal?"
}
```
- `POST /chat`: Genera la siguiente respuesta basado en el mensaje y el historial de mensajes propocionado;
```json
{
  "prompt": "Bien, gracias por preguntar.",
  "chat_history": [
    {"role": "user", "content": "Hola, mi nombre es Isaac"},
    {"role": "assistant", "content": "Hola, ¿qué tal?"}
  ]
}
```
respuesta esperada:
```json
{
    "generated_text": "¿En qué puedo ayudarte hoy, Isaac?"
}
```
- `GET /docs`: Documentación automática de la API usando Swagger UI.
- `GET /`: Retorna un mensaje de bienvenida indicando que la API está funcionando correctamente.
