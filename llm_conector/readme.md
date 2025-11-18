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
- `POST /generate/?prompt=your_prompt`: Genera texto basado en el prompt proporcionado.
- `GET /docs`: Documentación automática de la API usando Swagger UI.
- `GET /`: Retorna un mensaje de bienvenida indicando que la API está funcionando correctamente.
