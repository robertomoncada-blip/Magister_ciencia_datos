# AI Impact on Jobs 2030 – Fase 1

Proyecto de la asignatura **MCDI504 – Machine Learning I**, correspondiente a la **Fase 1: Definición y Orientación de la Situación**.

**Curso:** MCDI504 - Machine Learning I
**Grupo:** 5

**Integrantes:**
- Arturo Knopke Vera
- Nicolás Soletic Cobos
- Sebastián Navarrete Soto
- Roberto Moncada González

**Fecha de entrega:** 9 de agosto de 2026

## Descripción

**NextWork Advisory** es una consultora ficticia de estrategia de talento y planificación de fuerza laboral. El proyecto utiliza el dataset **AI Impact on Jobs 2030** (3.000 perfiles laborales) para evaluar si es posible construir un modelo capaz de estimar el nivel de riesgo de automatización (`Risk_Category`: Low / Medium / High) de un cargo hacia 2030, a partir de características observables como salario, experiencia, educación, exposición a la IA y perfil de habilidades.

Esta Fase 1 se limita a la definición del problema, la exploración descriptiva inicial de los datos y la justificación del enfoque de aprendizaje (clasificación supervisada multiclase). No se entrena ningún modelo predictivo en esta etapa; eso se abordará en fases posteriores (F2–F4).

## Estructura del proyecto

```
.
├── data/
│   └── AI_Impact_on_Jobs_2030.csv     # Dataset original (3.000 registros)
├── docs/
│   ├── MCDI504_S1_1_GRUPO5.pdf        # Informe entregable
│   └── MCDI504_S1_1_GRUPO5.docx
├── figures/                           # Gráficos generados por el notebook
│   ├── boxplot_salario_experiencia.png
│   ├── boxplot_indices_habilidades.png
│   ├── correlacion_pearson.png
│   ├── pvalores_pearson.png
│   └── kdd_proceso.png
├── notebooks/
│   └── F1_Definicion.ipynb            # Notebook principal del análisis
├── requirements.txt
└── Readme.md
```

## Contenido del notebook

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

## Requisitos

- Python 3.12+

## Instalación

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Uso

```bash
source .venv/bin/activate
jupyter notebook notebooks/F1_Definicion.ipynb
```

El notebook carga el dataset desde `../data/AI_Impact_on_Jobs_2030.csv` y guarda las figuras generadas en `../figures/`, por lo que debe ejecutarse con `notebooks/` como directorio de trabajo (comportamiento por defecto al abrirlo desde Jupyter en esa carpeta).

## Referencias

- Fayyad, U., Piatetsky-Shapiro, G., & Smyth, P. (1996). From data mining to knowledge discovery in databases. *AI Magazine*, *17*(3), 37-54.
- pandas development team. (s. f.). *pandas documentation*. https://pandas.pydata.org/docs/
- Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., Blondel, M., Prettenhofer, P., Weiss, R., Dubourg, V., Vanderplas, J., Passos, A., Cournapeau, D., Brucher, M., Perrot, M., & Duchesnay, É. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research*, *12*, 2825-2830.
- Ruete, D. (2026a). *Introducción al Machine Learning* [Apunte]. Universidad Andrés Bello, Santiago, Chile.
- Ruete, D. (2026b). *Relación entre ML y Metodología KDD* [Apunte]. Universidad Andrés Bello, Santiago, Chile.
- Ruete, D. (2026c). *Fase 1: Estadística descriptiva, correlación y normalización de datos* [Apunte]. Universidad Andrés Bello, Santiago, Chile.
- scikit-learn developers. (s. f.). *scikit-learn documentation*. https://scikit-learn.org/stable/documentation.html
