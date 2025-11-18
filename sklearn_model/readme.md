# Sklearn model
1. Crear un entorno virtual con el comando `python -m venv venv`
2. Activar el entorno virtual con el comando `source venv/bin/activate` (Linux/Mac) o `venv\Scripts\activate` (Windows)
3. Instalar las dependencias con el comando `pip install -r requirements.txt`
4. (Opcional) Ejecutar el script del pipeline con el comando `python pipeline/main.py`
5. Iniciar la api con el comando `fastapi run ./app/app.py`

## Endpoints disponibles
- `POST /predict/`: Realiza una predicción utilizando el modelo entrenado. Se debe enviar un JSON con las características necesarias para la predicción.
```json
{
   "Store": 1,
   "Date": "05-02-2010",
   "Holiday_Flag": 0,
   "Temperature": 42.31,
   "Fuel_Price": 2.572,
   "CPI": 211.0963582,
   "Unemployment": 8.106
 }
```
respuesta esperada:
```json
{
  "prediction": [1643000.67]
}
```
- `GET /`: Retorna un mensaje de bienvenida indicando que la API está funcionando correctamente.

- `GET /reload_model/`: Fuerza la recarga del modelo desde MLflow.

- `GET /docs`: Documentación automática de la API generada por FastAPI.

- `GET /test_prediction/`: Endpoint de prueba para verificar que la predicción funciona correctamente con datos de ejemplo.

- `GET /get_model_info/`: Retorna información sobre el modelo actualmente cargado.

