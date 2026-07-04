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

## 3. Observaciones influyentes identificadas (jackknife)

Clientes con `LIMIT_BAL` en el percentil superior (hasta NT$1.000.000) concentran la mayor influencia individual sobre la media de `LIMIT_BAL`, aunque ninguna observación domina el resultado (desplazamiento marginal por observación < NT$30). Se recomienda para S3: (a) inspeccionar estos casos como parte de un análisis de outliers en el modelado predictivo, (b) evaluar transformaciones (log) o técnicas robustas (RobustScaler, modelos basados en árboles) menos sensibles a esta asimetría.

## 4. Recomendaciones metodológicas para S3

1. **Modelos predictivos**: priorizar `LIMIT_BAL`, el historial de pagos (`PAY_0`...`PAY_6`, no evaluado en profundidad aquí) y variables derivadas de las facturas por sobre variables débiles como `AGE`, cuya relación con el default es estadísticamente detectable pero de magnitud práctica despreciable.
2. **Manejo de outliers**: no eliminar automáticamente los outliers de `LIMIT_BAL` — el análisis de robustez muestra que, si bien desplazan la media puntual, no afectan la significancia de las pruebas de hipótesis; considerar en su lugar transformaciones o modelos robustos a colas pesadas.
3. **Supuestos distribucionales**: al construir estimaciones de riesgo/exposición (p. ej. pérdida esperada), usar Lognormal u otra distribución de cola derecha en lugar de Normal para variables monetarias, dado que la elección de distribución cambia los resultados en ~4%.
4. **Validación continua**: mantener el patrón de esta Sumativa 2 (bootstrap/permutación) como chequeo de sanidad cuando se reentrenen modelos en S3, especialmente si cambia el tamaño o la composición de la muestra.
5. **Limitación pendiente**: no se dispone de una tasa de recuperación / *loss given default* (LGD) estimada; el EAD de la Sección 4 debe interpretarse como exposición, no como pérdida neta esperada, hasta que S3 incorpore ese parámetro.
