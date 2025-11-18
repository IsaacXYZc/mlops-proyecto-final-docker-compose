# Taller final de mlops, orquestación de microservicios con docker-compose, gradio para la interfaz web
##servicios disponibles:
- Servicio de chat con modelo llm (gemini-2.0-flash) 
- Servicio de predicción de Ventas semanales de walmart (sklearn xgboost) 
- Servicio de interfaz web (Gradio para interactuar con los servicios de llm)

## Instrucciones para correr el proyecto
1. Clonar el repositorio
```bash
git clone https://github.com/IsaacXYZc/mlops-taller-final-orquestadores.git
cd mlops-taller-final-orquestadores
```
2. ingresar a la carpeta `infra/`
3. correr el siguiente comando para levantar los servicios `docker-compose up --build`
4. Abrir el navegador y dirigirse a la siguiente URL: `http://localhost:7860`