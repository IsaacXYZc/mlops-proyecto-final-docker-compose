import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

def preprocess_data(path="./data/Walmart_Sales.csv"):
    '''
    Preprocesa los datos para el entrenamiento y la evaluación del modelo.
    Args:
        path: Ruta al archivo CSV con los datos.
    Returns:
        X_train: Datos de entrenamiento.
        X_test: Datos de prueba.
        y_train: Etiquetas de entrenamiento.
        y_test: Etiquetas de prueba.
        preprocessor: Objeto de preprocesamiento (ColumnTransformer).
    '''
    df = pd.read_csv(path)

    # Eliminar columnas duplicadas
    df = df.drop_duplicates()

    # Definir columna objetivo
    target_col = "Weekly_Sales"

    # Definir variables categóricas y numéricas 
    cat_cols = df.select_dtypes(include=["object"]).columns.tolist()
    num_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    num_cols.remove(target_col)  # eliminar la columna objetivo de las características numéricas


    # Dividir datos en características y objetivo
    X = df.drop(columns=[target_col])
    y = df[target_col]

    # Definir preprocesador
    preprocessor = ColumnTransformer(
            transformers=[
                ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols),
                ("num", "passthrough", num_cols)
            ]
        )

    # Dividir datos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test, preprocessor