import mlflow
import mlflow.sklearn

def configure_mlflow(tracking_uri: str, experiment_name: str):
    """
    Configura MLflow: tracking uri y experimento.
    Args:
        tracking_uri (str): URI del servidor de tracking de MLflow.
        experiment_name (str): Nombre del experimento en MLflow.
    Returns:
        None
    """
    print(f"Configurando MLflow con URI: {tracking_uri} y experimento: {experiment_name}", flush=True)
    mlflow.set_tracking_uri(tracking_uri)
    print(f"Tracking URI configurada a: {mlflow.get_tracking_uri()}", flush=True)
    mlflow.set_experiment(experiment_name)
    print(f"Experimento configurado a: {experiment_name}", flush=True)
    return

def get_model(model_name: str):
    """
    Intenta cargar el último modelo registrado. Devuelve None si no existe o falla la carga.
    Args:
        model_name (str): Nombre del modelo registrado en MLflow.
    Returns:
        model: Modelo cargado o None si no se pudo cargar.
    """
    try:
        print(f"Intentando cargar el modelo '{model_name}' desde MLflow...", flush=True)
        model = mlflow.sklearn.load_model(f"models:/{model_name}/latest")
        print(f"Modelo '{model_name}' cargado exitosamente desde MLflow.", flush=True)
        return model
    except Exception as exc:
        print(f"No se pudo cargar el modelo '{model_name}': {exc}", flush=True)
        return None

