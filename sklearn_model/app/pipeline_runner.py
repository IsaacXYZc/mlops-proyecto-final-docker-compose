import mlflow
import mlflow.sklearn
from pipeline.preprocessing import preprocess_data
from pipeline.training import train_model
from pipeline.evaluation import evaluate_model
from typing import Dict

def run_pipeline(model_name: str, params: Dict = None):
    """
    Ejecuta: preprocess -> train -> evaluate y guarda el registro en MLflow.
    """
    if params is None:
        params = {"n_estimators": 100, "learning_rate": 0.1, "random_state": 42}

    X_train, X_test, y_train, y_test, preprocessor = preprocess_data()

    with mlflow.start_run():
        model = train_model(X_train, y_train, preprocessor, params)

        mae, mse, rmse, r2 = evaluate_model(model, X_test, y_test)

        mlflow.log_params(params)
        mlflow.log_metric("MAE", mae)
        mlflow.log_metric("MSE", mse)
        mlflow.log_metric("RMSE", rmse)
        mlflow.log_metric("R2", r2)

        mlflow.sklearn.log_model(model, name=model_name, registered_model_name=model_name)
