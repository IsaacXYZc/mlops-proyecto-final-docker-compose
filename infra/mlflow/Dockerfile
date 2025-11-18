FROM python:3.10-slim
WORKDIR /app
RUN pip install mlflow
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
EXPOSE 5000
ENTRYPOINT ["mlflow", "server", "--host", "0.0.0.0", "--port", "5000", "--backend-store-uri", "/mlruns", "--default-artifact-root","/mlruns", "--allowed-hosts", "*"]
VOLUME ["/mlruns"]