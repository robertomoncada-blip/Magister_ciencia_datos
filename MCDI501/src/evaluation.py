
"""
Módulo asociado a la evaluación de modelos de clasificación.

Actualmente expone la función evaluar_modelo, que calcula y muestra
métricas de rendimiento como accuracy y el reporte de clasificación
completo, permitiendo analizar el desempeño del modelo sobre el
conjunto de prueba.
"""


from sklearn.metrics import classification_report, accuracy_score

def evaluar_modelo(model, X_test, y_test):
    y_pred = model.predict(X_test)

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("\nReporte:\n", classification_report(y_test, y_pred))