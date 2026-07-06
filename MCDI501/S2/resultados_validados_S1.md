# Resultados Validados — Entrada para la Sumativa 3

Generado automáticamente desde `notebooks/F2_semana2.ipynb` (Sumativa 2).
Todos los parámetros provienen del dataset `data/raw/UCI_Credit_Card_con_faltantes.csv`
tras el preprocesamiento de la Sumativa 1 (imputación mediana/moda, n = 30,000).

## 1. Parámetros robustamente estimados

| Parámetro | Estimación puntual | IC 95% bootstrap (BCa) | Validación |
|---|---|---|---|
| Proporción de default | 0.2212 (22.12%) | [0.216 ; 0.226] | Bootstrap ≈ Wilson clásico; muy estable |
| Media LIMIT_BAL | NT$164,247 | [162,844.410 ; 165,583.814] | Bootstrap ≈ t-Student clásico; sensible a outliers (usar con cautela si se excluyen outliers, ver Sección 5) |
| Diferencia LIMIT_BAL (No Default − Default) | NT$42,374 (d Cohen=0.363) | — | Confirmada por Welch t-test, permutación (p=0.0002) y robusta a outliers |
| Media AGE | 35.49 años | [35.381 ; 35.589] | Bootstrap ≈ t-Student clásico |

## 2. Correlaciones estables (usar en modelos predictivos de S3)

| Par | r | Estabilidad |
|---|---|---|
| BILL_AMT1 – BILL_AMT2 | 0.951 | Muy alta — candidata a colinealidad si se usan ambas en un modelo |
| LIMIT_BAL – DEFAULT | -0.144 | Alta — variable predictiva más confiable identificada hasta ahora |
| AGE – LIMIT_BAL | 0.136 | Alta pero débil en magnitud |

**Correlación inestable — usar con cautela:** AGE – DEFAULT (r=0.014), amplitud relativa del IC ≈169%. No se recomienda como variable predictiva relevante por sí sola.

## 3. Historial de pagos (PAY_0–PAY_6) — hallazgo nuevo de esta fase (Sección 6.1)

No evaluado en S1 ni en las Secciones 1–5 de esta fase. `PAY_0` resultó ser **la variable con la asociación más fuerte y más estable con el incumplimiento de todo el análisis**:

| Variable | V de Cramér vs. DEFAULT | IC 95% bootstrap | Amplitud relativa |
|---|---|---|---|
| PAY_0 (más reciente) | 0.390 | [0.3779 ; 0.4027] | 6.4% |
| PAY_2 | 0.340 | [0.3277 ; 0.3538] | 7.7% |
| PAY_6 (más antiguo) | 0.251 | [0.2380 ; 0.2647] | 10.7% |

`PAY_0` (V ≈ 0.39) supera en magnitud de asociación a `LIMIT_BAL`–`DEFAULT` (r = -0,144) por más de 2,5 veces, con una amplitud relativa de IC (6.4%) más baja que cualquier correlación no monetaria de la Sección 3.1. La tasa de incumplimiento salta de forma no lineal entre "sin atraso" (~13%–17%) y "con atraso" (34%–77%), y las seis variables están fuertemente autocorrelacionadas entre sí (ρ Spearman hasta 0,82 entre meses consecutivos) — **no usarlas todas sin control de colinealidad** en un modelo lineal para S3.

## 4. Observaciones influyentes identificadas (jackknife)

Clientes con `LIMIT_BAL` en el percentil superior (hasta NT$1.000.000) concentran la mayor influencia individual sobre la media de `LIMIT_BAL`, aunque ninguna observación domina el resultado (desplazamiento marginal por observación < NT$30). Se recomienda para S3: (a) inspeccionar estos casos como parte de un análisis de outliers en el modelado predictivo, (b) evaluar transformaciones (log) o técnicas robustas (RobustScaler, modelos basados en árboles) menos sensibles a esta asimetría.

## 5. Recomendaciones metodológicas para S3

1. **Modelos predictivos**: priorizar `PAY_0` (la variable individual más fuertemente asociada al incumplimiento encontrada en esta fase, ver Sección 3 de este informe), `LIMIT_BAL` y variables derivadas de las facturas, por sobre variables débiles como `AGE`. Evitar incluir `PAY_0`...`PAY_6` completas sin control de colinealidad, dada su fuerte autocorrelación mensual (ver Sección 3).
2. **Manejo de outliers**: no eliminar automáticamente los outliers de `LIMIT_BAL` — el análisis de robustez muestra que, si bien desplazan la media puntual, no afectan la significancia de las pruebas de hipótesis; considerar en su lugar transformaciones o modelos robustos a colas pesadas.
3. **Supuestos distribucionales**: al construir estimaciones de riesgo/exposición (p. ej. pérdida esperada), usar Lognormal u otra distribución de cola derecha en lugar de Normal para variables monetarias, dado que la elección de distribución cambia los resultados en ~4%.
4. **Validación continua**: mantener el patrón de esta Sumativa 2 (bootstrap/permutación) como chequeo de sanidad cuando se reentrenen modelos en S3, especialmente si cambia el tamaño o la composición de la muestra.
5. **Limitación pendiente**: no se dispone de una tasa de recuperación / *loss given default* (LGD) estimada; el EAD de la Sección 4 debe interpretarse como exposición, no como pérdida neta esperada, hasta que S3 incorpore ese parámetro.
