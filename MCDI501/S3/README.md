# Análisis de Incumplimiento de Clientes de Tarjetas de Crédito
### MCDI501: Estadística Computacional para la Toma de Decisiones
**Magíster en Ciencia de Datos e Inteligencia Artificial**

---

## Descripción del Proyecto

Este repositorio contiene el desarrollo de la **Evaluación Sumativa 3 (Final)** del curso MCDI501, centrada en **modelamiento predictivo integrado** sobre el dataset *Default of Credit Card Clients* (UCI, Taiwan 2005).

Esta fase **integra todo el proyecto**: reutiliza como insumos el análisis de faltantes, la matriz de correlaciones y los outliers identificados en la Sumativa 1, y las correlaciones estables y el bootstrap de la Sumativa 2, para construir y validar un **modelo de regresión logística** que estima la probabilidad de incumplimiento de pago.

| | |
|---|---|
| **Dataset** | Default of Credit Card Clients (UCI Machine Learning Repository, Taiwan 2005) |
| **Fase del proyecto** | Fase 4: Cierre del proyecto (Evaluación Sumativa 3 — Final) |
| **Resultado de aprendizaje** | RA3: integrar métodos estadísticos y de remuestreo en un modelo predictivo para apoyar decisiones de negocio |
| **Ponderación** | Evaluación final del curso |

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

El archivo utilizado es `data/raw/UCI_Credit_Card_con_faltantes.csv`, que introduce valores faltantes bajo mecanismo **MCAR** (semilla 42) en las variables `LIMIT_BAL` y `PAY_0` (12,5% cada una). A diferencia de S1/S2, en esta fase los faltantes **no se imputan de inmediato**: se dejan intactos hasta la Parte 1, donde se implementan y comparan tres estrategias de tratamiento (incluida imputación por regresión lineal múltiple). `data/raw/valores_originales_referencia.csv` contiene los valores reales pre-MCAR, usados como referencia externa para evaluar qué estrategia recupera mejor la información original.

## Estructura del Repositorio

```
S3/
├── data/
│   └── raw/
│       ├── UCI_Credit_Card_con_faltantes.csv   # Dataset con valores faltantes (MCAR)
│       ├── UCI_Credit_Card.csv                 # Dataset original sin faltantes
│       └── valores_originales_referencia.csv   # Valores originales de referencia (pre-MCAR)
├── figures/                                    # Figuras exportadas por f4_s03_template_informefinal.ipynb
│   ├── fig_diag_imputacion_LIMIT_BAL.png       # Diagnóstico de residuos — imputación por regresión (LIMIT_BAL)
│   ├── fig_diag_imputacion_PAY_0.png           # Diagnóstico de residuos — imputación por regresión (PAY_0)
│   ├── fig_comparacion_imputacion.png          # Comparación de estrategias A/B/C vs. referencia real
│   ├── fig_outliers_tratamiento.png            # LIMIT_BAL antes/después de transformación log1p
│   ├── fig_boot_ic_modelo.png                  # IC bootstrap vs. tradicional — coeficientes del modelo final
│   ├── fig_cooks_distance.png                  # Observaciones influyentes (distancia de Cook)
│   ├── fig_linealidad_logit.png                # Test de Box-Tidwell y logit empírico por deciles
│   ├── fig_matrices_confusion.png              # Matrices de confusión — M1, M2, M3
│   ├── fig_curvas_roc.png                      # Curvas ROC comparadas — M1, M2, M3
│   └── fig_impacto_imputacion_modelo.png       # AUC y coeficientes clave por estrategia de imputación
├── notebooks/
│   ├── F1_semana1.ipynb                        # Análisis EDA e inferencial (Sumativa 1)
│   ├── F2_semana2.ipynb                        # Validación, simulación y remuestreo (Sumativa 2)
│   └── f4_s03_template_informefinal.ipynb      # Modelamiento predictivo integrado (Sumativa 3 — esta fase)
├── src/
│   └── data_loading.py                         # Módulo de carga de datos (cargar_datos)
├── resultados_validados_S1.md                  # Resultados validados de S2, insumo de esta fase
└── requirements.txt                             # Dependencias del proyecto
```

## Instalación y Uso

### 1. Clonar el repositorio

```bash
git clone https://github.com/robertomoncada-blip/Magister_ciencia_datos.git
cd Magister_ciencia_datos/MCDI501/S3
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
jupyter lab notebooks/f4_s03_template_informefinal.ipynb
```

## Análisis Realizados (f4_s03_template_informefinal.ipynb)

El notebook está estructurado en 4 partes, precedidas por la carga de resultados de S1 y S2:

| Parte | Sección | Contenido | Puntaje |
|---|---|---|---|
| 0 | Carga de resultados de S1 y S2 | Reconstrucción del dataset crudo (con faltantes intactos) e insumos documentados de S1 (faltantes, correlaciones, outliers) y S2 (`resultados_validados_S1.md`: correlaciones estables, V de Cramér de `PAY_0`) | — |
| 1 | Manejo de Datos Faltantes | 1.1 Resumen de S1 · 1.2 Imputación por regresión lineal múltiple para `LIMIT_BAL` y `PAY_0` (con evaluación out-of-sample, VIF y diagnóstico de residuos) · 1.3 Comparación de 3 estrategias (A: eliminación, B: imputación simple, C: regresión) contra la referencia real pre-MCAR | 25 pts |
| 2 | Regresión Logística | 2.1 Preparación de datos (outliers, transformación log1p, escalado) · 2.2 Selección de variables (Modelo 1: 5 variables de S1/S2; Modelo 2: stepwise por p-valor; Modelo 3: stepwise por AIC) · 2.3 Bootstrap del modelo (1.000 remuestras, IC de coeficientes y Odds Ratios) · 2.4 Diagnóstico de supuestos (VIF, distancia de Cook, linealidad en el logit vía Box-Tidwell) · 2.5 Evaluación de desempeño (matrices de confusión, curvas ROC, comparación de modelos) | 50 pts |
| 3 | Análisis Comparativo de Imputación | Reajuste del modelo final bajo las 3 estrategias de la Parte 1 para evaluar si la elección de imputación cambia las conclusiones (coeficientes, AUC, ancho de IC) | 10 pts |
| 4 | Conclusiones Integradas | Síntesis S1→S2→S3, interpretación de Odds Ratios del modelo final, recomendaciones para toma de decisiones y limitaciones | — |
| — | Checklist de Integración | Verificación explícita del uso de insumos de S1 y S2 en cada sección | — |

Todas las semillas aleatorias (imputación por regresión, bootstrap, partición train/test) se fijan en `SEED = 42` para garantizar reproducibilidad exacta.

### Resultados destacados

| Análisis | Resultado |
|---|---|
| Imputación por regresión vs. simple (RMSE frente a valores reales) | LIMIT_BAL: 110.433 vs. 128.723 · PAY_0: 0,83 vs. 1,12 — la regresión recupera mejor el valor real y preserva el 100% de la muestra |
| Estrategia de imputación elegida | **C (regresión lineal múltiple)**: sin pérdida de muestra, menor RMSE y mejor preservación de la estructura de correlación real que B |
| Selección de variables | Los stepwise por p-valor (M2) y por AIC (M3) convergen a las mismas 7 variables: `PAY_0`, `PAY_AMT2_log`, `LIMIT_BAL_log`, `PAY_AMT1_log`, `MARRIAGE_soltero`, `EDU_otros`, `SEX_female` |
| Modelo final seleccionado | **M2 (stepwise por p-valor)** — AUC test = 0,726, Accuracy = 0,799, Precision = 0,642, Recall = 0,208, F1 = 0,315; VIF máximo = 1,24 (sin multicolinealidad) |
| Predictor dominante | `PAY_0` (OR = 2,02; IC 95% bootstrap [1,93; 2,11]): cada desviación estándar de atraso en el pago casi **duplica** las probabilidades relativas de incumplir |
| Diagnóstico de supuestos | 4,81% de observaciones sobre el umbral de Cook (ninguna domina el ajuste); Box-Tidwell no significativo (p=0,23) para `LIMIT_BAL_log`, consistente con linealidad en el logit |
| Robustez a la estrategia de imputación (Parte 3) | El signo e interpretación de los coeficientes se mantiene bajo A/B/C; no se observa evidencia de subestimación de varianza en la Estrategia C (ancho de IC ≈ idéntico a B) |
| `AGE` como predictor | No fue seleccionada por ningún procedimiento automático (stepwise ni AIC) — confirma, con las tres fases del proyecto, que no aporta señal útil por sí sola |

## Equipo

| Integrante | Rol |
|---|---|
| Arturo Knopke Vera | Integrante |
| Nicolás Soletic Cobos | Integrante |
| Sebastián Navarrete Soto | Integrante |
| Roberto Moncada González | Integrante |

**Docente:** Jean Paul Maidana
