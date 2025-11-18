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
    mlflow.set_tracking_uri(tracking_uri)
    mlflow.set_experiment(experiment_name)
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
        model = mlflow.sklearn.load_model(f"models:/{model_name}/latest")
        return model
    except Exception as exc:
        return None

