FROM python:3.10-slim
RUN pip install mlflow
EXPOSE 5000
ENTRYPOINT ["mlflow", "server", "--host", "0.0.0.0", "--port", "5000", "--backend-store-uri", "/mlruns", "--allowed-hosts", "*"]
VOLUME ["/mlruns"]
# docker build -t mlflow ./infra/mlflow/Dockerfile 