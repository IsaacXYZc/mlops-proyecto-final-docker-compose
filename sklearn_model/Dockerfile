FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8100
ENV MLFLOW_TRACKING_URI=http://mlflow:5000 MLFLOW_EXPERIMENT_NAME=sklearn_model_experiment MODEL_NAME=salary_model
CMD ["fastapi", "run", "./app/app.py", "--port", "8100"]