# Taller final de mlops, orquestación de microservicios con docker-compose, gradio para la interfaz web
## servicios disponibles:
- Servicio de chat con modelo llm (gemini-2.0-flash) 
- Servicio de predicción de Ventas semanales de walmart (sklearn xgboost) 
- Servicio de interfaz web (Gradio para interactuar con los servicios de llm)
- Servicio de mlflow para monitoreo y logs de los modelos

## Instrucciones para correr el proyecto
1. Clonar el repositorio
```bash
git clone https://github.com/IsaacXYZc/mlops-taller-final-orquestadores.git
cd mlops-taller-final-orquestadores
```
2. En la carpeta de `llm_conector`crear un archivo .env con la variable de entorno `GEMINI_API_KEY=tu_api_key`
3. ingresar a la carpeta de infraestructura con `cd infra/`
4. construir las imagenes de los servicios 
```bash
docker-compose build.
```
### Levantar servicios 
#### (Opcion 1) con docker-compose
correr el siguiente comando para levantar los servicios 
```bash
docker-compose --build`
```

#### (Opcion 2)  con swarm-stack
correr el siguiente comando para levantar los servicios 
```bash
docker stack deploy -c swarm-stack.yml mlops_final_stack
```
Ver el estado de los servicios 
```bash
docker stack services mlops_final_stack 
```
## ruta de los servicios
- http://localhost:7860/ - frontend de la interfaz web
- http://localhost:8000/ - servidor de chat con modelo llm
- http://localhost:8100/ - servidor de predicción de ventas semanales de walmart
- http://localhost:5000/ - Mlflow interfaz
