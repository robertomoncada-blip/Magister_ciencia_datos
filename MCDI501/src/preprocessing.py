"""
Módulo encargado del preprocesamiento y transformación de datos.

Reúne las funciones necesarias para limpiar, codificar, construir
variables, normalizar y validar el conjunto de datos, exponiéndolas
a través de un pipeline unificado listo para alimentar el modelo.
"""


import pandas as pd

def limpiar_datos(df: pd.DataFrame) -> pd.DataFrame:
    # crear copia para no modificar original
    df = df.copy()
    # eliminar duplicados
    df = df.drop_duplicates()

    # imputación Detecta columnas numéricas 
    num_cols = df.select_dtypes(include=['float64','int64']).columns
    #Reemplaza los valores NaN por la mediana de cada columna
    df[num_cols] = df[num_cols].fillna(df[num_cols].median())

    cat_cols = df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    return df

def encoding_categorico(df):
    """Aplica encoding ordinal a Education_Level y Risk_Category, y OHE a Job_Title."""
    # Education_Level (ordinal)
    if 'Education_Level' in df.columns:
        education_map = {
            'High School': 0,
            "Bachelor's": 1,
            "Master's": 2,
            'PhD': 3
        }
        df['Education_Level'] = df['Education_Level'].map(education_map)

    # Risk_Category (ordinal)
    if 'Risk_Category' in df.columns:
        risk_map = {
            'Low': 0,
            'Medium': 1,
            'High': 2
        }
        df['Risk_Category'] = df['Risk_Category'].map(risk_map)

    # Job_Title (OneHot)
    if 'Job_Title' in df.columns:
        df = pd.get_dummies(df, columns=['Job_Title'], drop_first=False)

    return df

def crear_features(df):
    """
    Feature Engineering:
    - Índice de habilidades
    - Target binaria (High_Risk)
    """

    # 1. Skill Index
    skill_cols = [col for col in df.columns if col.startswith('Skill_')]
    if len(skill_cols) > 0:
        df['Skill_Index'] = df[skill_cols].mean(axis=1)

    # 2. Variable target
    if 'Automation_Probability_2030' in df.columns:
        df['High_Risk'] = (df['Automation_Probability_2030'] > 0.7).astype(int)

    return df


def normalizar_datos(df):
    """Escala columnas numéricas continuas al rango [0, 1] con MinMaxScaler."""
    from sklearn.preprocessing import MinMaxScaler

    cols_a_normalizar = ['Average_Salary', 'Years_Experience', 'Tech_Growth_Factor',
                         'Education_Level', 'Risk_Category']
    cols_presentes = [c for c in cols_a_normalizar if c in df.columns]

    scaler = MinMaxScaler()
    df[cols_presentes] = scaler.fit_transform(df[cols_presentes])

    return df


def validar_datos(df):
    """
    Validaciones de calidad de datos
    """

    assert len(df) > 0, "❌ DataFrame vacío"

    # Nulos
    assert df.isnull().sum().sum() == 0, "❌ Existen valores nulos"

    # Duplicados
    assert df.duplicated().sum() == 0, "❌ Existen duplicados"

    print("✅ Validaciones OK")


def preprocessing_pipeline(df):
    """
    Pipeline completo de preprocessing
    """

    print("🔹 Iniciando preprocessing...")

    df = limpiar_datos(df)
    print("Limpieza completada")

    df = encoding_categorico(df)
    print("Encoding completado")

    df = crear_features(df)
    print("Features creadas")

    df = normalizar_datos(df)
    print("Normalización completada")

    validar_datos(df)

    print("Preprocessing finalizado")

    return df


def exportar_dataset(df, path='../data/processed/AI_Impact_on_Jobs_2030_clean.csv'):
    """
    Exporta dataset procesado y muestra resumen
    """

    import os
    os.makedirs('../data/processed', exist_ok=True)

    df.to_csv(path, index=False)

    print("\n=== DATASET FINAL ===")
    print("Shape:", df.shape)
    print("\nColumnas:", df.columns.tolist())
    print("\nTipos:\n", df.dtypes)
    print("\nNulos:\n", df.isnull().sum())

    print(f"\n✅ Dataset exportado en: {path}")