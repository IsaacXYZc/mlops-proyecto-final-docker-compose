from xgboost import XGBRegressor
from sklearn.pipeline import Pipeline


def train_model(X_train, y_train, preprocessor, params=None):
    '''
    Entrena un modelo XGBoost con el preprocesador dado y los datos de entrenamiento.
    Args:
        X_train: Datos de entrenamiento.
        y_train: Etiquetas de entrenamiento.
        preprocessor: Objeto de preprocesamiento (ColumnTransformer).
        params: Diccionario de hiperparámetros para XGBRegressor.
    Returns:
        model: Modelo entrenado (Pipeline con preprocesador y XGBRegressor).
    '''

    if params is None:
        params = {"n_estimators": 100, "learning_rate": 0.1, "random_state": 42}

    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('model', XGBRegressor(**params))
    ])

    model.fit(X_train, y_train)

    return model