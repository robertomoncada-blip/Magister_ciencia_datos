import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import os


class Preprocesador:
    """Pipeline de preprocesamiento POO para el dataset AI Impact on Jobs 2030.

    Encapsula las transformaciones desarrolladas en la Fase 2 (funciones en
    preprocessing.py) dentro de una clase reutilizable con estado propio.

    Atributos
    ---------
    ruta : str
        Ruta al archivo CSV de entrada.
    dataset : pd.DataFrame o None
        DataFrame activo; None hasta que se invoque cargar_datos().
    """

    def __init__(self, dataset=None, ruta=None):
        self.dataset = dataset
        self.ruta = ruta

    # ------------------------------------------------------------------
    # II.a  Carga de datos
    # ------------------------------------------------------------------

    def cargar_datos(self) -> pd.DataFrame:
        """Carga el CSV indicado en self.ruta y lo almacena en self.dataset.

        Returns
        -------
        pd.DataFrame
            Dataset original sin transformar.

        Raises
        ------
        FileNotFoundError
            Si la ruta no existe.
        ValueError
            Si el archivo no es un CSV válido.
        """
        if not os.path.exists(self.ruta):
            raise FileNotFoundError(f"Archivo no encontrado: {self.ruta}")
        try:
            self.dataset = pd.read_csv(self.ruta)
        except Exception as exc:
            raise ValueError(f"Error al leer el CSV: {exc}") from exc
        return self.dataset

    # ------------------------------------------------------------------
    # II.b  Limpieza
    # ------------------------------------------------------------------

    def limpiar_datos(self, df: pd.DataFrame) -> pd.DataFrame:
        """Elimina duplicados e imputa nulos.

        Estrategia:
        - Numéricos  → mediana (robusta ante outliers).
        - Categóricos → moda.

        Parameters
        ----------
        df : pd.DataFrame
            DataFrame de entrada.

        Returns
        -------
        pd.DataFrame
            DataFrame limpio (copia independiente).
        """
        df = df.copy()
        df = df.drop_duplicates()

        num_cols = df.select_dtypes(include=["float64", "int64"]).columns
        df[num_cols] = df[num_cols].fillna(df[num_cols].median())

        cat_cols = df.select_dtypes(include=["object"]).columns
        for col in cat_cols:
            df[col] = df[col].fillna(df[col].mode()[0])

        return df

    # ------------------------------------------------------------------
    # II.b  Encoding
    # ------------------------------------------------------------------

    def encoding_categorico(self, df: pd.DataFrame) -> pd.DataFrame:
        """Aplica encoding ordinal a Education_Level y Risk_Category, OHE a Job_Title.

        Parameters
        ----------
        df : pd.DataFrame

        Returns
        -------
        pd.DataFrame
        """
        df = df.copy()

        if "Education_Level" in df.columns:
            education_map = {
                "High School": 0,
                "Bachelor's": 1,
                "Master's": 2,
                "PhD": 3,
            }
            df["Education_Level"] = df["Education_Level"].map(education_map)

        if "Risk_Category" in df.columns:
            risk_map = {"Low": 0, "Medium": 1, "High": 2}
            df["Risk_Category"] = df["Risk_Category"].map(risk_map)

        if "Job_Title" in df.columns:
            df = pd.get_dummies(df, columns=["Job_Title"], drop_first=False)

        return df

    # ------------------------------------------------------------------
    # II.b  Feature engineering
    # ------------------------------------------------------------------

    def crear_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Crea Skill_Index y la variable objetivo binaria High_Risk.

        Parameters
        ----------
        df : pd.DataFrame

        Returns
        -------
        pd.DataFrame
        """
        df = df.copy()

        skill_cols = [c for c in df.columns if c.startswith("Skill_")]
        if skill_cols:
            df["Skill_Index"] = df[skill_cols].mean(axis=1)

        if "Automation_Probability_2030" in df.columns:
            df["High_Risk"] = (df["Automation_Probability_2030"] > 0.7).astype(int)

        return df

    # ------------------------------------------------------------------
    # II.b  Normalización
    # ------------------------------------------------------------------

    def normalizar_datos(self, df: pd.DataFrame) -> pd.DataFrame:
        """Escala variables continuas al rango [0, 1] con MinMaxScaler.

        Solo se normalizan las columnas que no están ya en [0, 1].

        Parameters
        ----------
        df : pd.DataFrame

        Returns
        -------
        pd.DataFrame
        """
        df = df.copy()
        cols_a_normalizar = [
            "Average_Salary",
            "Years_Experience",
            "Tech_Growth_Factor",
            "Education_Level",
            "Risk_Category",
        ]
        cols_presentes = [c for c in cols_a_normalizar if c in df.columns]
        scaler = MinMaxScaler()
        df[cols_presentes] = scaler.fit_transform(df[cols_presentes])
        return df

    # ------------------------------------------------------------------
    # II.c  Validación
    # ------------------------------------------------------------------

    def validar_datos(self, df: pd.DataFrame) -> bool:
        """Verifica integridad básica del DataFrame procesado.

        Parameters
        ----------
        df : pd.DataFrame

        Returns
        -------
        bool
            True si todas las validaciones pasan.

        Raises
        ------
        AssertionError
            Si alguna condición de calidad no se cumple.
        """
        assert len(df) > 0, "DataFrame vacío"
        assert df.isnull().sum().sum() == 0, "Existen valores nulos"
        assert df.duplicated().sum() == 0, "Existen duplicados"
        print("Validaciones OK: sin nulos, sin duplicados, filas > 0")
        return True

    # ------------------------------------------------------------------
    # Pipeline completo
    # ------------------------------------------------------------------

    def pipeline_completo(self) -> pd.DataFrame:
        """Ejecuta la secuencia completa de preprocesamiento.

        Returns
        -------
        pd.DataFrame
            Dataset procesado (3.000 × 39): limpio, codificado, con features y normalizado.
        """
        df = self.cargar_datos()
        df = self.limpiar_datos(df)
        df = self.encoding_categorico(df)
        df = self.crear_features(df)
        df = self.normalizar_datos(df)
        self.validar_datos(df)
        self.dataset = df
        return df

    # ------------------------------------------------------------------
    # Exportación
    # ------------------------------------------------------------------

    def exportar_dataset(
        self,
        df: pd.DataFrame,
        path: str = "../data/processed/AI_Impact_on_Jobs_2030_clean.csv",
    ) -> None:
        """Exporta el DataFrame a CSV.

        Parameters
        ----------
        df : pd.DataFrame
        path : str
            Ruta de destino.
        """
        os.makedirs(os.path.dirname(path), exist_ok=True)
        df.to_csv(path, index=False)
        print(f"Dataset exportado en: {path}  ({df.shape[0]} filas × {df.shape[1]} columnas)")
