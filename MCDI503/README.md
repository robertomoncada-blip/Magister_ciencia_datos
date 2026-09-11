# Análisis exploratorio reproducible del dataset Titanic

Proyecto de la asignatura **MCDI503 – Exploración Inteligente para la Ciencia de Datos**. Incluye la Fase 1 (implementación inicial del EDA reproducible) y las Fases 2 y 3 (diagnóstico de calidad, limpieza, integración, transformación y análisis exploratorio univariado-bivariado).

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
- **Fases 2 y 3 – Diagnóstico, limpieza, integración, transformación y análisis exploratorio:** diagnóstico formal de calidad (faltantes, duplicados, inconsistencias de dominio, categorías problemáticas), limpieza e imputación definitivas (`Embarked` con la moda; `Age` con la mediana estratificada por `Pclass × Sex`, validada mediante Kruskal-Wallis), **integración de una fuente complementaria de origen web** (`seaborn`-data) con validación estructural y semántica de la correspondencia entre registros, transformaciones analíticas (`Title_agrupado`, `FamilySize`/`IsAlone`, `AgeGroup`, `Fare_log`, `FareBand`, `Deck_combinado`), análisis univariado con pruebas de normalidad (D'Agostino-Pearson) y análisis bivariado con pruebas estadísticas formales (chi-cuadrado y V de Cramér, Mann-Whitney U, correlaciones de Pearson/Spearman), y detección de outliers (IQR y Z-score robusto/MAD) con distinción entre error de dato y comportamiento relevante.

## Estructura del proyecto

```
.
├── data/
│   ├── Titanic-Dataset.csv                     # Dataset principal (891 registros, Kaggle)
│   ├── titanic_seaborn_reference.csv           # Fuente complementaria (origen web, seaborn-data), cacheada para reproducibilidad
│   └── titanic_prepared.csv                    # Dataset preparado tras limpieza/integración/transformación (Fases 2 y 3)
├── docs/
│   ├── mcdi503_f1_sumativo_grupo5.docx         # Informe entregable Fase 1
│   └── mcdi503_f23_sumativo_grupo5.pdf         # Informe entregable Fases 2 y 3
├── figures/                                    # Gráficos generados por los notebooks
│   ├── f1_titanic_*.png                        # Figuras de la Fase 1
│   └── f23_titanic_*.png                       # Figuras de las Fases 2 y 3
├── notebooks/
│   ├── mcdi503_f1_sumativo_grupo5.ipynb        # Notebook Fase 1
│   └── mcdi503_f23_sumativo_grupo5.ipynb       # Notebook Fases 2 y 3
├── requirements.txt
└── README.md
```

## Contenido de los notebooks

### mcdi503_f1_sumativo_grupo5.ipynb

1. Identificación del proyecto
2. Contexto y objetivo exploratorio
3. Carga y revisión inicial de datos
4. Exploración preliminar
5. Decisiones y transformaciones iniciales
6. Resultados e interpretación inicial
7. Supuestos y limitaciones
8. Cierre del avance

### mcdi503_f23_sumativo_grupo5.ipynb

1. Encabezado e identificación del notebook
2. Carga del dataset y descripción inicial
3. Revisión del contenido del dataset
4. Diagnóstico de calidad de datos
5. Limpieza, validación e integración (incluye integración con fuente web)
6. Transformaciones aplicadas y preparación del dataset
7. Análisis univariado
8. Análisis bivariado
9. Patrones, anomalías y hallazgos iniciales
10. Supuestos, límites y cierre del avance
11. Cierre del avance

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

Ambos notebooks cargan el dataset principal desde `../data/Titanic-Dataset.csv` y guardan las figuras generadas en `../figures/`, por lo que deben ejecutarse con `notebooks/` como directorio de trabajo (comportamiento por defecto al abrirlos desde Jupyter en esa carpeta). El notebook de Fases 2 y 3 además carga la fuente complementaria desde `../data/titanic_seaborn_reference.csv` (una copia local cacheada de `seaborn.load_dataset("titanic")`, guardada así para que el notebook sea ejecutable sin depender de conexión a internet) y exporta el dataset preparado a `../data/titanic_prepared.csv`.

## Referencias

- Kaggle. (s. f.). *Titanic - Machine Learning from Disaster* [Conjunto de datos]. https://www.kaggle.com/c/titanic
- McKinney, W. (2010). Data structures for statistical computing in Python. *Proceedings of the 9th Python in Science Conference*, 56-61. https://doi.org/10.25080/Majora-92bf1922-00a
- Paraíso, S. (2026). *Resumen aplicado del libro: EDA mínimo viable* [Apunte]. Universidad Andrés Bello, Santiago, Chile.
- The pandas development team. (2026). *pandas documentation* (versión 3.0) [Documentación de software]. https://pandas.pydata.org/docs/
- Virtanen, P., Gommers, R., Oliphant, T. E., et al. (2020). SciPy 1.0: Fundamental algorithms for scientific computing in Python. *Nature Methods, 17*, 261-272. https://doi.org/10.1038/s41592-019-0686-2
- Waskom, M. L. (2021). Seaborn: Statistical data visualization. *Journal of Open Source Software, 6*(60), 3021. https://doi.org/10.21105/joss.03021
- Waskom, M. L. (s. f.). *seaborn-data* [Repositorio de datos]. GitHub. https://github.com/mwaskom/seaborn-data
- Wilson, G., Bryan, J., Cranston, K., Kitzes, J., Nederbragt, L., & Teal, T. K. (2017). Good enough practices in scientific computing. *PLOS Computational Biology, 13*(6), e1005510. https://doi.org/10.1371/journal.pcbi.1005510
