# Análisis de Incumplimiento de Clientes de Tarjetas de Crédito
### MCDI501: Estadística Computacional para la Toma de Decisiones
**Magíster en Ciencia de Datos e Inteligencia Artificial**

---

## Descripción del Proyecto

Este repositorio contiene el análisis estadístico del dataset *Default of Credit Card Clients* (UCI, Taiwan 2005), desarrollado como parte de la Evaluación Sumativa 1 — Fase 2 del curso MCDI501.

El objetivo es caracterizar el comportamiento de pago de clientes de tarjetas de crédito mediante estadística descriptiva, estimación paramétrica y pruebas de hipótesis, sentando las bases para el desarrollo posterior de modelos predictivos que apoyen la toma de decisiones en gestión de riesgo crediticio.

## Dataset

| Atributo | Detalle |
|---|---|
| **Nombre** | Default of Credit Card Clients |
| **Fuente** | UCI Machine Learning Repository |
| **Período** | Abril – Septiembre 2005, Taiwan |
| **Observaciones** | 30.000 clientes |
| **Variables** | 25 (demográficas, historial de pagos, facturas, montos pagados) |
| **Variable objetivo** | `default.payment.next.month` (1 = incumple, 0 = no incumple) |
| **Tasa de incumplimiento** | 22,12% |

El archivo utilizado es `data/raw/UCI_Credit_Card_con_faltantes.csv`, que introduce valores faltantes bajo mecanismo **MCAR** (semilla 42) en las variables `LIMIT_BAL` y `PAY_0` (12,5% cada una).

## Estructura del Repositorio

```
MCDI501/
├── data/
│   └── raw/
│       ├── UCI_Credit_Card_con_faltantes.csv   # Dataset con valores faltantes (MCAR)
│       ├── UCI_Credit_Card.csv                 # Dataset original sin faltantes
│       └── fig_*.png                           # Figuras exportadas (histogramas, boxplots, IC, tests)
├── notebooks/
│   └── F1_semana1.ipynb                        # Análisis EDA e inferencial (Sumativa 1 — Fase 2)
├── src/
│   └── data_loading.py                         # Módulo de carga de datos (cargar_datos)
├── requirements.txt                            # Dependencias del proyecto
└── README.md
```

## Instalación y Uso

### 1. Clonar el repositorio

```bash
git clone https://github.com/robertomoncada-blip/Magister_ciencia_datos.git
cd Magister_ciencia_datos/MCDI501
```

### 2. Crear entorno virtual e instalar dependencias

```bash
python3 -m venv .venv
source .venv/bin/activate        # macOS / Linux
# .venv\Scripts\activate         # Windows

pip install -r requirements.txt
```

### 3. Ejecutar el notebook

```bash
jupyter lab notebooks/F1_semana1.ipynb
```

## Análisis Realizados (F1_semana1.ipynb)

El notebook está estructurado en 9 secciones:

| # | Sección | Contenido | Criterio |
|---|---|---|---|
| 1 | Carga y exploración inicial | Dimensiones, tipos de datos, vista previa | — |
| 2 | Valores faltantes | Verificación MCAR (t-test sobre AGE), imputación mediana/moda | — |
| 3 | Preprocesamiento | Tipado de variables, eliminación de ID | — |
| 4 | Estadística descriptiva | Medidas de tendencia central, dispersión, histogramas, boxplots, mapa de correlaciones | ID1.2 |
| 5 | Estimación puntual e IC | IC 95% (t-Student y Wilson) para LIMIT_BAL, proporción de default, AGE, BILL_AMT1, PAY_AMT1 | ID1.3 |
| 6 | Pruebas de hipótesis | T1: Welch t-test (LIMIT_BAL × default); T2: χ² (SEX × default); T3: χ² (EDUCATION × default) | ID1.4 |
| 7 | Resumen e interpretación | Tabla resumen de pruebas con tamaños de efecto; interpretación vinculada a decisiones bajo incertidumbre | — |
| 8 | Conclusiones generales | Hallazgos principales, limitaciones metodológicas, proyecciones para modelos predictivos | — |
| 9 | Referencias | Fuentes bibliográficas (Yeh & Lien 2009, UCI, Cohen, Wilson, Agresti, Montgomery) | — |

### Resultados destacados

| Análisis | Resultado |
|---|---|
| Tasa de incumplimiento | **22,12%** [IC 95%: 21,65% – 22,59%] |
| Límite de crédito (No Default vs Default) | NT$173.620 vs NT$131.246 — t=27,13; p≈2,3×10⁻¹⁵⁷; d Cohen=0,363 |
| Género × Incumplimiento | Masculino 24,2% vs Femenino 20,8% — χ²=47,71; p<0,0001; V Cramér=0,040 (negligible) |
| Educación × Incumplimiento | Secundaria 25,2% > Universidad 23,7% > Posgrado 19,2% — χ²=97,00; p<0,0001; V Cramér=0,057 (negligible) |

## Equipo

| Integrante | Rol |
|---|---|
| Arturo Knopke Vera | Integrante |
| Nicolás Soletic Cobos | Integrante |
| Sebastián Navarrete Soto | Integrante |
| Roberto Moncada González | Integrante |

**Docente:** Jean Paul Maidana
