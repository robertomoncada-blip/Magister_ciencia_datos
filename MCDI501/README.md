# Análisis de Incumplimiento de Clientes de Tarjetas de Crédito
### MCDI501: Estadística Computacional para la Toma de Decisiones
**Magíster en Ciencia de Datos e Inteligencia Artificial**

---

## Descripción del Proyecto

Este repositorio contiene el análisis estadístico del dataset *Default of Credit Card Clients* (UCI, Taiwan 2005), desarrollado como parte de la Evaluación Formativa 1 del curso MCDI501.

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
│       └── fig_*.png                           # Figuras exportadas por el notebook
├── notebooks/
│   └── F1_semana1.ipynb                        # Análisis EDA e inferencial (Formativa 1)
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

| Sección | Contenido | Indicador |
|---|---|---|
| Valores faltantes | Verificación MCAR (t-test), imputación mediana/moda | — |
| Estadística descriptiva | Medidas de tendencia central, dispersión, histogramas, boxplots, correlaciones | ID1.2 |
| Estimación puntual e IC | IC 95% para media de LIMIT_BAL, proporción de default, edad, facturación | ID1.3 |
| Pruebas de hipótesis | Welch t-test (LIMIT_BAL × default), Chi-cuadrado (SEX × default, EDUCATION × default) | ID1.4 |
| Interpretación | Implicaciones para gestión de riesgo crediticio | — |

### Resultados destacados

- Tasa de incumplimiento: **22,12%** [IC 95%: 21,65% – 22,59%]
- Los clientes que incumplieron tienen un límite de crédito significativamente menor (NT$131.246 vs NT$173.620; t=27,13; p<0,001)
- El nivel educacional se asocia con la tasa de default: Secundaria (25,2%) > Universidad (23,7%) > Posgrado (19,2%)

## Equipo

| Integrante | Rol |
|---|---|
| Arturo Knopke Vera | Integrante |
| Nicolás Soletic Cobos | Integrante |
| Sebastián Navarrete Soto | Integrante |
| Roberto Moncada González | Integrante |

**Docente:** Jean Paul Maidana
