# Análisis exploratorio reproducible del dataset Titanic

Proyecto de la asignatura **MCDI503 – Exploración Inteligente para la Ciencia de Datos**. Fase 1: implementación inicial del análisis exploratorio de datos (EDA) reproducible.

**Curso:** MCDI503 - Exploración Inteligente para la Ciencia de Datos
**Grupo:** 5

**Integrantes:**
- Arturo Knopke Vera
- Nicolás Soletic Cobos
- Sebastián Navarrete Soto
- Roberto Moncada González

## Descripción

El proyecto trabaja con el dataset **Titanic** (891 pasajeros, 12 variables; fuente: Kaggle, *Titanic - Machine Learning from Disaster*), que combina información demográfica, socioeconómica y de composición familiar de los pasajeros del RMS Titanic.

- **Fase 1 – Implementación inicial del EDA reproducible:** carga y revisión inicial del dataset, diagnóstico de calidad (valores faltantes), exploración descriptiva univariada y bivariada frente a `Survived`, documentación trazable de cinco decisiones exploratorias (indicadores de completitud para `Cabin` y `Age`, imputación puntual de `Embarked`, construcción de `FamilySize`/`IsAlone` y extracción de `Title`), detección preliminar de valores atípicos mediante IQR y síntesis de hallazgos iniciales. No se realiza imputación definitiva, codificación final ni modelado predictivo en esta fase.

## Estructura del proyecto

```
.
├── data/
│   └── Titanic-Dataset.csv                     # Dataset original (891 registros)
├── docs/
│   ├── f1_s01_evaluacion_entregable.docx       # Informe entregable Fase 1, versión extensa (6 p.)
│   └── f1_s01_evaluacion_entregable_4p.docx    # Informe entregable Fase 1, versión compacta (4 p.)
├── figures/                                    # Gráficos generados por el notebook
│   ├── f1_titanic_dist_age_fare.png
│   ├── f1_titanic_frecuencias_categoricas.png
│   ├── f1_titanic_supervivencia_categoricas.png
│   ├── f1_titanic_boxplots_survived.png
│   ├── f1_titanic_familia_titulo.png
│   └── f1_titanic_correlacion.png
├── notebooks/
│   └── mcdi503_f1_sumativo_grupo5.ipynb        # Notebook Fase 1
├── requirements.txt
└── README.md
```

## Contenido del notebook

### mcdi503_f1_sumativo_grupo5.ipynb

1. Identificación del proyecto
2. Contexto y objetivo exploratorio
3. Carga y revisión inicial de datos
4. Exploración preliminar
5. Decisiones y transformaciones iniciales
6. Resultados e interpretación inicial
7. Supuestos y limitaciones
8. Cierre del avance

## Requisitos

- Python 3.12+

## Instalación (en carpeta raíz del proyecto MCDI503)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Uso

```bash
source .venv/bin/activate
jupyter lab notebooks/
```

El notebook carga el dataset desde `../data/Titanic-Dataset.csv` y guarda las figuras generadas en `../figures/`, por lo que debe ejecutarse con `notebooks/` como directorio de trabajo (comportamiento por defecto al abrirlo desde Jupyter en esa carpeta).

## Referencias

- Kaggle. (s. f.). *Titanic - Machine Learning from Disaster* [Conjunto de datos]. https://www.kaggle.com/c/titanic
- McKinney, W. (2010). Data structures for statistical computing in Python. *Proceedings of the 9th Python in Science Conference*, 56-61. https://doi.org/10.25080/Majora-92bf1922-00a
- Paraíso, S. (2026). *Resumen aplicado del libro: EDA mínimo viable* [Apunte]. Universidad Andrés Bello, Santiago, Chile.
- The pandas development team. (2026). *pandas documentation* (versión 3.0) [Documentación de software]. https://pandas.pydata.org/docs/
- Waskom, M. L. (2021). Seaborn: Statistical data visualization. *Journal of Open Source Software, 6*(60), 3021. https://doi.org/10.21105/joss.03021
- Wilson, G., Bryan, J., Cranston, K., Kitzes, J., Nederbragt, L., & Teal, T. K. (2017). Good enough practices in scientific computing. *PLOS Computational Biology, 13*(6), e1005510. https://doi.org/10.1371/journal.pcbi.1005510
