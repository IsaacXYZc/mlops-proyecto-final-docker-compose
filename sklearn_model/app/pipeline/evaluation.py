from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

def evaluate_model(model, X_test, y_test):
    '''
    Evalúa el modelo con los datos de prueba y devuelve las métricas.
    Args:
        model: Modelo entrenado.
        X_test: Datos de prueba.
        y_test: Etiquetas reales de los datos de prueba.
    Returns:
        mae: Error absoluto medio.
        mse: Error cuadrático medio.
        rmse: Raíz del error cuadrático medio.
        r2: Coeficiente de determinación R².
    '''
    y_pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    return mae, mse, rmse, r2