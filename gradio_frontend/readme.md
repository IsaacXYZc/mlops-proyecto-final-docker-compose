# Frontend con Gradio

## Ejecutar directamente
1. Crear un entorno virtual con el comando `python -m venv venv`
2. Activar el entorno virtual con el comando `source venv/bin/activate` (Linux/Mac) o `venv\Scripts\activate` (Windows)
3. Instalar las dependencias con el comando `pip install -r requirements.txt`
4. Iniciar la api con el comando `python app.py`
6. (Opcional) Configurar la variables `LLM_BASE_URL`, `SKMODEL_BASE_URL` y `PORT` en un archivo `.env` en la raíz del proyecto **gradio_fronted**

## Ejecutar con Docker
1. Construir la imagen de Docker con el comando `docker build -t gradio_frontend .`
2. Ejecutar el contenedor con el comando `docker run -d -p 7860:7860 --name gradio_frontend gradio_frontend`.
