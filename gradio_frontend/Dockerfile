FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 7860
ENV LLM_BASE_URL=http://llm_conector:8000 SKMODEL_BASE_URL=http://sklearn_model:8100 PORT=7860
CMD ["python", "app.py"]