# Validación con `validador-notebooks-rubrica`: Formativa 4 (S4)

- **Notebook:** `notebooks/mcdi505_s4rmoncada.ipynb` · **Dataset:** `consumo_electrico_litoral_depurado_s4.csv`
- **Rúbrica:** `notebooks/S4eje_profe/MCDI505_Formativa4_instrucciones_v2.pdf` (reemplaza la rúbrica de la Sumativa 1 que trae la skill)
- **Fecha:** 21 de octubre de 2026 · **Motor:** `nbclient` (kernel real del `.venv`), en una carpeta limpia con solo el notebook y el CSV

> Los niveles son **estimaciones**, no una calificación. En la Formativa 4 lo evaluado es el **borrador en PDF** (`entregas/mcdi505_s4rmoncada.pdf`); el notebook es su anexo. La evidencia se cita del notebook, cuyos textos se copiaron literalmente al PDF.

## 1. Resumen

**Run All: APROBADO** (nbclient, cero errores). Nivel estimado: **Excelente en los tres criterios de contenido (27/27)**. Pendiente principal: la **declaración de uso de IA** no describe todo el apoyo recibido.

## 2. Tabla por criterio (Formativa 4: 3 criterios de contenido; no se evalúan ortografía ni formato)

| Criterio | Nivel estimado | Evidencia citada | Brecha para subir o asegurar el nivel |
|---|---|---|---|
| **1. Problema, metodología y solución** (ID 4.1) | Excelente (9) | §4, bloque 1: «Decisión: elegir cuánta energía contratar para el año siguiente. Si se contrata menos de lo necesario, hay que comprar energía en el mercado spot, donde el precio puede ser entre 2 y 4 veces más alto. Si se contrata de más, se termina pagando energía que no se utiliza.» · «se analizaron 10 años de consumo mensual (2015-2024) con un modelo que reconoce la estacionalidad anual y el efecto de la pandemia» · «La propuesta es contratar un volumen algo mayor que el pronóstico (alrededor de 4 % más)» · Figura 1 (§1): serie, pronóstico 2024 e intervalo al 95 % | Ninguna obligatoria. Opcional: en el bloque 3, «cuantil 75 %» es jerga para la Gerencia |
| **2. Sustento técnico** (ID 3.2) | Excelente (9) | §2: Tabla 2 con B, A (S2), B + ARFIMA y B + GARCH (S3) y naive, con RMSE, MAE y MASE en 2023 y 2024 · §4, bloque 2: «El modelo tuvo el menor error en 2023 (RMSE 6,85 GWh)… fue el único candidato de la Semana 2 que, además de superar al naive, pasó la prueba de Ljung-Box.» · §2, «Cadena de evidencia» (incluida en el PDF): «ADF = −8,82 (frente al valor crítico −2,90) y KPSS = 0,040 (frente a 0,463)… no hubiera memoria larga (H = 0,652…) ni volatilidad condicional (ARCH-LM p = 0,639; S3)… MASE 0,61» | Ninguna |
| **3. Conclusiones y recomendaciones** (ID 4.1) | Excelente (9) | §4, bloque 3: «**Contratar el cuantil 75 %**, equivalente a 1.499,3 GWh para 2025, lo que representa un 4,1 % más que el consumo promedio esperado. Con esta estrategia, en 2024 el costo habría sido aproximadamente 39 % menor.» · «Como limitación, este resultado supone que el costo de quedarse corto es 3 veces mayor… y se basa en una prueba de solo 12 meses.» · §3: cinco limitaciones con su efecto | Ninguna |

## 3. Resultado de Run All

| Regla | Estado | Detalle |
|---|---|---|
| Ejecución limpia (carpeta nueva, kernel nuevo) | ✅ OK | nbclient, 0 errores |
| Orden y estado guardado | ✅ OK | `execution_count` = 1..9; todas las celdas con salida; sin salidas de error |
| Portabilidad | ✅ OK | Rutas relativas (`consumo_electrico_litoral_depurado_s4.csv`); semilla fija (`SEMILLA = 505`) |
| Consistencia de cifras (N1) | ✅ OK tras revisión manual | Las 8 cifras sin coincidencia literal (0,001; 0,03; 0,040; 0,463; 0,639; 0,652; 2,90; 8,82) están **citadas a la S2 o la S3** (ADF/KPSS, H, ARCH-LM, Jarque-Bera) o son **derivadas** de la Tabla 2 (diferencias ≤ 0,03 GWh) |
| Dependencias | ✅ OK | numpy, pandas, matplotlib, scipy, statsmodels del `.venv` |
| Advertencias silenciadas (R6) | ℹ️ Observación | `warnings.filterwarnings("ignore")` viene de la **plantilla oficial**; la ejecución no muestra errores ocultos |

**Veredicto: APROBADO.**

**Reglas de la skill que no aplican a esta evaluación** (están pensadas para la Sumativa 1): extensión de 10 a 15 páginas (la Formativa 4 es un PDF de una página más una de tabla y figura), secciones «introducción / ACF / descomposición / exploración / referencias» y «código comentado». Esta última marca 3 celdas sin comentarios (imports, carga de datos y evaluación), que son celdas de la **plantilla oficial** sin modificar.

## 4. Correcciones priorizadas

| Prioridad | Ubicación | Problema | Dato o sugerencia |
|---|---|---|---|
| **P1** | Declaración de uso de IA (última celda y página 2 del PDF) | La instrucción limita la IA a «organizar ideas o mejorar la redacción». La declaración dice «apoyo práctico para el código… borrador de ideas y guías de interpretación», pero **no menciona** que el asistente construyó las Tablas 2 a 4, la prueba retrospectiva de costos y el plan 2025, validó los textos («dice / debe decir») ni **armó el PDF** | Describirlo con exactitud. Que el código lo haya hecho la IA va más allá de lo que permite la instrucción: conviene **consultar al docente** en el foro. No se redacta aquí una declaración más favorable |
| P3 | Bloque 3 (§4 y PDF) | «cuantil 75 %» es jerga para la Gerencia | Explicarlo en palabras simples si se quiere |
| P3 | Celdas de código 0, 2 y 5 (plantilla) | Sin comentarios | Opcional: no se evalúa en la Formativa |

## 5. Pendientes que solo el autor puede confirmar

- **Plazo:** el PDF de instrucciones dice miércoles 21 de octubre a las 23:59; la guía de compañía lo movió al viernes 23.
- **Ejecución en su equipo:** las salidas guardadas ya muestran una ejecución completa 1..9; confirmar que el notebook adjunto es el mismo del ZIP (`entregas/mcdi505_s4rmoncada.zip`).
- **Retroalimentación:** el criterio y el alcance del uso de IA permitido, si se consulta al docente.

## Nota de calibración

La skill trae por defecto la rúbrica de la Sumativa 1. Para otras evaluaciones, conviene ajustar sus reglas automáticas (extensión, secciones esperadas) y probarla con 2 o 3 notebooks ya calificados, hasta que sus niveles coincidan con la nota real.
