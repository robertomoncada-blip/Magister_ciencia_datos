# Validación: `mcdi505_s2rmoncada.ipynb` frente a la Sumativa 2 (instrucciones v2 y rúbrica)

- **Fecha de revisión:** 14 de octubre de 2026
- **Versión revisada:** archivo de trabajo con las ediciones del autor posteriores al commit `cc74161`, sin marcas `[REVISAR]`
- **Ejecución de control:** «Reiniciar kernel y ejecutar todo» con kernel nuevo, sobre una copia. **5/5 celdas de código, ejecutadas en orden y sin errores**
- **Documento de referencia:** `MCDI505_Sumativa2_instrucciones_v2.pdf`, con 6 criterios de 9 puntos cada uno (total 54)
- **Alcance:** cumplimiento de cada criterio, concordancia de las cifras del texto con las salidas, extensión y estructura, y declaración de uso de IA. Es una estimación de cumplimiento, no una nota.

## Segunda revisión (14 de octubre, después de las correcciones del autor)

**Ejecución de control:** con kernel nuevo, sobre una copia: 5/5 celdas sin errores. El autor eliminó la celda de propuesta, así que el notebook vuelve a tener 21 celdas y la Hoja es la primera sección. Todas las cifras siguen coincidiendo con las salidas.

| # | Criterio | Nivel probable | Puntaje | Cambio respecto de la primera revisión |
|---|---|---|---|---|
| 1 | Estacionariedad | Excelente | 9 | La regla de la fila 1 de la Hoja sigue sin la condición ACF(12) < 0,5 |
| 2 | Identificación | Excelente | 9 | La redacción de la §2 quedó corregida por completo |
| 3 | Selección | Excelente | 9 | La redacción de la §3 quedó corregida. La fila 3 de la Hoja todavía no cita las métricas de 2023 (opcional) |
| 4 | Diagnóstico | Excelente | 9 | Quedan 2 errores menores |
| 5 | Ortografía y redacción | Excelente, al límite | 9 (6 si se acumulan los menores) | De ~25 errores quedan **9 menores** (tabla siguiente) |
| 6 | Formato y entrega | Excelente | 9 | Extensión OK; falta regenerar el ZIP |
| | **Total estimado** | | **51-54 / 54** | |

**Extensión:** las interpretaciones tienen §1 **247** · §2 **245** · §3 200 · §4 198 palabras. La §1 subió 5 palabras y queda a 3 del límite: no agregar nada más ahí.

### Correcciones aplicadas por el autor ✅
- La frase sin verbo del contexto quedó «Se utiliza la variable consumo_gwh…».
- §1: «valor que por sí solo no permite decidir», «Como λ ≈ 0» y «Como se observa en la Tabla 1».
- §2: «evidenció», «A partir de», «El modelo G… se incluyó», «En el modelo A», «Por otro lado, los parámetros».
- §3: «Como referencia», sin espacio inicial, «Los modelos E y F también», «Frente al naive», «En la validación 2023» y «Por último, el ARIMA».
- §4: «Además,» (sin la «Y» inicial).
- Hoja, fila 1: «se eligieron d y D» y el espacio en «D = 1. |».
- Declaración: «práctico».

### Pendientes de redacción
| Celda | Texto actual | Corrección |
|---|---|---|
| Hoja, fila 1 | «Se aplicó logaritmo» | «Se aplicó el logaritmo» |
| Hoja, fila 1 | «aunque pasan ADF.\|» | Espacio antes de la barra |
| 4 · Contexto | «noviembre 2017  y» | «noviembre de 2017 y» |
| 7 · §1 | «**Interpretacion** de la estacionariedad.» | «Interpretación» (tilde) |
| 7 · §1 | «KPSS  (Kwiatkowski» y «p-valor  de» | Quitar dobles espacios |
| 13 · §3 | «Por último, se seleccionó…» y luego «Por último, el ARIMA…» | Repetido: cambiar el primero por «Finalmente, se seleccionó» |
| 16 · §4 | «Como **Ambos** valores» | «Como ambos valores» |
| 16 · §4 | «Por otro lado, prueba ARCH-LM» | «Por otro lado, la prueba ARCH-LM» |
| 18 · Conclusiones | «airline»).  En la» | Quitar el doble espacio |
| 20 · Declaración | «autocontenido.  Además» y «resultados.  Por último» | Quitar dobles espacios |

### Sin cambios desde la primera revisión
- **Hoja, fila 1 (criterio 1):** agregar «con ACF(12) menor que 0,5» a la regla, igual que en el código.
- **Hoja, fila 3 (opcional):** «En 2023: RMSE 6,85 frente a 7,26 GWh y MAE 6,40 frente a 6,53 GWh del naive estacional».
- **Declaración de IA (sección 4 de la primera revisión):** sigue sin nombrar la herramienta y sigue diciendo que las interpretaciones y conclusiones son «análisis propio». Es el punto de mayor riesgo frente a la regla de uso de IA de las instrucciones.
- **ZIP de entrega:** regenerarlo con la versión final.

---

# Primera revisión (14 de octubre)

## Resumen

| # | Criterio | Nivel probable | Puntaje | Pendiente principal |
|---|---|---|---|---|
| 1 | Estacionariedad y transformaciones (ID 2.2) | Excelente | 9 | La regla de la Hoja (fila 1) omite la condición ACF(12) < 0,5 que aplica el código |
| 2 | Identificación y estimación (ID 2.1) | Excelente | 9 | — |
| 3 | Selección y comparación (ID 2.1) | Excelente | 9 | Opcional: citar en la Hoja (fila 3) las métricas de 2023 que piden las instrucciones |
| 4 | Diagnóstico de residuos (ID 2.2) | Excelente | 9 | — |
| 5 | Ortografía y redacción | **Bueno** | **6** | ~20 errores nuevos de las últimas ediciones: tildes, una frase sin verbo, conectores y dobles espacios |
| 6 | Formato y entrega | Excelente | 9 | Regenerar el ZIP de entrega |
| | **Total estimado** | | **51 / 54** (54 si se corrige la redacción) | |

Aparte de la rúbrica queda la **declaración de uso de IA**: las instrucciones permiten la IA «únicamente para organizar ideas o mejorar la redacción», y la declaración actual no describe todo el uso que hubo (sección 4).

**Cifras:** todas las cifras del texto y de la Hoja coinciden con las salidas de la ejecución. Entre ellas: ADF/KPSS 0,391/0,100; desviaciones estándar 0,047/0,065/0,079; efecto COVID de −4,2 % a −6,7 %; RMSE móvil 5,87/7,05/7,12/7,11/7,72 GWh; reducción de 7,9 %; métricas 2023 de 6,85/7,26 y 6,40/6,53 GWh; RMSE móvil del ARIMA 31,95 GWh; y las pruebas de la Tabla 4.

---

## 1. Requisitos de formato (instrucciones v2)

| Requisito | Estado | Detalle |
|---|---|---|
| `.ipynb` ejecutable desde un kernel reiniciado | ✅ | 5/5 celdas, sin errores |
| Estructura: Hoja → contexto → 4 secciones en el orden de la rúbrica → conclusiones → referencias → declaración de IA | ✅ | Celdas 1, 4, 5-16, 17-18, 19 y 20 |
| Por sección: hasta 3 figuras | ✅ | §1: 2 · §2: 1 · §3: 1 · §4: 1 |
| Por sección: una tabla | ✅ | Tablas 1 a 4, una por sección |
| Por sección: hasta 250 palabras de interpretación | ✅ ajustado | Interpretaciones: §1 **242** · §2 **246** · §3 203 · §4 198. Si el corrector suma el párrafo introductorio de cada sección, §1 llega a 309 y §2 a 300. Conviene no agregar texto a §1 ni §2 |
| Nombre `mcdi505_s2inicialapellido` | ✅ | `mcdi505_s2rmoncada.ipynb` |
| Referencias APA, todas citadas en el texto | ✅ | Las 13 entradas se citan |
| Partición 2015-2022 / 2023, sin usar 2024 | ✅ | Celda 3 |
| ZIP de entrega actualizado | ⚠️ | `entregas/mcdi505_s2rmoncada.zip` es de las 11:58 y no tiene las ediciones posteriores |

## 2. Contenido técnico por criterio

### Criterio 1: Estacionariedad (Excelente)
ADF y KPSS se aplican e interpretan en conjunto. El texto aclara el p-valor truncado y la H0 del KPSS según la regresión. La elección del logaritmo se justifica con λ y con la elasticidad, y d = 1 y D = 1 se verifican con el criterio de varianza.

- ⚠️ **Inconsistencia con el código:** la fila 1 de la Hoja define la regla como «la mínima diferenciación necesaria … según ADF y KPSS». El código (celda 6) exige además **ACF(12) < 0,5**. Agregar: «… según ADF y KPSS, con ACF(12) menor que 0,5».

### Criterio 2: Identificación y estimación (Excelente)
Hay 7 candidatos, 3 o más como piden las instrucciones, que cubren las familias AR, MA, ARMA, ARIMA y SARIMA. La identificación se apoya en la ACF y la PACF (rezago 12; G como contraste), todos los modelos usan covid como regresor y se reporta la invertibilidad.

### Criterio 3: Selección y comparación (Excelente)
La comparación usa AIC, BIC, RMSE y MAE de 2023 con el naive estacional como referencia, y además el origen móvil, que las instrucciones mencionan para profundizar. La elección de B se justifica con cifras.

- Opcional: la fila 3 de la Hoja cita solo las métricas con origen móvil. Como las instrucciones piden RMSE y MAE de 2023, conviene agregar «En 2023: RMSE 6,85 frente a 7,26 y MAE 6,40 frente a 6,53 GWh del naive». Ojo: en 2023, C tiene menor RMSE (6,46) que B; el texto ya explica que C no es elegible por Ljung-Box.
- La fila 3 todavía tiene la nota «*Ajuste respecto de la versión anterior: …*». Se puede quitar o dejar como evidencia de la corrección pedida.

### Criterio 4: Diagnóstico (Excelente)
Incluye Ljung-Box en los rezagos 12 y 24 (con los parámetros descontados), Jarque-Bera y Shapiro-Wilk, ARCH-LM y la prueba F, la sensibilidad sin marzo-junio de 2020 y la cobertura del intervalo. La conclusión sobre la validez del modelo es explícita.

## 3. Criterio 5: ortografía y redacción (pendientes)

Todos los errores son de las ediciones recientes.

| Celda | Texto actual | Corrección |
|---|---|---|
| 1, fila 1 | «Se aplicó logaritmo y eligió d y D» | «Se aplicó el logaritmo y se eligieron d y D» |
| 1, fila 1 | «D = 1.\|» / «pasan ADF.\|» | Agregar un espacio antes de `\|` (formato) |
| 4 | «noviembre 2017  y» | «noviembre de 2017 y» |
| 4 | «**Se la variable** consumo_gwh y el periodo estacional es de 12 meses.» | «Se utiliza la variable consumo_gwh, con un periodo estacional de 12 meses.» (**falta el verbo**) |
| 7 | «**Interpretacion estacionariedad.**» | «**Interpretación de la estacionariedad.**» |
| 7 | «obteniendo λ = 0,00 (…), por sí solo no permite decidir» | «… λ = 0,00 (…), valor que por sí solo no permite decidir» |
| 7 | «**Cómo** λ ≈ 0» | «**Como** λ ≈ 0» (causal, sin tilde) |
| 7 | «Se observa en la Tabla 1, la serie…» | «Como se observa en la Tabla 1, la serie…» |
| 7 | «1979)  y KPSS  (» · «p-valor  de» | Quitar los dobles espacios |
| 10 | «La ACF **evidencio**» | «evidenció» |
| 10 | «A contar de esta identificación» | «A partir de esta identificación» (más formal) |
| 10 | «**Para el modelo G**, con AR estacional, **se incluyó** como contraste» | «El modelo G, con AR estacional, se incluyó como contraste» |
| 10 | «Para el modelo A, la COVID-19 produjo» | «En el modelo A, la COVID-19 produjo» |
| 10 | «Por otro lado los parámetros» | «Por otro lado, los parámetros» |
| 11 | «Para referenciar se utilizó el pronóstico naive» | «Como referencia se utilizó el pronóstico naive» |
| 13 | « El modelo A» (espacio inicial) | Quitar el espacio |
| 13 | «**En cambio** los modelos E y F **también** superaron» | «Los modelos E y F también superaron…» («en cambio» contradice «también») |
| 13 | «**Sobre al** naive estacional (7,72 GWh)» | «Frente al naive estacional (7,72 GWh)» |
| 13 | «**En cambio** en la validación 2023, B también superó» | «En la validación 2023, B también superó» |
| 13 | «**Y el** ARIMA sin estacionalidad» | «Por último, el ARIMA sin estacionalidad» |
| 16 | «Ambos valores son mayores que 0,05, no se rechaza…» | «Como ambos valores son mayores que 0,05, no se rechaza…» |
| 16 | «Por otro lado prueba ARCH-LM» | «Por otro lado, la prueba ARCH-LM» |
| 16 | «**Y Además**, el intervalo» | «Además, el intervalo» |
| 18 | «covid.  El efecto» · ««airline»).  En la» | Quitar los dobles espacios |
| 20 | «apoyo **practico**» | «práctico» |

## 4. Declaración de uso de IA (instrucciones: «Uso de IA»)

> «No se permite emplear herramientas automatizadas de generación de contenidos (IA generativa) para producir respuestas completas; estas herramientas podrán utilizarse únicamente para organizar ideas o mejorar la redacción, siempre que se declare su uso al final del notebook.»

| Aspecto | Estado | Detalle |
|---|---|---|
| Declaración al final del notebook | ✅ | Celda 20 |
| Nombra la herramienta | ❌ | No dice cuál: Claude (Anthropic), en Claude Code |
| Describe todo el uso | ❌ | Dice que la IA se usó para el código y que «las interpretaciones y conclusiones fueron realizadas mediante análisis propio». La comparación con tu versión del 11 de octubre muestra que el asistente también redactó la **Hoja de decisiones** (filas 2-4 casi sin cambios respecto de su borrador), escribió frases y cifras de las §1-§4 y de las conclusiones (por ejemplo, el criterio de varianza, el modelo G, E y F, y la validación 2023) y la lista de **referencias** |
| Uso dentro de lo permitido | ⚠️ | Generar el código y redactar partes del texto va más allá de «organizar ideas o mejorar la redacción». Esto no se corrige solo con la declaración. Si hay dudas, conviene consultarlo en el foro «Consultas al docente» antes de la entrega |

**Recomendación:**
1. Reescribir con tus palabras las frases y filas que redactó el asistente (las que estaban marcadas con `[REVISAR]`), en especial la Hoja.
2. Ajustar la declaración para que nombre la herramienta y diga con exactitud qué hizo: código de las cuatro secciones, borrador de la Hoja y de las referencias, y revisión de redacción y cifras de las interpretaciones.
3. Corregir «práctico» y los dobles espacios de la celda 20.

## 5. Antes de entregar

1. Corregir la redacción (sección 3) y la regla de la fila 1 de la Hoja (criterio 1).
2. Resolver la declaración de IA (sección 4).
3. Volver a contar las palabras de §1 y §2 (≤ 250).
4. Reiniciar el kernel y ejecutar todo; guardar con las salidas.
5. Regenerar `entregas/mcdi505_s2rmoncada.zip` (notebook + CSV depurado).
6. Revisar `git status`: `mcdi505_s2rmoncadaV1.ipynb` aparece borrado en el árbol de trabajo. Si no fue intencional, recuperarlo con `git restore`.
