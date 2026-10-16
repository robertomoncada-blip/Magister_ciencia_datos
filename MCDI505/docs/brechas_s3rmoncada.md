# Brechas por corregir: `mcdi505_s3rmoncada.ipynb` (Semana 3, ARFIMA / GARCH)

- **Fecha de revisión:** 14 de octubre de 2026 (miércoles: hoy se entrega la Hoja de decisiones, Formativa 3)
- **Versión revisada:** archivo sin commit, con todas las salidas de la ejecución guardadas
- **Ejecución de control:** «Reiniciar kernel y ejecutar todo» con kernel nuevo. **Las 8 celdas de código corren en orden y sin errores**
- **Referencias de control:** notebook de la S2 (`mcdi505_s2rmoncada.ipynb`), plantilla del profesor (`S3eje_profe/mcdi505_s3_plantilla.ipynb`) y guía de compañía de la Semana 3 (`S3eje_profe/MCDI505_S3_guia_de_compania.pdf`), incluida su tabla «Errores frecuentes de la IA en esta unidad»
- **Fuera de alcance:** el PDF de instrucciones de la Formativa y la Sumativa 3, que no está en el repositorio. Según la guía es el único documento evaluativo y prevalece sobre todo lo demás; revisar contra él la extensión, el formato y el nombre del archivo.

---

# Sexta revisión (16 de octubre): reinicio de kernel + ejecutar todo y verificación de las instrucciones específicas

**Ejecución:** kernel reiniciado y «ejecutar todo» **sobre el archivo**: 9/9 celdas de código, en orden (1 a 9) y sin errores. Las salidas quedaron guardadas.

### Instrucciones específicas, punto por punto

| Criterio | Lo que pide la instrucción | Dónde se cumple | Estado |
|---|---|---|---|
| 1 | ACF de los residuos hasta el rezago 36 | Figura 1b | ✅ |
| 1 | Hurst y d = H − 0,5 | H = 0,652; d = 0,152 | ✅ |
| 1 | Interpretar considerando el tamaño de la muestra | Simulación de 500 ruidos blancos con n = 83 (Figura 2) | ✅ |
| 1 | ARFIMA(0,d,0) sobre los residuos, como contraste | «estimado como contraste»; −0,24 GWh | ✅ |
| 1 | Concluir sobre presencia o ausencia | «no hay evidencia de memoria larga» | ✅ |
| 2 | ACF de los residuos² | Figura 3b | ✅ |
| 2 | Ljung-Box (12) y ARCH-LM sobre los cuadrados | p = 0,485 y 0,639 | ✅ |
| 2 | GARCH(1,1): ω, α, β y α + β | 0,457; 0,066; 0,442; 0,509 | ✅ |
| 2 | Revisar los residuos estandarizados | Ljung-Box z 0,562, z² 0,654; ARCH-LM 0,832 (Figura 4) | ✅ |
| 2 | Interpretar en el contexto del consumo eléctrico | Párrafo sobre el segmento comercial y el covid como cambio de nivel | ✅ |
| 3 | Tabla: SARIMA, SARIMA + ARFIMA y naive con RMSE y MAE en GWh | Tabla 1 (única) | ✅ |
| 3 | Cobertura y ancho del IC 95 %: SARIMA frente a SARIMA + GARCH | Tabla 1 | ✅ |
| 3 | Qué mejora cada aspecto, qué diferencias son sustantivas y qué limitaciones conserva cada uno | Párrafos 2-4 | ✅ |
| 4 | Selección que integra dependencia, volatilidad, métricas y diagnóstico (no una sola métrica) | Párrafo 2 | ✅ |
| 4 | Pronóstico 2023 con su intervalo | Tabla 2 y Figura 6 | ✅ |
| 4 | Interpretarlo en el contexto del caso | Párrafo 3 con cifras (sesgo de 5,9 %, intervalo de 26 %) | ✅ (opcional: implicancia para DEL) |
| 4 | Limitaciones; modelo para la Semana 4 | Párrafo 4 | ✅ |
| 6 | Hoja primero; punto de partida; 4 secciones; conclusiones; referencias; declaración | Estructura | ✅ |
| 6 | ≤ 3 figuras, 1 tabla y ≤ 250 palabras por sección | §1: 2 / 0 / 200 · §2: 2 / 0 / 245 · §3: 1 / 1 / 244 · §4: 1 / 1 / 231 | ✅ |
| 6 | Nombre `mcdi505_s3inicialapellido`; APA | `mcdi505_s3rmoncada.ipynb`; 11 referencias, todas citadas | ✅ |

### Criterios de la rúbrica

| # | Criterio | Nivel probable | Puntaje |
|---|---|---|---|
| 1 | Memoria larga | Excelente | 9 |
| 2 | Volatilidad | Excelente | 9 |
| 3 | Contraste | Excelente | 9 |
| 4 | Selección | Excelente | 9 |
| 5 | Redacción | Excelente, con 3 detalles menores | 9 |
| 6 | Formato | Excelente | 9 |
| | **Total estimado** | | **~54 / 54** |

**Resuelto desde la quinta revisión:** las 255 palabras de la §3 (ahora 244), la conclusión 5 reescrita, el «Por ello» de la §4 movido, «Por otro lado,», el «;;» de la Hoja, «−0,981» en la §4 y la coma de «Claude Code,».

**Pendientes (con borrador en el notebook solo en estas 3 secciones):**
1. Punto de partida: «(-0,981)» → «(−0,981)».
2. §4: «con datos 2015-2023» → «con datos de 2015-2023». Opcional: una frase corta sobre la implicancia para DEL.
3. Declaración: «guias» → «guías»; «Sin embargo las» → «Sin embargo, las»; mencionar las propuestas de corrección del asistente.

**Fuera de lo verificable aquí:** que la Hoja incorpore la retroalimentación de la Formativa 3 (no está en el repositorio) y la entrega en plazo (domingo 18, 23:59).

---

# Quinta revisión (16 de octubre): rúbrica de la Sumativa 3, tras las correcciones del autor

**Ejecución de control:** con kernel nuevo, sobre una copia: 9/9 celdas sin errores. Todas las cifras coinciden con las salidas.

| # | Criterio | Nivel probable | Puntaje | Estado |
|---|---|---|---|---|
| 1 | Memoria larga | Excelente | 9 | ✅ Completo: ACF, H y d, simulación por tamaño de muestra, ARFIMA como contraste y Ljung-Box con parámetros descontados |
| 2 | Volatilidad | Excelente | 9 | ✅ **C2 resuelto por el autor** (contexto del consumo eléctrico); C3 citado. Queda una coma mal puesta |
| 3 | Contraste | Excelente | 9 | ✅ **C4 resuelto** (limitaciones de cada modelo y MAE del naive); tabla única |
| 4 | Selección | Excelente | 9 | ✅ **C5 resuelto** (pronóstico 2023 con cifras). Detalle: el «Por ello, se descartan…» quedó después del párrafo del pronóstico |
| 5 | Redacción | Bueno → Excelente | 6-9 | 7 detalles menores (ver abajo) |
| 6 | Formato | **Bueno** | **6** | ⚠️ **§3 tiene 255 palabras (máximo 250)**. Lo demás cumple: una tabla y ≤ 3 figuras por sección, Hoja primero, referencias APA todas citadas |
| | **Total estimado** | | **~48-51 / 54** | **54** con los ajustes |

**Resueltas desde la cuarta revisión:** C1, C2, C3, C4, C5, F2, B3, R1-R5, la fila 3 de la Hoja (sentido y cobertura del 100 %) y las cifras cruzadas de la §2. Se eliminaron las referencias sin cita (Sheppard; Hyndman et al., 2026).

**Pendientes (todos con «Donde dice / Debe decir» en el borrador bajo cada sección):**
1. **§3: 255 palabras.** Acortar la frase de la Semana 2 y «anchos de intervalo»; quedan 244 (verificado).
2. **Conclusión 5:** quedó copiada la instrucción «Agregar otras limitaciones:» y falta el punto final.
3. **§4:** mover «Por ello, se descartan…» al final del segundo párrafo; «datos de 2015-2023»; «−0,981».
4. **§2:** «Por otro, lado» → «Por otro lado,».
5. **Hoja, fila 3:** «;;» y «Tabla 1» repetida.
6. **Punto de partida:** «−0,981».
7. **Declaración:** «Claude Code, como apoyo», «guías», «Sin embargo, las» y mencionar las propuestas de corrección del asistente.

---

# Cuarta revisión (16 de octubre): cambios de código aplicados y propuestas «Donde dice / Debe decir»

**Código aplicado por el asistente** (ejecutado completo con kernel nuevo, 9/9 celdas sin errores):

| Brecha | Cambio | Resultado |
|---|---|---|
| C1 | Ljung-Box de los residuos con `model_df=2`, como en la S2 | p = 0,355 / 0,061 / 0,076 |
| C3 | Ljung-Box sobre los residuos estandarizados en nivel | p = 0,562 / 0,121 |
| F2 | Una sola tabla de contraste en la §3 (RMSE, MAE, ΔRMSE, cobertura, ancho, meses dentro); la tabla de la §4 pasa a ser la Tabla 2 | Ver Tabla 1 |
| M3 | **No aplicado**: la rúbrica no lo exige y se mantiene exp(μ), como en la plantilla. Se propone reconocer en el texto que el naive tiene menor MAE | — |

**Propuestas en el notebook:** 9 celdas destacadas, una bajo cada sección (Hoja, punto de partida, §1-§4, conclusiones, referencias y declaración). Cada una tiene una tabla «Donde dice / Debe decir / Motivo» construida sobre el texto actual del autor, y cada «Donde dice» se verificó como texto literal. El contenido que falta según la rúbrica (C2, C4, C5) aparece como filas **[AUTOR]** con ideas y cifras, no como texto redactado.

**Hallazgos nuevos en las ediciones del autor:**
- **Hoja, fila 3, «Alternativa descartada»:** el sentido quedó invertido. «Se consideró una mejora si el RMSE disminuyó…» dice que sí se consideró mejora, y el RMSE del ARFIMA subió.
- **Hoja, fila 3, evidencia:** «cobertura del 95 % (12/12)» es incorrecto: 12/12 es 100 %.
- **§2, cifras cruzadas:** el párrafo de los residuos² (Figura 3) cita las pruebas de los residuos estandarizados (0,654 / 0,562 / 0,832); corresponden 0,485 y 0,639.
- ✅ La fila 1 de la Hoja ya tiene 5 columnas (F1b resuelta por el autor).

---

# Tercera revisión: rúbrica de la Sumativa 3 (16 de octubre, tras las ediciones del autor)

- **Ejecución de control:** con kernel nuevo, sobre una copia: 9/9 celdas sin errores. Las cifras de los textos coinciden con las salidas
- **Cambios del autor desde la segunda revisión:** queda **una sola Hoja**, con redacción propia en las filas 1 y 2. La **declaración de IA** ahora nombra Claude Code y menciona borradores. El código, las interpretaciones y las conclusiones no cambiaron
- **Propuestas en el notebook:** la propuesta única del final se reemplazó por **8 celdas destacadas, una bajo cada sección con brecha**: Hoja, §1, §2, §3, §4, Conclusiones, Referencias y Declaración. Las celdas del autor no se modificaron (verificado). Las propuestas traen correcciones de redacción, cambios de código e **ideas y cifras para organizar** los textos que faltan (C2, C4 y C5), no párrafos redactados, de acuerdo con la regla de uso de IA de las instrucciones

| # | Criterio | Nivel probable | Puntaje | Cambio respecto de la segunda revisión |
|---|---|---|---|---|
| 1 | Memoria larga | Excelente | 9 | Sin cambios: C1 y R1 pendientes |
| 2 | Volatilidad | Bueno | 6 | Sin cambios: C2 y C3 pendientes |
| 3 | Contraste | Bueno | 6 | Sin cambios: C4 y F2 pendientes |
| 4 | Selección | Bueno | 6-9 | Sin cambios: C5 pendiente |
| 5 | Redacción | Bueno | 6 | R1-R6, más «guias» y «Sin embargo las» en la declaración |
| 6 | Formato | **Bueno** | **6** (antes 3) | ✅ Una sola Hoja. ⚠️ **Fila 1 de la Hoja rota** (4 columnas, F1b); F2; B3 |
| | **Total estimado** | | **~39-42 / 54** | **~54** si se resuelven las brechas |

**Brecha nueva, F1b:** en la fila 1 de la Hoja falta la barra `|` entre la evidencia y «Agregar un ARFIMA(0,d,0) con d = 0,152». La fila queda con 4 columnas y la tabla se desplaza.

**Declaración de IA (D):** mejoró. Queda una precisión: dice «borrador de ideas y guías de interpretación», pero el asistente preparó borradores de texto completos de la Hoja, el punto de partida, las interpretaciones y las conclusiones, y la lista de referencias. Las filas 3 y 4 de la Hoja conservan frases idénticas al borrador.

---

# Segunda revisión: rúbrica de la Sumativa 3 (instrucciones v2)

- **Fecha:** 16 de octubre de 2026. Plazo de entrega: domingo 18 a las 23:59
- **Versión revisada:** archivo de trabajo con las interpretaciones, el punto de partida y las conclusiones ya reescritos por el autor (sin commit)
- **Ejecución de control:** con kernel nuevo, sobre una copia: **9/9 celdas de código, en orden y sin errores**
- **Documento de referencia:** `MCDI505_Sumativa3_instrucciones_v2.pdf`, con 6 criterios de 9 puntos (total 54). Reemplaza la «Fuera de alcance» de la primera revisión
- **Cifras:** todas las cifras de los textos del autor coinciden con las salidas. La excepción es Ljung-Box, que queda bien con la salida actual pero no con la S2 (C1)

## Resumen

| # | Criterio | Nivel probable | Puntaje | Brechas que lo limitan |
|---|---|---|---|---|
| 1 | Memoria larga (ID 3.1) | Excelente | 9 | C1 (Ljung-Box sin descontar parámetros) y R1 (frase rota) |
| 2 | Volatilidad (ID 3.1) | **Bueno** | **6** | C2: falta interpretar la dinámica de volatilidad **en el contexto del consumo eléctrico**, que la instrucción pide expresamente; C3: Ljung-Box sobre z |
| 3 | Contraste (ID 3.1) | **Bueno** | **6** | C4: falta explicar «qué limitaciones conserva cada uno» (el sesgo de 12/12 desapareció del texto de la §3) y reconocer que en MAE el naive le gana al SARIMA; F2: dos tablas en la sección |
| 4 | Selección (ID 3.2) | **Bueno** | **6-9** | C5: el pronóstico 2023 no se interpreta «en el contexto del caso»; C1 («p ≥ 0,10») |
| 5 | Ortografía y redacción | Bueno | 6 | R1 a R6 |
| 6 | Formato y entrega | **Insuficiente** | **3** | F1: **dos Hojas de decisiones** (la [BORRADOR] completa y la [AUTOR] vacía); F2; B3 (citas) |
| | **Total estimado** | | **~36-39 / 54** | **~54** si se resuelven las brechas |

Aparte de la rúbrica sigue pendiente **A2, la declaración de IA**: es copia de la S2, no nombra la herramienta y no menciona que los textos partieron de borradores del asistente.

## Estado de las brechas de la primera revisión

| # | Brecha | Estado |
|---|---|---|
| A1 | Celdas [AUTOR] | ⚠️ **Parcial.** Punto de partida, las 4 interpretaciones y las conclusiones están reescritas y sin marcas. **Falta la Hoja** (F1) |
| A2 | Declaración de IA | ❌ Pendiente (sección D) |
| M1 | Ljung-Box con `model_df=2` | ❌ Pendiente, ahora **C1** |
| M2 | Ljung-Box sobre z en nivel | ❌ Pendiente, ahora **C3** |
| M3 | Retransformación exp(μ) frente a la de la S2 | ❌ Pendiente, se integra en **C4** |
| B1 | Raíz MA 1,002 frente a −0,981 | ✅ Resuelta: el texto solo cita −0,981 |
| B2 | ADF y memoria larga | Opcional, sin cambios |
| B3 | Citas APA | ❌ Pendiente: «Notebook S3, §…» aparece 4 veces (celdas 15 y 18) sin entrada que coincida; Seabold y Perktold (2010), Sheppard (s. f.) y Hyndman et al. (2026) no se citan |

## Brechas de contenido (criterios 1 a 4)

**C1. Ljung-Box de los residuos (criterios 1 y 4).** La celda 11 no descuenta los 2 parámetros MA, como sí hizo la S2. Con `acorr_ljungbox(residuos, lags=[12, 24, 36], model_df=2)` los valores p pasan de 0,526 / 0,102 / 0,115 a **0,355 / 0,061 / 0,076**. Hay que actualizarlos en:
- la Hoja, fila 1;
- la celda 12;
- la celda 21 y la conclusión 1, donde dice «Ljung-Box p ≥ 0,10». Con el descuento esto ya no es cierto: usar «p ≥ 0,06; no rechaza en ningún rezago».

**C2. Volatilidad en el contexto del consumo eléctrico (criterio 2).** La instrucción pide «interprete la dinámica de volatilidad en el contexto del consumo eléctrico». La celda 15 interpreta las pruebas, pero no relaciona el resultado con el fenómeno. Preguntas para responder con tus palabras:
- ¿Por qué el consumo mensual de un segmento comercial, a diferencia de un precio financiero, no tendría rachas de volatilidad?
- ¿Qué papel cumple el indicador covid, que absorbe el shock de 2020-2021 como cambio de nivel y no como volatilidad?
- ¿Qué significan α ≈ 0,07 y un factor de escala que vuelve a 1,00 en 2 o 3 meses?

**C3. Ljung-Box sobre z en nivel (criterio 2).** La rúbrica pide revisar los residuos estandarizados «y sus cuadrados». Agregar en la celda 14 `acorr_ljungbox(z, lags=[12, 24])`, que da p = 0,562 y 0,121, y citarlo en la celda 15 y en la Hoja.

**C4. Contraste: aspectos, diferencias sustantivas y limitaciones (criterio 3).** La instrucción pide explicar «qué modelo mejora cada aspecto, qué diferencias son sustantivas y qué limitaciones conserva cada uno». A la celda 18 le falta:
- **Limitaciones de cada modelo**, sobre todo el sesgo del SARIMA: 12/12 errores positivos, +6,68 GWh. Ya se imprime en la celda 17, pero el autor lo sacó de la §3. También la del naive (sin intervalos) y la del ARFIMA (la corrección va en sentido contrario al error).
- **El naive tiene menor MAE** que el SARIMA (6,53 frente a 6,68) con exp(μ). Hay que reconocerlo o aplicar la corrección de sesgo de la S2 (M3: SARIMA 6,85 / 6,40 frente a 7,26 / 6,53 del naive). La frase en primera persona «usé corrección… aquí uso exp(μ)» se puede reformular o, con M3, eliminar.

**C5. Interpretar el pronóstico 2023 en el contexto del caso (criterio 4).** La celda 21 presenta la Tabla 3 y la Figura 6, pero no las interpreta para DEL. Pregunta guía: ¿qué significa para la compra de energía que el modelo subestime todos los meses en unos 6,7 GWh (~6 % del consumo mensual) y que, aun así, los 12 meses queden dentro del intervalo?

## Brechas de formato (criterio 6)

**F1. Dos Hojas de decisiones.** La celda 1 sigue siendo la Hoja **[BORRADOR]** completa del asistente y la celda 2 es la Hoja **[AUTOR]** vacía. Hay que completar la celda 2 con tus palabras y las cifras corregidas (C1, C3 y, si aplica, M3), borrar la celda 1 y quitar las marcas «[AUTOR]» y «_(completar…)_». La Hoja debe ser la primera sección.

**F2. Una tabla por sección.** La §3 tiene dos tablas (Tabla 1, puntual, y Tabla 2, intervalos). La instrucción pide «una tabla que compare» ambos aspectos. Se pueden unir en una sola: filas SARIMA, SARIMA + ARFIMA, SARIMA + GARCH y naive; columnas RMSE, MAE, cobertura y ancho, con «—» donde no aplique. Al hacerlo, renumerar la Tabla 3 de la §4 como Tabla 2.

| Requisito de formato | Estado |
|---|---|
| Ejecutable desde un kernel reiniciado | ✅ 9/9 |
| Estructura: Hoja → punto de partida → 4 secciones → conclusiones → referencias → declaración | ⚠️ Orden correcto, pero con dos Hojas (F1) |
| Hasta 3 figuras por sección | ✅ §1: 2 · §2: 2 · §3: 1 · §4: 1 |
| Una tabla por sección | ⚠️ §3 tiene 2 (F2) |
| Hasta 250 palabras de interpretación | ✅ §1 185 · §2 153 · §3 166 · §4 155 (hay margen para C2, C4 y C5) |
| Nombre `mcdi505_s3inicialapellido` | ✅ |
| Referencias APA citadas | ⚠️ B3 |

## Redacción (criterio 5)

| # | Celda | Texto actual | Corrección |
|---|---|---|---|
| R1 | 12 | «Luego se calculo el exponente de Hurst fue H = 0,652» | «Luego se calculó el exponente de Hurst, que fue H = 0,652» (tilde y frase rota) |
| R2 | 18 | «porque usé corrección de sesgo… aquí uso exp(μ)» | Unificar en impersonal («se usó…, aquí se usa…») o eliminar con M3 |
| R3 | 21 | «**Modelo seleccionado,** se mantiene el SARIMA…» | «Como modelo seleccionado se mantiene el SARIMA…» |
| R4 | 15 | «(Ljung-Box p = 0,654; ARCH-LM p = 0,832) (Notebook S3, §3.5; Figura 4)» | Unir en un solo paréntesis |
| R5 | 18 | «Conclusión:» sin negrita | «**Conclusión:**», como en las demás secciones |
| R6 | 24 | «autocontenido.  Además» y «resultados.  Por último» | Quitar dobles espacios |
| — | 9, 21 | «-300,9», «-6,0 %», «-0,981» con guion | Opcional: signo menos «−», como en las celdas 12 y 22 |

## D. Declaración de uso de IA (A2)

Las instrucciones permiten la IA «únicamente para organizar ideas o mejorar la redacción, siempre que se declare su uso en la entrega». La celda 24 es copia de la S2 y tiene tres problemas:
- No nombra la herramienta (Claude, en Claude Code).
- No dice que el asistente preparó el código de los bloques 1 a 4 y **borradores de todos los textos**, que luego reescribiste.
- La Hoja actual (celda 1) sigue siendo el borrador del asistente.

Reescribir la Hoja (F1) antes de cerrar la declaración, y que la declaración describa con exactitud lo que se hizo.

## Orden sugerido

1. Código: C1 (`model_df=2`), C3 (Ljung-Box sobre z) y decidir M3; luego F2 (una tabla en la §3). Ejecutar todo.
2. Textos: C2, C4 y C5 con las cifras nuevas; R1 a R6; B3.
3. Hoja [AUTOR] completa y borrar la [BORRADOR] (F1).
4. Declaración de IA (D).
5. Reiniciar el kernel, ejecutar todo y revisar el conteo de palabras (≤ 250 por sección).

---

# Primera revisión (14 de octubre)

## Resumen

| Prioridad | # | Brecha | Celdas | Estado |
|---|---|---|---|---|
| Alta | A1 | Faltan las 8 celdas [AUTOR], y las [BORRADOR] siguen en el archivo | 0, 1-2, 9-10, 13-14, 17-18, 21-22, 25-28, 30-31 | ❌ Pendiente |
| Alta | A2 | Uso de IA: los borradores se hicieron con los datos y residuos de DEL, algo que la guía pide no hacer | 30-31 | ❌ Pendiente: declararlo con exactitud |
| Media | M1 | Ljung-Box sin descontar parámetros, distinto de la S2 | 12, 1, 13, 25, 27 | ⚠️ Corregir cifras |
| Media | M2 | Ljung-Box sobre los residuos estandarizados (z) en nivel, no solo sobre z² | 16, 1, 17 | ⚠️ Agregar |
| Media | M3 | Retransformación con exp(μ), distinta de la decisión de la S2 | 20, 1, 21, 24-25, 27 | ⚠️ Decidir y ajustar |
| Baja | B1 | La raíz MA (1,002) y el coeficiente (−0,981) aparecen sin relacionarlos | 8, 9 | Opcional |
| Baja | B2 | La relación ADF / memoria larga (§2.5) no se menciona | 13 | Opcional |
| Baja | B3 | Citas APA: «Notebook S3» no coincide con la entrada de referencias; hay dos referencias sin cita en el texto | 13, 17, 21, 25, 29 | ⚠️ Corregir |

**Lo que ya está correcto (no tocar):** el punto de partida coincide con la S2 y la tabla de errores frecuentes de la guía se cumple en todas sus filas (ver la sección final).

---

## A1. Celdas [AUTOR] pendientes y limpieza de borradores

Las 8 celdas [AUTOR] solo tienen el texto «_Pendiente: reescribir…_» o una tabla vacía:

| Celda [AUTOR] | Contenido esperado | Límite |
|---|---|---|
| 2 | Hoja de decisiones (4 filas × 5 columnas) | Celdas breves: una cifra o prueba por columna |
| 10 | Punto de partida | — |
| 14 | Interpretación de la memoria larga | máx. 250 palabras |
| 18 | Interpretación de la volatilidad | máx. 250 palabras |
| 22 | Interpretación del contraste | máx. 250 palabras |
| 26 | Interpretación de la selección (modelo para la Semana 4) | máx. 250 palabras |
| 28 | Conclusiones | — |
| 31 | Declaración de uso de IA | ver A2 |

Antes de entregar:

1. Eliminar todas las celdas **[BORRADOR]** (1, 9, 13, 17, 21, 25, 27 y 30).
2. Quitar el recuadro «📝 Las celdas marcadas [BORRADOR]…» de la celda 0.
3. Quitar las etiquetas «[AUTOR]» y los textos «_(completar…)_», dejando los títulos como los de la plantilla («Interpretación (máx. 250 palabras)», «Conclusiones», etc.).
4. Contar las palabras de cada interpretación. Los borradores tienen entre 243 y 247 palabras, muy cerca del límite; si se agrega texto (M1-M3, B1-B2), hay que recortar en otra parte.
5. **Hoy (miércoles):** la Formativa 3 es solo la Hoja de decisiones. Es lo primero que debe quedar en la celda 2 con redacción propia y con las cifras ya corregidas por M1-M3.

## A2. Uso de IA según la guía de compañía

La guía (págs. 3-4) permite usar IA «para ordenar ideas o mejorar la redacción, no para obtener respuestas completas», y su regla 1 dice: «No suba los datos de DEL, sus residuos ni su hoja de decisiones para que la IA los complete». Los borradores y el código de los bloques 1 a 4 se prepararon con Claude Code trabajando directamente sobre el notebook con la serie de DEL.

Qué corregir:

- **La celda 31 debe describir lo que se hizo:** herramienta (Claude, en Claude Code), con qué material trabajó (el notebook y la serie de DEL), qué produjo (código de los bloques 1 a 4 y borradores de texto, que se eliminaron) y qué se redactó y verificó por cuenta propia.
- La celda 30 dice «Contrasté las afirmaciones técnicas con el notebook de la Sesión 3 (§2.2, §2.5, §3.3–§3.5, §4.5, §5 y §7) y con la guía de compañía». Incluirlo en la declaración final solo si de verdad se hizo esa lectura.
- Si hay dudas sobre si este uso cabe en la política del curso, conviene consultarlo con el profesor antes de la Sumativa del domingo.

## M1. Ljung-Box con los parámetros MA descontados (consistencia con la S2)

En la S2 (Tabla 4), Ljung-Box se calculó con 2 parámetros AR/MA descontados (`model_df=2`): p = 0,355 en el rezago 12 y 0,061 en el 24. La S3 lo calcula sin descontarlos y obtiene otros valores para los mismos residuos.

**Código (celda 12):**

```python
print(acorr_ljungbox(residuos, lags=[12, 24, 36], model_df=2).round(3))
```

**Cifras que cambian:**

| Rezago | Actual (sin descuento) | Con `model_df=2` (igual que la S2) |
|---|---|---|
| 12 | 0,526 | **0,355** |
| 24 | 0,102 | **0,061** |
| 36 | 0,115 | **0,076** |

**Textos por ajustar:**

- Hoja, fila 1 y celda 13: «p = 0,526 / 0,102 / 0,115» → «p = 0,355 / 0,061 / 0,076».
- Celdas 25 (punto 1) y 27 (punto 1): «Ljung-Box p ≥ 0,10 hasta el rezago 36» **deja de ser cierto**. Usar, por ejemplo: «Ljung-Box no rechaza en ningún rezago (p ≥ 0,06 hasta el 36), igual que en la Semana 2».
- La conclusión no cambia: ningún valor p queda bajo 0,05. Sí conviene decir que el rezago 24 está cerca del umbral, como en la S2, y relacionarlo con la ACF (−0,22 en el rezago 24, apenas fuera de la banda de ±0,215). Una sola autocorrelación aislada no equivale al decaimiento lento propio de la memoria larga.

## M2. Diagnóstico de los residuos estandarizados «y sus cuadrados»

La guía pide diagnosticar el GARCH «sobre los residuos estandarizados por σ̂ₜ **y sus cuadrados**» (Notebook §3.5). La celda 16 solo prueba z² con Ljung-Box y z con ARCH-LM (que también mira los cuadrados). Falta el nivel.

**Código (celda 16), después de `lb_z`:**

```python
lb_z_nivel = acorr_ljungbox(z, lags=[12, 24])
print(f"Residuos estandarizados: Ljung–Box z (12 / 24) p = "
      f"{lb_z_nivel.lb_pvalue.iloc[0]:.3f} / {lb_z_nivel.lb_pvalue.iloc[1]:.3f}")
```

**Resultado verificado:** p = 0,562 (rezago 12) y 0,121 (rezago 24). No queda estructura. Agregar la cifra a la hoja (fila 2) y a la interpretación de la volatilidad.

## M3. Retransformación a GWh: exp(μ) o exp(μ + σ²/2)

En la S2 se decidió explícitamente retransformar con corrección de sesgo, exp(μ + σ²ₕ/2), porque exp(μ) entrega la mediana y no la media (commit `f4dbdcc`; Hyndman y Athanasopoulos, 2021, §5.6). La S3 vuelve a exp(μ), como sugiere la plantilla, y lo justifica en la celda 21. El problema es que con exp(μ) **el MAE del SARIMA (6,68) queda peor que el del naive (6,53)**, y ningún texto lo dice. La frase «el naive estacional queda muy cerca» no basta.

| Métrica (validación 2023, GWh) | exp(μ), actual | exp(μ + σ²/2), como en la S2 |
|---|---|---|
| RMSE / MAE SARIMA | 7,13 / 6,68 | **6,85 / 6,40** |
| RMSE / MAE SARIMA + ARFIMA | 7,34 / 6,93 | **7,06 / 6,64** |
| ΔRMSE ARFIMA | +0,21 | +0,21 |
| RMSE / MAE naive estacional | 7,26 / 6,53 | 7,26 / 6,53 |
| Sesgo medio SARIMA (meses con error positivo) | +6,68 (12/12) | **+6,40 (12/12)** |
| Cobertura y ancho de los intervalos | sin cambio | sin cambio (los intervalos no se corrigen) |

**Recomendación: opción B (corrección de sesgo).** Mantiene la decisión de la S2, el SARIMA vuelve a superar al naive en ambas métricas, como en la S2, y las conclusiones no cambian.

- **Opción B (recomendada):** en la celda 12, `pron_sarima = np.exp(media_log + sd_log**2 / 2)` y `pron_arfima = np.exp(media_log_arfima + sd_log**2 / 2)`. En la celda 20, eliminar la línea de «Referencia Sumativa 2», que pasa a ser la cifra principal. Actualizar las cifras de las celdas 1, 13 («−0,24 GWh» se recalcula), 21, 25 y 27 según la tabla.
- **Opción A (mantener exp(μ)):** agregar en la celda 21 una frase que reconozca que en MAE el naive queda por debajo del SARIMA (6,53 frente a 6,68 GWh).

## B1. Raíz MA frente al coeficiente (opcional)

La celda 8 imprime «mín. |raíz MA| = 1,002» y los textos hablan del coeficiente ma.S.L12 = −0,981. Las dos cifras son correctas y dicen lo mismo: la raíz queda casi sobre el círculo unitario. Basta con citar una de ellas o agregar «(raíz de módulo 1,002)» en el punto de partida.

## B2. ADF y memoria larga (opcional, refuerza la fila «ADF» de la tabla de la guía)

El notebook no comete el error, pero tampoco lo menciona. Una frase en la interpretación de la memoria larga cubriría esa fila de la tabla: «Las pruebas ADF y KPSS de la Semana 2 justificaron d = 1, pero ADF no distingue una memoria larga con 0 < d < 0,5 (Notebook S3, §2.5). Por eso la memoria larga se prueba sobre los residuos». Tener en cuenta el límite de 250 palabras.

## B3. Citas y referencias APA

| Problema | Corrección |
|---|---|
| El texto cita «(Notebook S3, §…)» siete veces, pero la entrada de referencias es «Universidad Andrés Bello. (s. f.)…» | Usar en el texto la misma autoría de la entrada, «(Universidad Andrés Bello, s. f., §2.2)», o cambiar la entrada para que empiece por la forma citada |
| La guía de compañía tiene autor y fecha (Harvey Rosas, 12 de octubre de 2026) | Si se cita, agregar una entrada propia: Rosas, H. (2026). *MCDI505: Guía de compañía, Semana 3* [Material de curso]. UNAB Online. |
| Seabold y Perktold (2010), Sheppard (s. f.) y Hyndman et al. (2026) no se citan en ningún texto | Citarlos donde corresponda (statsmodels en el punto de partida; fpppy junto a fpp3) o eliminarlos. La librería `arch` no se usó, así que Sheppard sobra salvo que se cite como lectura del bloque 2 |

---

## Validación de lo que ya está correcto

### Punto de partida frente a la S2

| Elemento | S2 | S3 | Estado |
|---|---|---|---|
| Modelo | B, SARIMA(0,1,1)(0,1,1)₁₂ + covid, en log | igual (celda 7) | ✅ |
| AIC | −300,903 | −300,9 | ✅ |
| Efecto covid | −6,0 % (−0,062; p < 0,001) | −6,0 % (−0,0617) | ✅ |
| ma.L1 / ma.S.L12 | −0,205 / −0,981 | −0,205 / −0,981 | ✅ |
| Residuos utilizables | 83 | 83 | ✅ |
| ARCH-LM (12) | p = 0,639 | p = 0,639 | ✅ |
| RMSE / MAE 2023 con corrección de sesgo | 6,854 / 6,398 | 6,85 / 6,40 | ✅ |
| Ljung-Box (12 / 24) | 0,355 / 0,061 | 0,526 / 0,102 | ❌ ver M1 |

### Tabla de la guía «Errores frecuentes de la IA en esta unidad»

| Lo correcto (según la guía) | Cómo lo resuelve el notebook | Estado |
|---|---|---|
| Con muestras cortas el R/S sobrestima H: contrastarlo con la ACF y con el efecto en el pronóstico | ACF de los residuos (Fig. 1), simulación de 500 ruidos blancos con n = 83 (Fig. 2: media de 0,612; el 37 % supera 0,652) y efecto sobre el pronóstico (−0,24 GWh; ΔRMSE +0,21) | ✅ |
| Se diagnostica sobre los residuos del SARIMA | Hurst y GARCH sobre `sarima.resid` desde la observación 14 (`d + D·s = 13` descartadas) | ✅ |
| ADF no distingue memoria larga con 0 < d < 0,5 | No se hace la afirmación errónea; la memoria larga se prueba sobre los residuos | ✅ (B2 opcional) |
| La restricción α + β < 1 debe imponerse | Restricción `0,999 − α − β ≥ 0` en SLSQP; persistencia de 0,509 y convergencia = True | ✅ |
| Diagnóstico sobre los residuos estandarizados por σ̂ₜ y sus cuadrados | z² (Ljung-Box p = 0,654) y ARCH-LM sobre z (p = 0,832) | ✅ con M2 |
| ARFIMA y GARCH no se comparan por AIC sino por su efecto en el pronóstico de validación | ARFIMA en el pronóstico puntual (Tabla 1), GARCH en los intervalos (Tabla 2); la celda 21 lo explica | ✅ |
| Sin evidencia previa, el modelo avanzado no se justifica; una conclusión negativa es válida | Se mantiene B con cifras de los tres bloques | ✅ |
| La validación es 2023; 2024 se abre solo en la Semana 4 | Entrenamiento 2015-2022 y validación 2023; 2024 está en el CSV pero no se usa | ✅ |

### Cifras de los borradores verificadas con la ejecución

| Cifra citada | Salida | Estado |
|---|---|---|
| Banda ±0,215; solo el rezago 24 (−0,22) fuera | ±0,215; [24]; ACF₂₄ = −0,219 | ✅ |
| H = 0,652; d = 0,152 | 0,652; 0,152 | ✅ |
| Ruido blanco: media 0,612, IC 95 % [0,392; 0,823], 37 % ≥ H | iguales | ✅ |
| Ljung-Box residuos² p = 0,485; ARCH-LM p = 0,639 | iguales | ✅ |
| ACF de residuos²: solo el rezago 18 (0,31) sobresale | 0,312 en el rezago 18 | ✅ |
| ω = 0,457; α = 0,066; β = 0,442; α + β = 0,509 | iguales | ✅ |
| Factor de escala 0,96 → 1,00 en 2-3 meses | 0,964; 0,982; 0,991… | ✅ |
| Cobertura 12/12; ancho de 29,4 y 29,3 GWh | 29,445 y 29,328 | ✅ |

## Orden sugerido de trabajo

1. Decidir M3 (opción A o B) y aplicar M1 y M2 en el código; volver a ejecutar todo.
2. Escribir la Hoja de decisiones [AUTOR] con las cifras nuevas (**Formativa 3, hoy**).
3. Redactar las interpretaciones, las conclusiones y el punto de partida, y revisar el límite de 250 palabras.
4. Corregir las citas (B3) y la declaración de IA (A2).
5. Eliminar los [BORRADOR], reiniciar el kernel, ejecutar todo y revisar el archivo contra el PDF de instrucciones.
