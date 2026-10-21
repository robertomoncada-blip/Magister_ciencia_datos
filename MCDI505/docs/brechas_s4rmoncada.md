# Brechas: Formativa 4 / Sumativa 4 (`mcdi505_s4rmoncada.ipynb` y borrador del informe)

- **Fecha de revisión:** 20 de octubre de 2026
- **Documentos de referencia:** `MCDI505_Formativa4_instrucciones_v2.pdf` (3 criterios de contenido, 9 puntos cada uno; formativa, 0 %), `MCDI505_S4_guia_de_compania.pdf` y `MCDI505_Sumativa4_instrucciones_v2.pdf` (5 criterios, para la etapa siguiente)
- **Ejecución de control:** con kernel nuevo, sobre una copia: **9/9 celdas de código, en orden y sin errores**; 1 figura (Figura 1)
- **Plazo de la Formativa 4:** **viernes 23 de octubre**, 23:59. La guía movió la fecha desde el miércoles: «si algún otro documento indica el miércoles, rige esta fecha»

## Octava revisión (21 de octubre): validación final de ortografía y de correlación texto–resultados

**Ejecución de control:** con kernel nuevo, sobre una copia: 9/9 celdas en orden, sin errores; 1 figura; **Tablas 1 a 4 con título** (numeración continua).

**Ortografía y formato:** ✅ se aplicaron todas las correcciones de la séptima revisión: Tabla 1, paréntesis en la §2, «el modelo» en la §3, «se eligió» en la §4 y «se comprobó» en la declaración. Búsqueda automática sin hallazgos (dobles espacios, «..», espacio antes de coma o punto).

**Correlación texto–resultados:** se cruzaron todas las cifras del texto con las salidas del notebook.

| Origen de la cifra | Cifras | Estado |
|---|---|---|
| Salidas de la S4 | MASE 0,98 / 0,61 / 1,02; RMSE 6,85 / 4,87; 113,66 y 120,05 GWh; sesgo +2,89 (2,4 %; 9/12); IC 12/12 y 29,7 GWh; Tabla 2 (38,5 y 29,7); Tabla 3 (41,3; 130,6; 13,8; 79,8); Tabla 4 (1.440,7; 1.499,3; +4,1 %; 148,8; 145,6; 142,3; 141,1); MA estacional −0,970 | ✅ Coinciden |
| Derivadas de las tablas | ≈ 40 % menos error; 5,6 % de crecimiento; diferencias ≤ 0,03 GWh; MASE 0,61 a 0,62; ≈ 30 % más ancho; −39 % de costo; 3,3 % del consumo | ✅ Correctas |
| Semanas 2 y 3, con fuente citada | ADF −8,82 / −2,90; KPSS 0,040 / 0,463 (S2); H = 0,652 y ARCH-LM p = 0,639 (S3); Jarque-Bera p = 0,001 (Semana 2) | ✅ Citadas |
| Semana 3, **sin fuente** | Sesgo de 2023 = +6,40 GWh (§1) | ⚠️ Agregar «(Semana 3)» |

**Pendientes (con [BORRADOR]):** la fuente del +6,40 en la §1 y el espacio en «entrega. |» de la declaración. Ninguno afecta la rúbrica.

**Rúbrica de la Formativa 4:** se mantiene **27 / 27** (los tres criterios en Excelente; ver la séptima revisión).

---

## Séptima revisión (21 de octubre): rúbrica de la Formativa 4 + ortografía y formato

**Ejecución de control:** con kernel nuevo, sobre una copia: 9/9 celdas en orden, sin errores; 1 figura. Todas las cifras del texto se respaldan en las salidas (incluido 113,66 GWh).

### A. Rúbrica de la Formativa 4 (3 criterios de contenido)

| # | Criterio | Instrucción específica | Cumplimiento en el borrador (§4) y en el anexo | Nivel probable |
|---|---|---|---|---|
| 1 | Informe ejecutivo: problema, metodología y solución (ID 4.1) | Párrafo de apertura de 5 a 8 líneas, sin jerga: decisión de la Gerencia, costo de equivocarse en cada dirección, solución propuesta y figura clave | ✅ Decisión: cuánta energía contratar para el año siguiente · ✅ costo en ambas direcciones: spot de 2 a 4 veces más caro / energía pagada sin usar · ✅ datos (10 años, 2015-2024) y metodología (estacionalidad anual, efecto de la pandemia, prueba en 2024) · ✅ solución: ≈ 4 % sobre el pronóstico · ✅ Figura 1 (serie, pronóstico 2024 e IC 95 %) · ✅ ≈ 8 líneas | **Excelente** (9) |
| 2 | Sustento técnico de los modelos (ID 3.2) | Tabla con el modelo final, las alternativas descartadas en S2 y S3 y el naive, con métricas de validación 2023 y prueba 2024, más una frase de por qué el final | ✅ Tabla 2: B, A (S2), B + ARFIMA y B + GARCH (S3) y naive, con RMSE, MAE, MASE, cobertura y ancho en 2023 y 2024 · ✅ frase con cifra (RMSE 6,85; empate en 2024; único que superó al naive y pasó Ljung-Box en la S2) · ✅ cadena de evidencia con cifras de dependencia temporal, volatilidad y pronóstico | **Excelente** (9) |
| 3 | Conclusiones y recomendaciones (ID 4.1) | Recomendación principal en 1-2 frases con su cifra y la limitación más importante | ✅ Contratar el cuantil 75 % = 1.499,3 GWh para 2025 (+4,1 %); −39 % de costo en la prueba 2024 · ✅ limitación: supuesto de costo 3 a 1 y prueba de solo 12 meses · ✅ cinco limitaciones más en la §3 | **Excelente** (9) |
| | **Total estimado** | | | **27 / 27** |

**Errores frecuentes de la guía:** ninguno. Se recomienda un cuantil superior y no la media; la corrección de sesgo se aplica solo a la media; 2024 se usa una sola vez para evaluar; MASE < 1 está bien interpretado; no se comparan AIC; el intervalo no se presenta como garantía; las cifras son rastreables.

### B. Ortografía y formato (no se evalúan en la Formativa; sí en la Sumativa 4)

**Corregido por el autor desde la sexta revisión:** gerundios, sujeto ambiguo y «12 de 12» (§1); título impersonal y «Cadena de evidencia» en negrita (§2); paréntesis de la Tabla 4, etiquetas en negrita y «parámetro MA estacional» (§3); línea en blanco, «que… que» y «Además… además» (§4); voz impersonal y artículo en la declaración.

**Pendientes (con [BORRADOR] «Dice / Debe decir» en el notebook):**

| Sección | Brecha | Tipo |
|---|---|---|
| §1 (código) | **Falta la «Tabla 1»**: la tabla resumen de la §1 no tiene título y la numeración salta a la Tabla 2 | Formato |
| §2 | «(ARCH-LM p = 0,639) (S3)»: dos paréntesis seguidos | Formato |
| §3 | «**Variables omitidas:** El modelo» → «el modelo» | Ortografía |
| §4 | Opcional: «Frase de por qué **elegí**» → «se eligió» | Voz |
| Declaración | «Por último, **comprobé**» → «se comprobó»; «entrega.\|» → «entrega. \|» | Voz y formato |

### C. Antes de entregar

1. Aplicar los 5 pendientes de B y borrar los [BORRADOR].
2. Reiniciar el kernel, ejecutar todo y guardar (el anexo debe ir ejecutado).
3. Llevar al **PDF de una página** (`mcdi505_s4rmoncada`, la tabla y la figura pueden ir en una segunda página) los tres bloques de la §4, la Figura 1 y la Tabla 2 reformateada como tabla del documento, con las mismas cifras.
4. **Plazo:** el PDF de instrucciones dice miércoles 21 de octubre (hoy); la guía de compañía dice viernes 23 y que, ante la diferencia, rige su fecha.

---

## Sexta revisión (21 de octubre): ortografía, redacción y formato

La Formativa 4 no evalúa ortografía ni formato, pero la **Sumativa 4 sí** (criterios 4 y 5), y este texto será la base del informe. Hay 5 celdas [BORRADOR] «Dice / Debe decir» en el notebook.

| Sección | Hallazgos |
|---|---|
| §1 | Gerundios de posterioridad («logrando», «mostrando»); sujeto ambiguo en «…aumentó… y tendió a subestimar» (¿el consumo o el naive?); «los 12 de 12 meses» redundante. **Formato: falta la «Tabla 1»**: la tabla resumen no tiene título, y el texto salta de la Figura 1 a la Tabla 2 |
| §2 | Título en primera persona («¿Por qué elegí…?») con el cuerpo impersonal; subtítulo «Cadena de evidencia» sin negrita; dos paréntesis seguidos «(… 0,639) (S3)» |
| §3 | Dos paréntesis seguidos «(+4,1 %) (Tabla 4)»; etiquetas de las viñetas sin negrita; «El modelo» con mayúscula después de dos puntos; «parámetro estacional MA» → «parámetro MA estacional» |
| §4 | Falta la línea en blanco después del título del bloque 1; «que… que» repetido; «Además… además» en la misma oración |
| Declaración | Mezcla de voces («se ejecutó… revisé… verifiqué… se generó»); falta el artículo en «las interpretaciones finales y conclusiones»; espacio antes de «\|» |

**Sin hallazgos:** encabezado, títulos de sección (§0 a §4), Figura 1 y Tablas 2 a 4 con título, cifras con coma decimal y espacio antes de «%», signo menos «−» en los negativos.

---

## Quinta revisión (21 de octubre): validación final con la rúbrica de la Formativa 4

**Ejecución de control:** con kernel nuevo, sobre una copia: 9/9 celdas en orden, sin errores; 1 figura. No quedan celdas [BORRADOR].

**Resueltas desde la cuarta revisión:**
- ✅ §1: el `print` ahora muestra el consumo medio de 2023 (**113,66 GWh**). Todas las cifras del texto tienen respaldo en las salidas.
- ✅ §3: las 5 limitaciones con viñetas y «**La prueba retrospectiva de 2024** (Tabla 3) mostró…» en una sola frase.
- ✅ §4: bloque 1 acortado (~128 palabras de párrafo, ≈ 8 líneas en una página).

| # | Criterio (Formativa 4) | Nivel probable | Puntaje |
|---|---|---|---|
| 1 | Problema, metodología y solución | Excelente | 9 |
| 2 | Sustento técnico de los modelos | Excelente | 9 |
| 3 | Conclusiones y recomendaciones | Excelente | 9 |
| | **Total estimado** | | **27 / 27** |

**Detalles menores (opcionales; la Formativa no evalúa ortografía ni formato):**
- §3: «Variables omitidas: **El** modelo» → «el modelo» (minúscula tras dos puntos).
- §4: «con un modelo que reconoce…, **que** en 2024 se equivocó» repite «que»; podría ser «…y el efecto de la pandemia. En 2024 se equivocó…».
- Declaración: opcional, mencionar las Tablas 2 a 4 y la validación de textos.

**Antes de entregar:** el PDF de una página `mcdi505_s4rmoncada`, con las mismas cifras que el notebook, y el notebook como anexo. Plazo: según la guía, viernes 23 de octubre (el PDF de instrucciones dice miércoles 21).

---

## Cuarta revisión (21 de octubre): rúbrica de la Formativa 4

**Ejecución de control:** con kernel nuevo, sobre una copia: 9/9 celdas en orden, sin errores; 1 figura.

### A. Cambios del autor desde la tercera revisión
- ✅ §1: se quitó el texto pegado del borrador anterior.
- ✅ §4, bloque 1: ahora menciona **los datos** (10 años, 2015-2024) **y la metodología** (estacionalidad anual, efecto de la pandemia y prueba en 2023 y 2024), como pide el criterio 1.
- ⚠️ §1: se agregó un `print`, pero del consumo medio de **2024** (120,05), que ya se imprimía. **113,66 (2023) sigue sin respaldo** en las salidas.
- ⚠️ §3: las limitaciones **siguen sin viñetas** (4 en un párrafo y «Variables omitidas» como título aparte), y un salto de línea separó «**La prueba retrospectiva de 2024**» de su frase «(Tabla 3) mostró…».

### B. Validación con la rúbrica de la Formativa 4 (3 criterios de contenido; no se evalúan ortografía ni formato)

| # | Criterio | Instrucción específica | Evidencia en el borrador (§4 del notebook) | Nivel probable |
|---|---|---|---|---|
| 1 | Problema, metodología y solución (ID 4.1) | Párrafo de 5 a 8 líneas sin jerga: decisión, costo de equivocarse en cada dirección, solución propuesta y figura clave | ✅ Decisión (cuánto contratar) · ✅ costo en ambas direcciones (spot de 2 a 4 veces; energía pagada sin usar) · ✅ **datos y metodología** · ✅ solución (≈ 4 % sobre el pronóstico) · ✅ Figura 1 · ⚠️ **largo**: ~145 palabras (≈ 9 a 11 líneas frente a 5 a 8) | **Excelente** (9) |
| 2 | Sustento técnico (ID 3.2) | Tabla con el modelo final, los descartados de S2 y S3 y el naive, con métricas 2023 y 2024, más una frase de por qué el final | ✅ Tabla 2 completa · ✅ frase con cifra (RMSE 6,85; empate en 2024; único que superó al naive y pasó Ljung-Box en la S2) · ✅ cadena de evidencia con cifras (ADF/KPSS, H = 0,652, ARCH-LM p = 0,639, MASE 0,61) | **Excelente** (9) |
| 3 | Conclusiones y recomendaciones (ID 4.1) | Recomendación en 1-2 frases con su cifra y la limitación más importante | ✅ Cuantil 75 % = 1.499,3 GWh (+4,1 %); −39 % de costo en 2024 · ✅ limitación (supuesto 3 a 1; 12 meses de prueba) | **Excelente** (9) |
| | **Total estimado** | | | **27 / 27** |

**Aspectos formales (no se califican en la Formativa, pero conviene cumplirlos):** PDF o DOCX de una página (tabla y figura pueden ir en una segunda), nombre `mcdi505_s4rmoncada`. **Plazo:** el PDF de instrucciones dice «miércoles de la Semana 4» (hoy, 21 de octubre); la guía de compañía lo movió al **viernes 23 de octubre** y dice que, ante la diferencia, rige su fecha. Si hay duda, conviene confirmarlo en el foro o entregar hoy.

### C. Pendientes (con [BORRADOR] «Dice / Debe decir» en el notebook)

| Sección | Brecha | Prioridad |
|---|---|---|
| §1 | 113,66 GWh sin respaldo: el `print` agregado es de 2024; cambiarlo a `y['2023']` | Media |
| §3 | Limitaciones en viñetas (5) y unir «**La prueba retrospectiva de 2024** (Tabla 3) mostró…» | Media (se ve en el PDF) |
| §4 | Acortar el bloque 1 a 5-8 líneas (propuesta: −16 palabras) | Media |
| Declaración | Opcional: mencionar las Tablas 2 a 4 y la validación de textos | Baja |

**El PDF no está en el repositorio:** revisar que tenga las mismas correcciones que el notebook.

---

## Tercera revisión (20 de octubre): texto contra resultados y rúbrica de la Formativa 4

**Ejecución de control:** con kernel nuevo, sobre una copia: 9/9 celdas en orden, sin errores; 1 figura (Figura 1).

### A. Concordancia texto–resultados

**Resueltas por el autor desde la segunda revisión:**
- §3: la cifra cruzada (cuantil 75 % frente a la media).
- §1: la conclusión matizada (MASE 0,98 en 2023 y 0,61 en 2024; sesgo 9/12; intervalo de 29,7 GWh) y la causa del sesgo dicha con prudencia.
- §2: la lógica del MASE y las cifras de la S3 (H = 0,652; ARCH-LM p = 0,639).
- §3: la fuente del Jarque-Bera.
- §4: la solución propuesta en el bloque 1, el RMSE 6,85 en el bloque 2 y la precisión sobre Ljung-Box.
- Declaración: se quitó la instrucción de la plantilla y «posteriormente».

**Pendientes (con [BORRADOR] «Dice / Debe decir»):**

| Sección | Brecha | Prioridad |
|---|---|---|
| §1 | **Quedó pegado el motivo del borrador anterior**: «…al entrenamiento.» \| Es una explicación plausible, pero no está probada: mejor decirlo con prudencia.» | Alta (se ve en el PDF) |
| §1 | «113,66 GWh» todavía no aparece en ninguna salida: agregar `print(f"Consumo medio mensual 2023 = {y['2023'].mean():.2f} GWh")` | Media |
| §3 | Las 5 limitaciones siguen sin viñetas y se ven como un solo párrafo | Media |
| §4 | Opcional: el bloque 1 no menciona **los datos ni la metodología** (criterio 1 de la rúbrica) | Media (para el Excelente) |
| Declaración | Opcional: mencionar que el asistente construyó las Tablas 2 a 4 y validó las cifras | Baja |

### B. Validación con la rúbrica de la Formativa 4

La Formativa evalúa **3 criterios de contenido** (no la ortografía ni el formato) sobre el **borrador en PDF o DOCX**. La validación se hace sobre la §4 del notebook, que el autor indica haber llevado al PDF (no está en el repositorio, así que no se pudo revisar).

| # | Criterio | Lo que pide la instrucción | Evidencia en el borrador (§4) | Nivel probable |
|---|---|---|---|---|
| 1 | Informe ejecutivo: problema, metodología y solución (ID 4.1) | Párrafo de 5 a 8 líneas sin jerga: decisión de la Gerencia, costo de equivocarse en cada dirección y solución propuesta, más la figura clave | ✅ Decisión (cuánto contratar) · ✅ costo en ambas direcciones (spot de 2 a 4 veces; energía pagada sin usar) · ✅ solución (≈ 4 % sobre el pronóstico) · ✅ Figura 1 · ⚠️ sin mención a los **datos ni a la metodología**, que la rúbrica nombra | **Bueno → Excelente** (6-9) |
| 2 | Sustento técnico (ID 3.2) | Tabla con el modelo final, los descartados de S2 y S3 y el naive, con métricas 2023 y 2024, más una frase de por qué el final | ✅ Tabla 2 completa (2023 y 2024: RMSE, MAE, MASE, cobertura y ancho) · ✅ frase con cifra (RMSE 6,85; empate en 2024; único que pasó Ljung-Box en la S2) · ✅ cadena de evidencia con cifras en la §2 | **Excelente** (9) |
| 3 | Conclusiones y recomendaciones (ID 4.1) | Recomendación principal en 1-2 frases con su cifra y la limitación más importante | ✅ Contratar el cuantil 75 % = 1.499,3 GWh (+4,1 %); −39 % de costo en 2024 · ✅ limitación: supuesto de costo 3 a 1 y prueba de 12 meses | **Excelente** (9) |
| | **Total estimado** | | | **24-27 / 27** |

**Verificaciones de la guía (errores frecuentes):** ✅ cuantil superior y no la media · ✅ corrección de sesgo solo en la media · ✅ 2024 usado una sola vez para evaluar · ✅ MASE < 1 bien interpretado · ✅ sin comparar AIC entre modelos distintos · ✅ el intervalo no se presenta como garantía · ✅ cifras rastreables al anexo (salvo 113,66).

### C. Antes de entregar (viernes 23 de octubre, 23:59)

1. Corregir el texto pegado en la §1 y agregar las viñetas en la §3. Opcional: datos y metodología en el bloque 1.
2. Revisar que el **PDF** tenga las mismas correcciones, sobre todo la cifra cruzada de la §3 ya corregida y el texto pegado de la §1.
3. Borrar los 4 [BORRADOR], reiniciar el kernel, ejecutar todo y adjuntar el notebook como anexo.
4. Nombre del documento: `mcdi505_s4rmoncada` (PDF o DOCX).

---

## Segunda revisión (20 de octubre): validación del texto del autor contra los resultados

**Ejecución de control:** 9/9 celdas sin errores. El autor redactó la §1, la §2, la §3, el borrador de la Formativa (§4) y la declaración, y eliminó 5 de los 6 [BORRADOR] anteriores (el que quedaba se reemplazó).

**Concordancia:** casi todas las cifras coinciden con las salidas: métricas 2023 y 2024, MASE, sesgo, cobertura, Tabla 2, prueba de costos y plan 2025. Brechas encontradas (con [BORRADOR] «Dice / Debe decir» bajo cada sección):

| Sección | Brecha | Tipo |
|---|---|---|
| §3 | «Mayor **consumo esperado**: diciembre (148,8) y enero (145,6)». Esas cifras son el **cuantil 75 %** (volumen a contratar); en la media, el mayor es enero (142,3) y luego diciembre (141,1) | **Cifra cruzada** |
| §1 | «113,66 GWh» no aparece en ninguna salida de la S4 | Sin respaldo en el anexo (agregar un `print`) |
| §1 | «pronósticos confiables… mejora claramente» exagera: en 2023 el MASE fue 0,98; sigue el sesgo (9/12) y el intervalo es ancho (29,7 GWh) | Afirmación más fuerte que la evidencia |
| §1 | «gracias a la incorporación de datos más recientes»: causa no probada | Redacción prudente |
| §2 | «fijarse más en el MASE»: el MASE también está empatado (0,61 a 0,62) | Lógica |
| §2 | La cadena de evidencia de la S3 no tiene cifras (H = 0,652; ARCH-LM p = 0,639) | Criterio 2 (cada afirmación con su cifra) |
| §3 | Las 5 limitaciones sin viñetas se ven como un solo párrafo; Jarque-Bera p = 0,001 sin fuente (S2) | Formato y fuente |
| §4 | El bloque 1 no dice qué **solución se propone** (la Formativa lo pide); el bloque 2 no tiene cifra | Instrucción específica |
| Declaración | Quedó «[AUTOR] (completar…)»; no menciona las Tablas 2 a 4 ni la validación; «posterior» → «posteriormente»; doble espacio | Exactitud y redacción |

**Pendiente fuera del notebook:** el documento de la Formativa 4 (PDF o DOCX de una página, `mcdi505_s4rmoncada`) para el viernes 23 de octubre.

---

## Resumen (primera revisión)

**Lo que se evalúa es el borrador del informe en PDF o DOCX, no el notebook.** El notebook es el anexo que respalda las cifras («no se califica por separado»). Hoy **la evidencia está completa, pero el borrador no existe**: las 5 celdas [AUTOR] están pendientes y no hay PDF ni DOCX.

| # | Criterio (Formativa 4) | Evidencia en el anexo | Texto del autor | Estado |
|---|---|---|---|---|
| 1 | Informe ejecutivo: problema, metodología y solución (ID 4.1) | ✅ Figura 1 (serie, pronóstico 2024 e IC 95 %) | ❌ Falta el párrafo de apertura (5 a 8 líneas, sin jerga) | **Pendiente** |
| 2 | Sustento técnico de los modelos (ID 3.2) | ✅ Tabla 2: modelo final, descartados de la S2 y la S3 y naive, en 2023 y 2024 | ❌ Falta la frase de por qué se eligió el modelo final | **Pendiente** |
| 3 | Conclusiones y recomendaciones (ID 4.1) | ✅ Tablas 3 y 4: cuantil 75 %, prueba de costos 2024 y plan 2025 | ❌ Faltan la recomendación con su cifra y la limitación principal | **Pendiente** |

Estimación: con el texto pendiente, cada criterio quedaría en **Insuficiente o Deficiente**. Con la evidencia que ya existe y un texto propio que la use, los tres pueden llegar a **Excelente**.

---

## 1. Cumplimiento de las instrucciones específicas

| Instrucción (Formativa 4) | Dónde está en el anexo | Estado |
|---|---|---|
| Reestimar el modelo de la S3 con 2015-2023 y pronosticar 2024 con IC 95 % | §1 (`evaluar("2023-12", …)`) | ✅ |
| Comparar con el naive estacional con RMSE, MAE y MASE | §1 (`resumen`) y Tabla 2 | ✅ RMSE 4,87, MAE 4,00 y MASE 0,61, frente a 8,19, 6,67 y 1,02 del naive |
| **Bloque 1:** párrafo de apertura con la decisión de la Gerencia, el costo de equivocarse en cada dirección y la solución | Ideas en el [BORRADOR] de la §4 | ❌ Texto del autor pendiente |
| **Bloque 1:** figura clave (serie observada, pronóstico 2024 e intervalo) | Figura 1 | ✅ |
| **Bloque 2:** tabla de modelos (final, descartados de S2 y S3 y naive) con métricas de 2023 y 2024 | Tabla 2 | ✅ Hay que reformatearla como tabla del documento |
| **Bloque 2:** una frase de por qué se eligió el modelo final | [AUTOR] de la §2 | ❌ Pendiente |
| **Bloque 3:** recomendación principal en 1-2 frases con la cifra que la respalda | Tablas 3 y 4 | ❌ Texto del autor pendiente |
| **Bloque 3:** la limitación más importante | Ideas en el [BORRADOR] de la §3 | ❌ Pendiente |
| Producto: PDF o DOCX de una página (tabla y figura pueden ir en una segunda) | — | ❌ No existe |
| Nombre `mcdi505_s4rmoncada` | Notebook ✅ | ❌ Falta el documento |
| Notebook ejecutado como anexo (guía) | 9/9 sin errores | ✅ |

## 2. Brechas del anexo (notebook)

| # | Brecha | Prioridad | Acción |
|---|---|---|---|
| N1 | Las 5 celdas **[AUTOR]** están vacías (§1, §2, §3, borrador de la Formativa y declaración) | Alta | Redactarlas con mis palabras: son la base del documento |
| N2 | Quedan 6 celdas **[BORRADOR]** | Alta | Borrarlas antes de entregar el anexo |
| N3 | **Declaración de IA vacía** | Alta | Completarla. Ver el [BORRADOR] con lo que hizo el asistente: completar la plantilla, la corrección de sesgo, las tablas 2 a 4 y las ideas |
| N4 | La plantilla se modificó: dataset `_s4`, `CORRECCION_SESGO = True` y las §2 y §3 nuevas | Media | Mencionarlo en una línea del informe o del anexo: la corrección de sesgo responde al **feedback del profesor** de la S3 (métricas comparables entre semanas). Con exp(μ), 2024 daría RMSE 4,96 y MAE 4,07; la conclusión no cambia |
| N5 | El supuesto de costo **c_u = 3·c_o** (cuantil 75 %) es una elección | Media | Decirlo explícitamente y mostrar la sensibilidad (2 a 4 veces → cuantil de 67 % a 80 %). El caso dice «entre 2 y 4 veces» |

## 3. Verificación con la tabla «Errores frecuentes de la IA» de la guía

| Lo correcto (guía) | Cómo está en el anexo | Estado |
|---|---|---|
| Con costo asimétrico se recomienda un **cuantil superior**, no la media | §3: cuantil 75 %; en 2024 el costo baja ≈ 39 % frente a contratar la media | ✅ |
| La corrección de sesgo va solo en la **media**; los cuantiles y los límites del IC van con exp() | `ajustar_y_pronosticar` y función `cuantil` | ✅ |
| **2024 se usa una sola vez** para evaluar; no se reestima antes | Se evalúa con 2015-2023; la reestimación con 2015-2024 se hace **después**, solo para el plan 2025 | ✅ (aclararlo en el informe) |
| MASE < 1 = supera al naive | 0,61 en 2024; 0,98 en 2023 | ✅ |
| No comparar el AIC de modelos distintos; comparar fuera de muestra | Tabla 2 con RMSE, MAE y MASE | ✅ |
| El IC 95 % no garantiza; 11 o 12 de 12 es compatible | 12/12 en 2023 y 2024 | ✅ (redactarlo así) |
| Sin jerga para la Gerencia | — | Pendiente (lo define el texto del autor) |
| Cada cifra sale del análisis | Todas las cifras de los borradores salen de las Tablas 1 a 4 | ✅ |

## 4. Evidencia disponible para el borrador (verificada en la ejecución)

| Tema | Cifra | Fuente |
|---|---|---|
| Prueba 2024: modelo final frente al naive | RMSE 4,87 / 8,19; MAE 4,00 / 6,67; MASE 0,61 / 1,02 | §1 |
| Validación 2023 | RMSE 6,85 / 7,26; MAE 6,40 / 6,53; MASE 0,98 / 1,00 | §1 |
| Intervalo 95 % | 12/12 en 2023 y 2024; ancho 29,7 GWh (≈ 25 % del nivel) | §1 |
| Sesgo | +6,40 GWh en 2023 (12/12) → +2,89 en 2024 (9/12; 2,4 %) | §1 |
| Alternativas en 2024 | A 4,88; ARFIMA 4,89; GARCH 4,87; empate (≤ 0,03 GWh). Intervalo de A: 38,5 GWh | Tabla 2 |
| Volumen (c_u = 3·c_o) | Cuantil 75 %; en 2024: faltante de 41,3 a 13,8 GWh y costo de 130,6 a 79,8 (−39 %) | Tabla 3 |
| Plan 2025 | Media 1.440,7 GWh; cuantil 75 % 1.499,3 GWh (+4,1 %); máximos en diciembre (148,8) y enero (145,6) | Tabla 4 |
| Limitaciones candidatas | 12 meses de prueba; supuesto de costo; residuos no normales (Jarque-Bera p = 0,001, S2); MA estacional ≈ −1 (−0,970); covid con una sola indicadora; sin temperatura | §3 y S2 |

## 5. Orden sugerido

1. **Redactar las 3 celdas [AUTOR] del borrador de la Formativa** (§4), usando las cifras de la tabla 4 de este informe.
2. Armar el **documento de una página** (PDF o DOCX, `mcdi505_s4rmoncada`): párrafo de apertura, Figura 1, tabla de modelos reformateada, recomendación y limitación.
3. Completar la **declaración de IA** (en el documento y en el anexo).
4. Borrar los [BORRADOR], reiniciar el kernel, ejecutar todo y adjuntar el notebook como anexo.
5. Entregar antes del **viernes 23 de octubre, 23:59**, y luego incorporar la retroalimentación en la Sumativa 4 (5 a 7 páginas).

## 6. Para la Sumativa 4 (después de la retroalimentación)

Criterios adicionales a los de la Formativa: **ortografía y redacción** y **formato** (5 a 7 páginas, anexo ejecutado, APA, nombre y plazo). El banco de evidencia y el mapa de secciones están en `docs/esquema_informe_s4rmoncada.md`.
