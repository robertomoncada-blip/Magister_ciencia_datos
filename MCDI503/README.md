# Análisis exploratorio reproducible del dataset Titanic

Proyecto de la asignatura **MCDI503 – Exploración Inteligente para la Ciencia de Datos**. Incluye la Fase 1 (implementación inicial del EDA reproducible), las Fases 2 y 3 (diagnóstico de calidad, limpieza, integración, transformación y análisis exploratorio univariado-bivariado) y la Fase 4 (ingeniería de variables y selección preliminar de características).

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
- **Fase 4 – Ingeniería de variables y selección preliminar de características:** a partir de `titanic_prepared.csv`, escalado robusto (`RobustScaler`) de las variables numéricas con colas legítimas, dos variables derivadas conceptuales (`Fare_per_person_log`, tarifa por persona a partir del grupo de `Ticket`; y la interacción `Sex_Pclass`, validada con un test de razón de verosimilitudes), selección preliminar con criterios explícitos (relevancia según V de Cramér, rango-biserial e información mutua con estabilidad en 21 semillas; redundancia exacta frente a parcial; interpretabilidad), inventario de destino de las 36 columnas disponibles, codificación *one-hot* con categoría de referencia explícita y exportación del dataset final de características (`titanic_features.csv`, 891 × 29: 27 características más `PassengerId` y `Survived`). No se entrena ningún modelo predictivo.

## Estructura del proyecto

```
.
├── data/
│   ├── Titanic-Dataset.csv                     # Dataset principal (891 registros, Kaggle)
│   ├── titanic_seaborn_reference.csv           # Fuente complementaria (origen web, seaborn-data), cacheada para reproducibilidad
│   ├── titanic_prepared.csv                    # Dataset preparado tras limpieza/integración/transformación (Fases 2 y 3)
│   └── titanic_features.csv                    # Dataset final de características, codificado y escalado (Fase 4)
├── docs/
│   ├── mcdi503_S1_sumativo_grupo5.docx/.pdf    # Informe entregable Fase 1
│   ├── mcdi503_f23_sumativo_grupo5.docx/.pdf   # Informe entregable Fases 2 y 3
│   └── mcdi503_f4_sumativo_grupo5.docx         # Informe entregable Fase 4 (el PDF se exporta desde este archivo)
├── figures/                                    # Gráficos generados por los notebooks
│   ├── f1_titanic_*.png                        # Figuras de la Fase 1
│   ├── f23_titanic_*.png                       # Figuras de las Fases 2 y 3
│   └── f4_titanic_*.png                        # Figuras de la Fase 4
├── notebooks/
│   ├── mcdi503_f1_sumativo_grupo5.ipynb        # Notebook Fase 1
│   ├── mcdi503_f23_sumativo_grupo5.ipynb       # Notebook Fases 2 y 3
│   └── mcdi503_f4_sumativo_grupo5.ipynb        # Notebook Fase 4
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

### mcdi503_f4_sumativo_grupo5.ipynb

1. Encabezado e identificación del notebook
2. Carga de datos y preparación del entorno
3. Revisión inicial del dataset
4. Transformaciones y normalizaciones aplicadas
5. Variables derivadas o creadas
6. Selección preliminar de características (incluye tabla de decisiones e inventario completo de columnas)
7. Documentación y trazabilidad del pipeline
8. Resultado final del dataset preparado
9. Supuestos, limitaciones y cierre del notebook

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

Los notebooks de las Fases 1 y 2-3 usan rutas relativas y guardan las figuras generadas en `../figures/`, por lo que deben ejecutarse con `notebooks/` como directorio de trabajo (comportamiento por defecto al abrirlos desde Jupyter en esa carpeta). Cargan el dataset principal desde `../data/Titanic-Dataset.csv`; el notebook de Fases 2 y 3 además carga la fuente complementaria desde `../data/titanic_seaborn_reference.csv` (una copia local cacheada de `seaborn.load_dataset("titanic")`, guardada así para que el notebook sea ejecutable sin depender de conexión a internet) y exporta el dataset preparado a `../data/titanic_prepared.csv`.

El notebook de la Fase 4 es distinto: no depende de ningún archivo local ni de una carpeta de trabajo fija. Su sección II.1 verifica que las librerías instaladas cumplan las versiones mínimas de `requirements.txt` (deteniendo la ejecución con un error explícito si no es así), y su sección II.2 reconstruye de forma condensada el pipeline de las Fases 1 y 2-3 (limpieza, imputación, integración y transformaciones) leyendo ambas fuentes **directamente desde internet**. Las figuras y el dataset final (`titanic_features.csv`) se escriben en el **directorio de trabajo actual** (el mismo desde el que se ejecuta el notebook, típicamente `notebooks/` si se abre normalmente desde ahí), en lugar de `../figures/` y `../data/`.

## Referencias

- Cohen, J. (1988). *Statistical power analysis for the behavioral sciences* (2.ª ed.). Lawrence Erlbaum Associates.
- Kaggle. (s. f.). *Titanic - Machine Learning from Disaster* [Conjunto de datos]. https://www.kaggle.com/c/titanic
- Kraskov, A., Stögbauer, H., & Grassberger, P. (2004). Estimating mutual information. *Physical Review E, 69*(6), Artículo 066138. https://doi.org/10.1103/PhysRevE.69.066138
- McKinney, W. (2010). Data structures for statistical computing in Python. *Proceedings of the 9th Python in Science Conference*, 56-61. https://doi.org/10.25080/Majora-92bf1922-00a
- Paraíso, S. (2026). *Resumen aplicado del libro: EDA mínimo viable* [Apunte]. Universidad Andrés Bello, Santiago, Chile.
- Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., Blondel, M., Prettenhofer, P., Weiss, R., Dubourg, V., Vanderplas, J., Passos, A., Cournapeau, D., Brucher, M., Perrot, M., & Duchesnay, É. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research, 12*, 2825–2830.
- The pandas development team. (2026). *pandas documentation* (versión 3.0) [Documentación de software]. https://pandas.pydata.org/docs/
- Virtanen, P., Gommers, R., Oliphant, T. E., et al. (2020). SciPy 1.0: Fundamental algorithms for scientific computing in Python. *Nature Methods, 17*, 261-272. https://doi.org/10.1038/s41592-019-0686-2
- Waskom, M. L. (2021). Seaborn: Statistical data visualization. *Journal of Open Source Software, 6*(60), 3021. https://doi.org/10.21105/joss.03021
- Waskom, M. L. (s. f.). *seaborn-data* [Repositorio de datos]. GitHub. https://github.com/mwaskom/seaborn-data
- Wilson, G., Bryan, J., Cranston, K., Kitzes, J., Nederbragt, L., & Teal, T. K. (2017). Good enough practices in scientific computing. *PLOS Computational Biology, 13*(6), e1005510. https://doi.org/10.1371/journal.pcbi.1005510
