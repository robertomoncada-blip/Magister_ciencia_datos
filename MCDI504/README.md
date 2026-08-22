# AI Impact on Jobs 2030

Proyecto de la asignatura **MCDI504 – Machine Learning I**. Cubre las Fases 1 a 3 del proyecto: definición del problema, implementación de modelos de regresión y desarrollo de modelos de clasificación mediante redes neuronales.

**Curso:** MCDI504 - Machine Learning I
**Grupo:** 5

**Integrantes:**
- Arturo Knopke Vera
- Nicolás Soletic Cobos
- Sebastián Navarrete Soto
- Roberto Moncada González

## Descripción

**NextWork Advisory** es una consultora ficticia de estrategia de talento y planificación de fuerza laboral. El proyecto utiliza el dataset **AI Impact on Jobs 2030** (3.000 perfiles laborales) para evaluar si es posible construir un modelo capaz de estimar el nivel de riesgo de automatización (`Risk_Category`: Low / Medium / High) de un cargo hacia 2030, a partir de características observables como salario, experiencia, educación, exposición a la IA y perfil de habilidades.

- **Fase 1 – Definición y Orientación de la Situación:** definición del problema, exploración descriptiva inicial de los datos y justificación del enfoque de aprendizaje (clasificación supervisada multiclase). No se entrena ningún modelo predictivo en esta etapa.
- **Fase 2 – Búsqueda y Recopilación de Información:** implementación y comparación de modelos de regresión supervisada (regresión lineal multivariable, árbol de decisión y red neuronal MLP) sobre una variable objetivo continua derivada del dataset.
- **Fase 3 – Desarrollo del Proyecto:** implementación y comparación de modelos de clasificación supervisada mediante redes neuronales (MLP) con una, dos y tres capas ocultas, para predecir `Risk_Category`.

## Estructura del proyecto

```
.
├── data/
│   └── AI_Impact_on_Jobs_2030.csv          # Dataset original (3.000 registros)
├── docs/
│   ├── MCDI504_S1_1_GRUPO5.pdf/.docx       # Informe entregable Fase 1
│   ├── MCDI504_F2_1_GRUPO5.pdf/.docx       # Informe entregable Fase 2
│   └── MCDI504_S3_2_GRUPO5.docx            # Informe entregable Fase 3
├── figures/                                # Gráficos generados por los notebooks
│   ├── boxplot_salario_experiencia.png     # Fase 1
│   ├── boxplot_indices_habilidades.png
│   ├── correlacion_pearson.png
│   ├── pvalores_pearson.png
│   ├── kdd_proceso.png
│   ├── f2_*.png                            # Fase 2 (regresión)
│   └── f3_*.png                            # Fase 3 (redes neuronales)
├── notebooks/
│   ├── F1_Definicion.ipynb                 # Notebook Fase 1
│   ├── F2_Regresion.ipynb                  # Notebook Fase 2
│   └── F3_RedesNeuronales.ipynb            # Notebook Fase 3
├── requirements.txt
└── Readme.md
```

## Contenido de los notebooks

### F1_Definicion.ipynb

1. Contexto y definición del problema
2. Librerías necesarias
3. Carga de la base de datos
4. Análisis descriptivo inicial
5. Visualización de la distribución con boxplot
6. Transformación de variables categóricas ordinales
7. Matriz de correlación de Pearson
8. Matriz de p-valores
9. Normalización de datos (Min-Max)
10. Base de datos normalizada completa
11. Relación con la metodología KDD
12. Clasificación del tipo de aprendizaje
13. Comparación de enfoques
14. Conclusiones

### F2_Regresion.ipynb

1. Contexto y objetivo de la Fase 2
2. Librerías necesarias
3. Carga del conjunto de datos
4. Descripción del conjunto de datos y preprocesamiento (variables, valores faltantes, relación `Job_Title`–objetivo, codificación, partición train/test, escalado, distribución del target)
5. Modelo de regresión lineal multivariable
6. Modelo de árbol de decisión para regresión
7. Modelo de red neuronal (MLP) para regresión
8. Evaluación de modelos de regresión
9. Comparación de modelos
10. Conclusiones
11. Referencias

### F3_RedesNeuronales.ipynb

1. Contexto y objetivo de la Fase 3
2. Librerías necesarias
3. Carga del conjunto de datos
4. Descripción del dataset y preparación para redes neuronales (variables, codificación, partición train/test, escalado)
5. Análisis exploratorio inicial y preparación de datos (distribución de clases de `Risk_Category`, relación `Job_Title`–`Risk_Category`)
6. Red neuronal con una capa oculta
7. Red neuronal con dos capas ocultas
8. Red neuronal con tres capas ocultas
9. Evaluación de desempeño de redes neuronales
10. Comparación de arquitecturas de redes neuronales
11. Conclusiones
12. Referencias

## Requisitos

- Python 3.12+

## Instalación (en carpeta raiz del proyecto MCDI504)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Uso

```bash
source .venv/bin/activate
jupyter notebook notebooks/
```

Cada notebook carga el dataset desde `../data/AI_Impact_on_Jobs_2030.csv` y guarda las figuras generadas en `../figures/`, por lo que debe ejecutarse con `notebooks/` como directorio de trabajo (comportamiento por defecto al abrirlo desde Jupyter en esa carpeta).

## Referencias

- Fayyad, U., Piatetsky-Shapiro, G., & Smyth, P. (1996). From data mining to knowledge discovery in databases. *AI Magazine*, *17*(3), 37-54.
- Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep learning*. MIT Press. https://www.deeplearningbook.org/
- pandas development team. (s. f.). *pandas documentation*. https://pandas.pydata.org/docs/
- Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., Blondel, M., Prettenhofer, P., Weiss, R., Dubourg, V., Vanderplas, J., Passos, A., Cournapeau, D., Brucher, M., Perrot, M., & Duchesnay, É. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research*, *12*, 2825-2830.
- Ruete, D. (2026a). *Introducción al Machine Learning* [Apunte]. Universidad Andrés Bello, Santiago, Chile.
- Ruete, D. (2026b). *Relación entre ML y Metodología KDD* [Apunte]. Universidad Andrés Bello, Santiago, Chile.
- Ruete, D. (2026c). *Fase 1: Estadística descriptiva, correlación y normalización de datos* [Apunte]. Universidad Andrés Bello, Santiago, Chile.
- Ruete, D. (2026d). *Fase 3: Redes neuronales para clasificación supervisada* [Apunte]. Universidad Andrés Bello, Santiago, Chile.
- scikit-learn developers. (s. f.). *scikit-learn documentation*. https://scikit-learn.org/stable/documentation.html
- scikit-learn Developers. (2026a). *`sklearn.neural_network.MLPClassifier`*. scikit-learn. https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html
- scikit-learn Developers. (2026b). *Metrics and scoring: quantifying the quality of predictions*. scikit-learn. https://scikit-learn.org/stable/modules/model_evaluation.html
