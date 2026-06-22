"""
Módulo encargado del proceso de entrenamiento del modelo predictivo.

Contiene la función entrenar_modelo, responsable de separar los datos
en particiones de entrenamiento y prueba, ajustar un clasificador
basado en Random Forest y devolver los resultados listos para evaluar.
"""

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def entrenar_modelo(df):
    # Se excluyen las columnas que filtran el objetivo: High_Risk se deriva de
    # Automation_Probability_2030 (umbral 0.7) y Risk_Category replica esos mismos
    # intervalos. Conservarlas produciría target leakage.
    features = df.drop(
        ['High_Risk', 'Automation_Probability_2030', 'Risk_Category'],
        axis=1,
    )
    target = df['High_Risk']

    X_train, X_test, y_train, y_test = train_test_split(
        features, target, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    return model, X_test, y_test
