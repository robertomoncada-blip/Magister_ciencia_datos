"""Módulo de transformadores POO para el pipeline de la Fase 3.

Implementa la jerarquía de clases Transformador (ABC) → subclases concretas
y la clase Pipeline que las orquesta por composición y polimorfismo.

Pilares POO aplicados
---------------------
Encapsulamiento : cada clase protege su estado con atributos protegidos (_col, _cols)
                  y expone una única interfaz pública: aplicar(df).
Herencia        : ImputarMediana, ImputarModa, EscalarMinMax y EscalarZScore
                  heredan de Transformador y están obligadas a implementar aplicar().
Polimorfismo    : Pipeline.ejecutar() itera las etapas llamando etapa.aplicar(df)
                  sin conocer la clase concreta; cada subclase responde de forma diferente.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

import pandas as pd
from sklearn.preprocessing import MinMaxScaler


# ---------------------------------------------------------------------------
# Clase base abstracta — contrato común
# ---------------------------------------------------------------------------

class Transformador(ABC):
    """Contrato común para todas las transformaciones del pipeline.

    Toda subclase debe implementar aplicar(df) y retornar un DataFrame
    transformado (copia independiente; nunca muta el original).
    """

    @abstractmethod
    def aplicar(self, df: pd.DataFrame) -> pd.DataFrame:
        """Aplica la transformación y retorna el DataFrame resultante."""
        ...

    def __repr__(self) -> str:
        return f"{type(self).__name__}()"


# ---------------------------------------------------------------------------
# Subclases concretas — herencia + polimorfismo
# ---------------------------------------------------------------------------

class ImputarMediana(Transformador):
    """Imputa valores nulos de una columna numérica con la mediana.

    La mediana es robusta ante outliers; se elige sobre la media cuando
    la distribución de la columna presenta valores extremos.

    Parameters
    ----------
    columna : str
        Nombre de la columna a imputar.
    """

    def __init__(self, columna: str) -> None:
        self._columna = columna

    def aplicar(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        if self._columna in df.columns:
            mediana = df[self._columna].median()
            df[self._columna] = df[self._columna].fillna(mediana)
        return df

    def __repr__(self) -> str:
        return f"ImputarMediana(columna='{self._columna}')"


class ImputarModa(Transformador):
    """Imputa valores nulos de una columna categórica con la moda.

    Parameters
    ----------
    columna : str
        Nombre de la columna a imputar.
    """

    def __init__(self, columna: str) -> None:
        self._columna = columna

    def aplicar(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        if self._columna in df.columns and df[self._columna].isnull().any():
            moda = df[self._columna].mode()[0]
            df[self._columna] = df[self._columna].fillna(moda)
        return df

    def __repr__(self) -> str:
        return f"ImputarModa(columna='{self._columna}')"


class EscalarMinMax(Transformador):
    """Escala columnas numéricas al rango [0, 1] con MinMaxScaler.

    Se prefiere sobre z-score cuando se necesita un rango acotado y el
    dataset no tiene outliers extremos que distorsionen el escalado.

    Parameters
    ----------
    columnas : list[str]
        Nombres de las columnas a escalar.
    """

    def __init__(self, columnas: list) -> None:
        self._columnas = columnas

    def aplicar(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        cols_presentes = [c for c in self._columnas if c in df.columns]
        if cols_presentes:
            scaler = MinMaxScaler()
            df[cols_presentes] = scaler.fit_transform(df[cols_presentes])
        return df

    def __repr__(self) -> str:
        return f"EscalarMinMax(columnas={self._columnas})"


class EscalarZScore(Transformador):
    """Estandariza columnas numéricas (media 0, desviación estándar 1).

    Se prefiere sobre MinMax cuando el algoritmo posterior asume distribución
    normal o cuando hay outliers que conviene mantener en escala relativa.

    Parameters
    ----------
    columnas : list[str]
        Nombres de las columnas a estandarizar.
    """

    def __init__(self, columnas: list) -> None:
        self._columnas = columnas

    def aplicar(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        for col in self._columnas:
            if col in df.columns:
                std = df[col].std()
                if std > 0:
                    df[col] = (df[col] - df[col].mean()) / std
        return df

    def __repr__(self) -> str:
        return f"EscalarZScore(columnas={self._columnas})"


# ---------------------------------------------------------------------------
# Pipeline — composición y polimorfismo
# ---------------------------------------------------------------------------

class Pipeline:
    """Orquesta una secuencia de Transformadores por composición.

    No hereda de Transformador; en cambio, lo *tiene* (composición):
    almacena una lista de etapas y las ejecuta en orden invocando
    etapa.aplicar(df) sin conocer la clase concreta (polimorfismo).

    Parameters
    ----------
    etapas : list[Transformador]
        Secuencia de transformaciones a aplicar en orden.
    """

    def __init__(self, etapas: list) -> None:
        self._etapas = list(etapas)

    def ejecutar(self, df: pd.DataFrame) -> pd.DataFrame:
        """Aplica cada etapa en orden y retorna el DataFrame transformado."""
        for etapa in self._etapas:
            df = etapa.aplicar(df)   # polimorfismo: misma llamada, distintos comportamientos
        return df

    def __repr__(self) -> str:
        nombres = [repr(e) for e in self._etapas]
        return "Pipeline([\n  " + ",\n  ".join(nombres) + "\n])"
