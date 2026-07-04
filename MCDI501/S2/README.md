# Análisis de Incumplimiento de Clientes de Tarjetas de Crédito
### MCDI501: Estadística Computacional para la Toma de Decisiones
**Magíster en Ciencia de Datos e Inteligencia Artificial**

---

## Descripción del Proyecto

Este repositorio contiene el desarrollo de la **Evaluación Sumativa 2** del curso MCDI501, centrada en **validación, simulación y métodos de remuestreo** sobre el dataset *Default of Credit Card Clients* (UCI, Taiwan 2005).

El trabajo no es independiente: se construye explícitamente sobre los resultados de la Sumativa 1 (parámetros estimados, intervalos de confianza y pruebas de hipótesis) y los valida y extiende mediante **bootstrap, permutación, simulación Monte Carlo y análisis de robustez (jackknife)**, generando insumos reutilizables para la Sumativa 3.

| | |
|---|---|
| **Dataset** | Default of Credit Card Clients (UCI Machine Learning Repository, Taiwan 2005) |
| **Fase del proyecto** | Fase 3: Desarrollo del proyecto (Evaluación Sumativa 2) |
| **Resultado de aprendizaje** | RA2: implementar métodos computacionales de simulación y remuestreo para apoyar la toma de decisiones en escenarios complejos |
| **Indicadores** | ID2.1, ID2.2, ID2.3 |
| **Ponderación** | 20% de la nota final |

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

El archivo utilizado es `data/raw/UCI_Credit_Card_con_faltantes.csv`, que introduce valores faltantes bajo mecanismo **MCAR** (semilla 42) en las variables `LIMIT_BAL` y `PAY_0` (12,5% cada una). El preprocesamiento (imputación mediana/moda, tipado, eliminación de `ID`) se reconstruye íntegramente en la Sección 0 del notebook de esta fase para que el análisis sea autocontenido y reproducible a partir de los datos crudos.

## Estructura del Repositorio

```
S2/
├── data/
│   └── raw/
│       ├── UCI_Credit_Card_con_faltantes.csv   # Dataset con valores faltantes (MCAR)
│       ├── UCI_Credit_Card.csv                 # Dataset original sin faltantes
│       └── valores_originales_referencia.csv   # Valores originales de referencia (pre-MCAR)
├── figures/                                    # Figuras exportadas por F2_semana2.ipynb
│   ├── fig_boot_ic.png                         # IC bootstrap (percentil, BCa) vs. clásico
│   ├── fig_perm_tests.png                      # Distribuciones nulas de permutación (T1, T2)
│   ├── fig_corr_estabilidad.png                # Estabilidad de correlaciones (IC bootstrap)
│   ├── fig_mc_simulacion.png                   # Simulación Monte Carlo de exposición crediticia
│   └── fig_robustez_distribucion.png           # Sensibilidad al supuesto distribucional (Normal vs. Lognormal)
├── notebooks/
│   ├── F1_semana1.ipynb                        # Análisis EDA e inferencial (Sumativa 1 — etapa anterior)
│   └── F2_semana2.ipynb                        # Validación, simulación y remuestreo (Sumativa 2 — esta fase)
├── src/
│   └── data_loading.py                         # Módulo de carga de datos (cargar_datos)
├── resultados_validados_S1.md                  # Resultados validados, generado por F2 como insumo para S3
└── requirements.txt                             # Dependencias del proyecto
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
jupyter lab notebooks/F2_semana2.ipynb
```

## Análisis Realizados (F2_semana2.ipynb)

El notebook está estructurado en 9 secciones:

| # | Sección | Contenido | Puntaje |
|---|---|---|---|
| 0 | Importaciones, preprocesamiento y resultados de S1 | Reconstrucción del pipeline de S1 y recálculo de sus IC y pruebas de hipótesis, como base de comparación | — |
| 1 | Validación mediante bootstrap | IC bootstrap (percentil y BCa, 10.000 remuestras) para 5 parámetros de S1 (LIMIT_BAL, proporción de default, AGE, BILL_AMT1, PAY_AMT1) vs. IC clásico | 18 pts |
| 2 | Validación de pruebas de hipótesis mediante permutación | Test de permutación (10.000 permutaciones) para T1 (Welch t-test LIMIT_BAL × Default) y T2 (χ² Género × Default) | 15 pts |
| 3 | Estabilidad de correlaciones | IC bootstrap percentil (10.000 remuestras) para 5 correlaciones de Pearson del mapa de S1 | 6 pts |
| 4 | Simulación Monte Carlo | Simulación de exposición crediticia (10.000 iteraciones, portafolio N=5.000) a partir de parámetros de S1; VaR simulado al 95% | 24 pts |
| 5 | Análisis de robustez | Jackknife vectorizado (media LIMIT_BAL, correlación LIMIT_BAL–DEFAULT), sensibilidad a outliers (IQR, media recortada) y al supuesto distribucional (Normal vs. Lognormal) | 15 pts |
| 6 | Preparación para la Sumativa 3 | Síntesis de parámetros y correlaciones robustas, observaciones influyentes y recomendaciones metodológicas; exporta `resultados_validados_S1.md` | 9 pts |
| 7 | Conclusiones generales | Síntesis de validación, simulación, robustez y limitaciones metodológicas | — |
| 8 | Referencias (APA 7) | Bootstrap (Efron & Tibshirani), permutación (Good), jackknife (Quenouille, Tukey), Monte Carlo (Metropolis & Ulam), SciPy (Virtanen et al.), entre otras | — |

Todas las semillas aleatorias (bootstrap, permutación, simulación Monte Carlo) se fijan en `SEED = 42` para garantizar reproducibilidad exacta.

### Resultados destacados

| Análisis | Resultado |
|---|---|
| Validación bootstrap (5 parámetros) | IC bootstrap (percentil/BCa) ≈ IC clásico de S1; diferencia de amplitud entre −0,94% y +0,27% |
| Permutación T1 (LIMIT_BAL × Default) | p permutación = 0,0002 vs. p paramétrico ≈ 2,3×10⁻¹⁵⁷ — coincide en la decisión (rechaza H₀) |
| Permutación T2 (Género × Default) | p permutación = 0,0002 vs. p paramétrico (χ²) = 4,95×10⁻¹² — coincide en la decisión (rechaza H₀) |
| Correlación más estable | BILL_AMT1–BILL_AMT2: r=0,951, amplitud relativa del IC ≈1,1% |
| Correlación más inestable | AGE–DEFAULT: r=0,014, amplitud relativa del IC ≈169% (significativa pero sin relevancia práctica) |
| Simulación Monte Carlo (exposición crediticia) | Exposición total media ≈ NT$845,8M; EAD medio ≈ NT$151,8M [P5–P95: NT$143,4M–NT$160,5M]; VaR 95% simulado; pérdida esperada relativa ≈17,95% |
| Robustez a outliers (LIMIT_BAL) | 4,14% de outliers (regla IQR); media se desplaza −8,9% al excluirlos, pero la conclusión de T1 (Welch) se mantiene significativa |
| Robustez al supuesto distribucional | EAD medio con Lognormal vs. Normal: −4,37% de diferencia |

## Equipo

| Integrante | Rol |
|---|---|
| Arturo Knopke Vera | Integrante |
| Nicolás Soletic Cobos | Integrante |
| Sebastián Navarrete Soto | Integrante |
| Roberto Moncada González | Integrante |

**Docente:** Jean Paul Maidana
