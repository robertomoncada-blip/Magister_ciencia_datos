# Brechas: Formativa 4 / Sumativa 4 (`mcdi505_s4rmoncada.ipynb` y borrador del informe)

- **Fecha de revisión:** 20 de octubre de 2026
- **Documentos de referencia:** `MCDI505_Formativa4_instrucciones_v2.pdf` (3 criterios de contenido, 9 puntos cada uno; formativa, 0 %), `MCDI505_S4_guia_de_compania.pdf` y `MCDI505_Sumativa4_instrucciones_v2.pdf` (5 criterios, para la etapa siguiente)
- **Ejecución de control:** con kernel nuevo, sobre una copia: **9/9 celdas de código, en orden y sin errores**; 1 figura (Figura 1)
- **Plazo de la Formativa 4:** **viernes 23 de octubre**, 23:59. La guía movió la fecha desde el miércoles: «si algún otro documento indica el miércoles, rige esta fecha»

## Decimocuarta revisión (25 de octubre): informe ejecutivo de la Sumativa 4 en PDF

**Cómo se armó:** con `scripts/construir_informe_s4.py` (ReportLab, Calibri 11, carta), que lee el notebook en cada ejecución. Los **textos se copian literalmente** de las celdas del autor (§1, §2, §3, §3.1, bloques 1 a 3 de la §4, Referencias y declaración de IA); las celdas `[BORRADOR]` se ignoran. Se comprobó por programa que **todos los párrafos y viñetas del autor están en el PDF**; solo se omiten los rótulos internos del notebook («(§1)», «(§3, criterio 3)», «Notas para el informe», «**Tabla 2 (§2).**»). Tablas y figuras se recalculan con el mismo código del anexo, con la **misma numeración** (Tablas 1 a 5, Figuras 1 y 2), para que las referencias del texto sigan valiendo. **Agregado por el asistente** (forma, no contenido): título y subtítulo, encabezado, títulos de sección según la rúbrica, títulos y notas APA de tablas y figuras (unidades y fuente), pie de página. Para regenerar tras cambiar un texto: `../.venv/Scripts/python.exe -I scripts/construir_informe_s4.py` desde `MCDI505/`.

### A. Instrucciones específicas

| Criterio | En el PDF | Estado |
|---|---|---|
| 1. Problema, datos, metodología y solución, para audiencias estratégicas y operativas, con visualizaciones | §1: bloque 1, Figura 1, evaluación 2023 y 2024, Tabla 1 | ✅ |
| 2. Sustento técnico con la evidencia de las semanas 2 a 4 (dependencia, volatilidad, ajuste, pronóstico 2023 y 2024); por qué no aportan los modelos avanzados | §2: bloque 2, «¿Por qué se eligió…?», Tabla 2 (B, A, ARFIMA, GARCH y naive), Cadena de evidencia (ADF, KPSS, H, ARCH-LM, MASE) | ✅ |
| 3. Conclusiones y recomendaciones accionables, con cifras, limitaciones y alcances | §3: recomendación con cifra, prueba 2024 (Tabla 3), plan 2025 (Tabla 4), sensibilidad (Tabla 5 y Figura 2), cinco limitaciones | ✅ (una sola recomendación accionable: decisión del autor) |
| Incorporar la retroalimentación del borrador | Sensibilidad del cuantil y referencias | ✅ |

### B. Aspectos formales

| Requisito | Estado |
|---|---|
| PDF o DOCX de 5 a 7 páginas | ✅ PDF de **6 páginas** |
| Anexo: notebook ejecutado | ✅ `notebooks/mcdi505_s4rmoncada.ipynb` (11/11 celdas, sin errores); entregarlo junto al PDF |
| Estructura sugerida (encabezado; síntesis; sustento; conclusiones; referencias; declaración de IA) | ✅ En ese orden |
| Sin código; figuras numeradas; tablas reformateadas; interpretación en prosa | ✅ Sin código (búsqueda automática); Figuras 1-2 y Tablas 1-5 con formato APA |
| APA en citas y referencias | ✅ 13 referencias, todas citadas, con sangría francesa |
| Nombre `mcdi505_s4inicialapellido` | ✅ `entregas/mcdi505_s4rmoncada.pdf` (reemplaza el PDF de la Formativa 4, que sigue en el historial: commit `1bcfc39`) |
| Plazo | ⚠️ Según el PDF, **hoy domingo 25 de octubre, 23:59**; confirmar en Canvas |

### C. Pendientes del autor antes de entregar

1. **P1 · Declaración de IA:** el PDF reproduce la declaración actual, que **no describe todo el apoyo**: código de las Tablas 2 a 5 y las Figuras 1 y 2, verificación de cifras, preguntas guía de la §3.1, correcciones «dice / debe decir», lista de referencias y **armado de este PDF** (diagramación, tablas, figuras y notas de tabla con los textos del autor). Además, «se generó el PDF ejecutivo» no dice quién lo generó. Corregirla en el notebook y regenerar el PDF; si hay dudas sobre el código hecho por la IA, consultar al docente.
2. **P3 · Repeticiones:** la §1 y la §3 repiten ideas de los bloques 1 y 3 (por ejemplo, el «≈ 40 % menos de error» y el «39 % menos de costo»). Si se quiere, acortar alguno de los dos textos en el notebook.
3. Regenerar `entregas/mcdi505_s4rmoncada.zip` con el PDF, el notebook final y el CSV, y validarlo descomprimiendo en una carpeta vacía.

---

## Decimotercera revisión (25 de octubre): 3.ª ronda contra la Sumativa 4

> Revisión con la skill `validador-notebooks-rubrica` contra `MCDI505_Sumativa4_instrucciones_v2.pdf`. Los niveles son **estimaciones**, no una calificación. Los textos del autor no se modificaron; las 5 correcciones nuevas están en `[BORRADOR] Correcciones «Dice / Debe decir» (3.ª ronda)`, antes de la declaración de IA, y sus 5 «Dice» se verificaron como texto literal.

### A. Qué cambió el autor desde la duodécima revisión

| Cambio | Estado |
|---|---|
| Correcciones 1 a 6 de la 2.ª ronda (§3.1 y bloque 3) | ✅ Aplicadas. La viñeta 1 ya concuerda con la Tabla 5 (q* de 66,7 % a 80 %; 75 % cuesta ≤ 2,9 % sobre el óptimo) |
| Correcciones 7 a 15 (referencias) | ✅ Nota del asistente borrada; Hurst, Engle, Hyndman y Koehler, Ljung y Box, Box et al., UNAB s. f.-a e Hyndman y Athanasopoulos citados; Bollerslev y Seabold eliminados. **Las 13 entradas de la lista se citan en el texto y todas las citas tienen entrada** |
| Corrección 16 (año de Box et al.) | ✅ Se mantuvo 2015, igual que en las Sumativas 2 y 3 |
| Correcciones 17 y 18 (declaración de IA) | ❌ Sin aplicar (siguen pendientes desde la 1.ª ronda) |
| Recuadro `[BORRADOR]` de la 1.ª ronda | ⚠️ **Reapareció** (probablemente al guardar desde un buffer de VS Code sin recargar). Se quitó: sus «Dice» ya no eran texto actual |
| Código y salidas | Sin cambios |

### B. Resultado de Run All

**APROBADO** (`nbclient`, carpeta limpia, kernel nuevo, 0 errores, 11/11 celdas en orden, 2 figuras). N1: las cifras sin coincidencia literal son las ya conciliadas (S2, S3 o derivadas de la Tabla 2) y «3,56», que venía del CSS del recuadro antiguo. A2: falso positivo (DOI de Kwiatkowski et al., `90104-Y`). C1, S1 y E1 no aplican al anexo de la S4.

### C. Cruce con la rúbrica de la Sumativa 4

| # | Criterio | Evidencia citada (anexo) | Nivel estimado | Brecha |
|---|---|---|---|---|
| 1 | Informe ejecutivo | §4, bloque 1 y Figura 1 | **Sin evidencia**: el informe de 5 a 7 páginas no existe (`entregas/` solo tiene el PDF y el ZIP de la Formativa, del 21 de octubre) | Redactar el informe |
| 2 | Sustento técnico | §2, Cadena de evidencia: «(H = 0,652, compatible con ruido blanco; Hurst, 1951) ni volatilidad condicional (ARCH-LM p = 0,639; S3; Engle, 1982)… (MASE 0,61, S4; Hyndman y Koehler, 2006)» · Tabla 2 | Potencial **Excelente** (9) | Llevarlo al informe con sus cifras |
| 3 | Conclusiones y recomendaciones | §3.1: «Aunque el cuantil óptimo varía entre 66,7 % y 80 % (1.476,7 a 1.514,9 GWh), contratar el 75 % cuesta como máximo 2,9 % más que el óptimo» · bloque 3 con la limitación cuantificada · cinco limitaciones (§3) | Potencial **Excelente** (9) | Sigue habiendo **una** recomendación accionable (contratar el 75 %); la rúbrica habla de recomendaciones. Decisión del autor |
| 4 | Ortografía y redacción | Textos sin errores relevantes; dos ajustes de forma (correcciones 4 y 5) | Potencial **Excelente** (9) | — |
| 5 | Formato y entrega | Nombre ✅; anexo ejecutado ✅; **referencias APA completas y todas citadas** ✅ | Anexo **Excelente**; el criterio completo depende del informe, el plazo y la declaración | Informe de 5 a 7 páginas en PDF o DOCX, sin código, con las mismas referencias |

### D. Correcciones de la 3.ª ronda

| Prioridad | # | Ubicación | Problema |
|---|---|---|---|
| **P1** | 1 | Declaración de IA | No describe todo el apoyo recibido |
| **P1** | 2 | Declaración de IA | «se generó el PDF ejecutivo» se refiere al PDF de la Formativa; ajustarlo al informe de la Sumativa |
| P3 | 3 | Declaración de IA | Espacio después de la barra |
| P3 | 4 | §3.1, viñeta 3 | «sería menor y … y …»: repetición y doble «y» |
| P3 | 5 | §3.1, viñeta 1 | «k = 2-4» → «k = 2 a 4» |

### E. Pendientes que solo el autor puede resolver

1. ⚠️ **Plazo:** según el PDF vence **hoy, domingo 25 de octubre, a las 23:59**; la guía remite a Canvas.
2. **Redactar el informe de 5 a 7 páginas**: el anexo ya está listo como respaldo.
3. Redactar la declaración de IA (correcciones 1 y 2); si hay dudas sobre el código hecho por la IA, consultar al docente.
4. **Borrar la celda `[BORRADOR]`**, ejecutar desde un kernel reiniciado y regenerar `entregas/mcdi505_s4rmoncada.zip` con el notebook, el CSV y el PDF del informe.

**Antes de editar en VS Code:** recargar el notebook desde el disco. Si se guarda el buffer antiguo, vuelven a aparecer celdas borradas o se pierde la celda nueva.

---

## Duodécima revisión (25 de octubre): validación de los cambios del autor contra la Sumativa 4

> Revisión con la skill `validador-notebooks-rubrica` contra `MCDI505_Sumativa4_instrucciones_v2.pdf`. Los niveles son **estimaciones**, no una calificación. Los textos del autor no se modificaron: las 18 correcciones nuevas están en la celda `[BORRADOR] Correcciones «Dice / Debe decir» (2.ª ronda)`, antes de la declaración de IA; los 17 «Dice» con cita se verificaron como texto literal.

### A. Qué cambió el autor desde la undécima revisión

| Cambio | Estado |
|---|---|
| Correcciones 1 a 5 de la 1.ª ronda (encabezado, cita de Arrow et al. y UNAB, «pasa a 67 % o a 80 %», Jarque y Bera, Dickey y Fuller y Kwiatkowski et al.) | ✅ Aplicadas tal cual |
| Conclusiones propias de la §3.1 (3 viñetas) | ✅ Escritas. ⚠️ La viñeta 1 no coincide con la Tabla 5 (corrección 2) |
| Recuadros `[BORRADOR]` de la 1.ª ronda | ✅ Borrados; la lista de referencias quedó como sección «Referencias (APA 7)» |
| Correcciones 6 y 7 (declaración de IA) | ❌ Sin aplicar |
| Código y salidas | Sin cambios: `execution_count` 1..11 y salidas de la ejecución anterior |

### B. Resultado de Run All

**APROBADO** (`nbclient`, carpeta limpia con el notebook y el CSV, kernel nuevo, 0 errores, 11/11 celdas en orden, 2 figuras). N1: 0,001; 0,040; 0,463; 0,639; 0,652 y 8,82 están citadas a la S2 o la S3; 0,03 es derivada de la Tabla 2. Las cifras nuevas del autor (1,5 %, 2,9 %, 1,75) aparecen en la salida de la Tabla 5. Reglas que no aplican al anexo de la S4: C1, S1 y E1 (heurística de 10 a 15 páginas de la Sumativa 1). A2 es un falso positivo (DOI de Seabold y Perktold).

### C. Cruce con la rúbrica de la Sumativa 4

| # | Criterio | Evidencia citada (anexo) | Nivel estimado | Brecha |
|---|---|---|---|---|
| 1 | Informe ejecutivo | §4, bloque 1 y Figura 1 | **Sin evidencia**: el informe de 5 a 7 páginas no existe aún (`entregas/` solo tiene el PDF y el ZIP de la Formativa, del 21 de octubre) | Redactar el informe |
| 2 | Sustento técnico | §2, Cadena de evidencia (ahora con citas de ADF y KPSS) · Tabla 2 | Potencial **Excelente** (9) | Citar Hurst, Engle, Hyndman y Koehler y Ljung y Box donde se usan (correcciones 8 a 11) |
| 3 | Conclusiones y recomendaciones | §3.1: «La recomendación del 75 % es robusta dentro del rango k = 2-4.» · «un sobrecosto estimado entre 1,5 % y 2,9 %» · «La recomendación cambiaría si la relación de precios spot bajara de k < 1,75.» · §3: cinco limitaciones | **Bueno → Excelente** (6-9) | ⚠️ **P1:** la viñeta 1 dice que «el nivel óptimo prácticamente no cambia», pero q* va de 66,7 % a 80 % (1.476,7 a 1.514,9 GWh); lo robusto es el costo del 75 % (≤ 2,9 % sobre el óptimo). La viñeta 2 propone reformular la limitación, pero el bloque 3 sigue igual (corrección 6). Sigue habiendo una sola recomendación accionable |
| 4 | Ortografía y redacción | Textos sin errores relevantes; precisiones en las correcciones 1, 3, 4 y 5 | Potencial **Excelente** (9) | Viñeta 2 en formato pregunta–respuesta («Sí, conviene…») |
| 5 | Formato y entrega | Nombre ✅; anexo ejecutado ✅; **referencias:** 15 en la lista y **solo 6 citadas** (Arrow, Gneiting, Dickey, Kwiatkowski, Jarque, UNAB s. f.-b); queda una nota del asistente en la celda de Referencias | **Insuficiente → Bueno** hoy; **Excelente** con el informe y las correcciones 7 a 16 | Citar o eliminar las 9 entradas sin cita; borrar la nota (corrección 7); unificar el año de Box et al. |

### D. Correcciones priorizadas (detalle en la celda `[BORRADOR]` del notebook)

| Prioridad | # | Ubicación | Problema |
|---|---|---|---|
| **P1** | 2 | §3.1, viñeta 1 | Afirmación que contradice la Tabla 5 (q* sí cambia) |
| **P1** | 7 | Referencias | Párrafo del asistente dentro de la celda final |
| **P1** | 17 | Declaración de IA | No describe todo el apoyo (código de las Tablas 2 a 5 y las Figuras 1 y 2, preguntas guía de la §3.1, referencias, PDF) |
| P2 | 3, 4, 6 | §3.1 y §4, bloque 3 | Precisión de la sensibilidad; coherencia de la limitación con la Tabla 5 |
| P2 | 8 a 14 | §2, §3, §4 y encabezado | Citas APA para que las referencias de la lista queden citadas |
| P3 | 1, 5, 15, 16, 18 | Varias | Forma: título, «cobertura», Bollerslev y Seabold, año de Box et al., espacio en la tabla |

### E. Pendientes que solo el autor puede resolver

1. ⚠️ **Plazo:** según el PDF vence **hoy, domingo 25 de octubre, a las 23:59**; la guía remite a Canvas. Confirmar.
2. **Redactar el informe de 5 a 7 páginas** (PDF o DOCX, sin código), con la §3.1 y solo las referencias citadas.
3. Decidir las 18 correcciones, **borrar la celda `[BORRADOR]`** y ejecutar el notebook desde un kernel reiniciado.
4. Redactar la declaración de IA con todo el apoyo recibido; si hay dudas sobre el código hecho por la IA, consultar al docente.
5. Regenerar `entregas/mcdi505_s4rmoncada.zip` con el notebook final, el CSV y el PDF del informe.

**El notebook se modificó en disco** (se agregó una celda de markdown): si está abierto en VS Code, recargarlo sin guardar el buffer abierto, o se perderá la celda nueva al guardar.

---

## Undécima revisión (25 de octubre) · BORRADOR: validación contra la Sumativa 4 y feedback del profesor

> **Modo borrador.** Revisión hecha con la skill `validador-notebooks-rubrica` contra `MCDI505_Sumativa4_instrucciones_v2.pdf` (5 criterios, 9 puntos cada uno, 25 % de la nota). Los niveles son **estimaciones**, no una calificación. Lo calificado en la Sumativa es el **informe ejecutivo de 5 a 7 páginas**; el notebook es su anexo y «no se califica por separado». Los textos del autor no se modificaron: las propuestas están en celdas `[BORRADOR]` del notebook.

**Feedback del profesor a la Formativa 4:** «Para la Sumativa, agregue la sensibilidad del cuantil a la razón de costos y si hay referencias».

### A. Qué se agregó al notebook

| Celda | Contenido | Tipo |
|---|---|---|
| §3.1 (título) | «Sensibilidad del cuantil a la razón de costos», con la regla q* = c_u / (c_u + c_o) y su cita (Arrow et al., 1951; Gneiting, 2011) | Código / encabezado |
| §3.1, **Tabla 5** | Para k = c_u / c_o = 1; 1,5; 2; 2,5; 3; 3,5; 4; 5; 6: q*, volumen 2025, % sobre la media, **costo esperado 2025** (distribución predictiva log-normal, fórmula cerrada) contratando q*, el 75 % o la media, y **costo real 2024** (prueba retrospectiva) con q* y con la media. Imprime además el **punto de cruce** k = 1,75 | Código |
| §3.1, **Figura 2** | Izquierda: volumen 2025 según k. Derecha: sobrecosto esperado de fijar el 75 % o la media si la razón real es otra. Rango del caso (2 a 4) sombreado | Código |
| [BORRADOR] Ideas §3.1 | Cifras y 4 preguntas para que el autor redacte la interpretación | Borrador (borrar antes de entregar) |
| [BORRADOR] Dice / Debe decir | 7 correcciones (abajo, sección D) | Borrador |
| [BORRADOR] Referencias (APA 7) | 15 referencias; DOI de Arrow et al. (1951) y Gneiting (2011) verificados en Crossref | Borrador |

**Controles de la Tabla 5:** con k = 2, 3 y 4 reproduce la Tabla 3 (62,3 / 89,3; 79,8 / 130,6; 95,5 / 171,9) y con k = 3 el plan 2025 (1.499,3 GWh). La fórmula cerrada del costo esperado se contrastó con Monte Carlo (4 millones de draws): 7,763 frente a 7,759.

### B. Resultado de Run All

| Regla | Estado | Detalle |
|---|---|---|
| Ejecución limpia (carpeta nueva con notebook + CSV, kernel nuevo) | ✅ OK | `nbclient`, 0 errores |
| Orden y estado guardado | ✅ OK | `execution_count` = 1..11; todas las celdas con salida; 2 figuras |
| Portabilidad | ✅ OK | Ruta relativa al CSV; `SEMILLA = 505` |
| Consistencia (N1) | ✅ OK tras revisión manual | 0,001; 0,040; 0,463; 0,639; 0,652; 8,82 están citadas a la S2 o la S3; 0,03 es derivada de la Tabla 2; «3,56» es un falso positivo (color CSS de los recuadros) |
| Dependencias | ✅ OK | numpy, pandas, matplotlib, scipy (se agrega `brentq`), statsmodels del `.venv` |
| R6 advertencias | ℹ️ OBS | `filterwarnings("ignore")` viene de la plantilla oficial |
| A2 APA | ℹ️ OBS | Falso positivo: el «guion» está dentro de un DOI (`Majora-92bf1922-011`) |
| C1 / S1 | No aplican | Reglas de la Sumativa 1 (celdas 0, 2 y 5 sin comentarios son de la plantilla; no hay ACF ni descomposición en la S4) |

**Veredicto: APROBADO** (motor `nbclient`).

### C. Cruce con la rúbrica de la Sumativa 4

| # | Criterio | Evidencia citada (anexo) | Nivel estimado | Brecha para subir o asegurar el nivel |
|---|---|---|---|---|
| 1 | Informe ejecutivo: problema, metodología y solución (ID 4.1) | §4, bloque 1: «Decisión: elegir cuánta energía contratar para el año siguiente.» · «se analizaron 10 años de consumo mensual (2015-2024)» · Figura 1 | **Sin evidencia** en formato de informe: el PDF actual es el borrador de 2 páginas de la Formativa. Potencial **Excelente** si el informe desarrolla estos textos | Redactar la síntesis (≈ 1½ pág.) con 1-2 figuras numeradas (esquema, §1) |
| 2 | Sustento técnico (ID 3.2) | §2, Cadena de evidencia: «ADF = −8,82 (frente al valor crítico −2,90) y KPSS = 0,040 (frente a 0,463)… (H = 0,652, compatible con ruido blanco) ni volatilidad condicional (ARCH-LM p = 0,639; S3)… (MASE 0,61, S4)» · Tabla 2 | Potencial **Excelente** (9) | En el informe, explicar con cifras **por qué** H = 0,652 no es memoria larga (S3: con ruido blanco, IC 95 % [0,392; 0,823]) y la persistencia GARCH α + β = 0,509. Citar los métodos (corrección 5) |
| 3 | Conclusiones y recomendaciones (ID 4.1) | §3: «el cuantil 75 % redujo los faltantes a 13,8 GWh en 3 meses y disminuyó el costo a 79,8, cerca de 39 % menos» · cinco limitaciones con efecto · §4, bloque 3 · **Tabla 5 y Figura 2 (nuevas)** | **Bueno → Excelente** (6-9) | ⚠️ Falta la **interpretación del autor** de la §3.1 (feedback del profesor). La rúbrica pide recomendaciones en plural: hoy hay una (contratar el 75 %). Ideas que el autor puede evaluar: revisar k cada año con los precios spot; reestimar el modelo al cerrar cada año; vigilar el sesgo positivo (9/12 meses en 2024) |
| 4 | Ortografía y redacción | Textos del anexo sin errores relevantes (octava revisión); 3 precisiones nuevas (correcciones 1, 3 y 7) | Potencial **Excelente** (9) | Revisar el informe nuevo con el mismo control |
| 5 | Formato y entrega | Nombre ✅; anexo ejecutado ✅; **referencias: el notebook no tenía** sección ni citas APA en el texto (regla A1: 0 citas) | **Insuficiente → Excelente** según lo que falte al entregar | Informe de **5 a 7 páginas** en PDF o DOCX, sin código; lista APA con solo lo citado; citas en el texto (correcciones 2, 4 y 5); plazo |

### D. Correcciones «Dice / Debe decir» (en la celda [BORRADOR] del notebook; los 7 «Dice» se verificaron como texto literal)

| # | Celda | Dice | Debe decir | Prioridad |
|---|---|---|---|---|
| 1 | Encabezado | «…se incluyeron tres secciones de apoyo para el informe: … y notas de apoyo para la Formativa 4.» | «…se incluyeron cuatro secciones de apoyo…, su sensibilidad a la razón de costos y notas de apoyo para el informe de la Sumativa 4.» | P3 |
| 2 | §3, párrafo 1 | «80 % (4:1) (Notebook S2, §8).» | «80 % (4:1), según la regla del vendedor de diarios, q* = c_u / (c_u + c_o) (Arrow et al., 1951; Universidad Andrés Bello, s. f.-b).» | **P1** (feedback) |
| 3 | §3, Limitaciones | «el cuantil óptimo pasa de 67 % a 80 %.» | «el cuantil óptimo pasa a 67 % o a 80 %, respectivamente (Tabla 5).» | P2 |
| 4 | §3, Limitaciones | «(Jarque-Bera p = 0,001, Semana 2)» | «(…, Semana 2; Jarque y Bera, 1987)» | P3 |
| 5 | §2, Cadena de evidencia | «ADF = −8,82 (frente al valor crítico −2,90) y KPSS = 0,040 (frente a 0,463).» | Agregar «Dickey y Fuller, 1979» y «Kwiatkowski et al., 1992» | P2 |
| 6 | Declaración de IA | «Se utilizó como borrador y apoyo práctico para el código de las secciones, borrador de ideas y guías de interpretación.» | Describir con exactitud: el asistente programó las Tablas 2 a 5 y las Figuras 1 y 2, verificó cifras, propuso las correcciones y la lista de referencias, y armó el PDF de la Formativa 4 | **P1** |
| 7 | Declaración de IA | «\|Se utilizó» | «\| Se utilizó» | P3 |

### E. Cifras de la sensibilidad (Tabla 5) para el autor

| k = c_u / c_o | q* | Volumen 2025 (GWh) | Sobre la media | Sobrecosto esperado del 75 % | Sobrecosto esperado de la media | Ahorro 2024 de q* frente a la media |
|---|---|---|---|---|---|---|
| 2 | 66,7 % | 1.476,7 | +2,5 % | +2,9 % | +8,2 % | 30,2 % |
| 3 | 75,0 % | 1.499,3 | +4,1 % | 0,0 % | +22,8 % | 38,9 % |
| 4 | 80,0 % | 1.514,9 | +5,2 % | +1,5 % | +38,6 % | 44,4 % |

Fuera del rango: con k = 1 el 75 % cuesta +22,5 % (la media, +0,1 %); con k = 6, +8,9 %. La media solo conviene con k < 1,75.

### F. Pendientes que solo el autor puede resolver

1. ⚠️ **Plazo:** el PDF dice «hasta las 23:59 hrs. del domingo de la Semana 4», que es **hoy, domingo 25 de octubre**; la guía de compañía dice «plazo publicado en Canvas». Confirmar en Canvas.
2. **Redactar el informe de 5 a 7 páginas** (no existe aún) con el esquema de `docs/esquema_informe_s4rmoncada.md`, incluida la interpretación de la Tabla 5 y la Figura 2.
3. Decidir las correcciones 1 a 7 y **borrar las tres celdas `[BORRADOR]`** antes de entregar; volver a ejecutar el notebook desde un kernel reiniciado.
4. **Declaración de IA:** redactarla con todo el apoyo recibido, incluido este (código de la §3.1, lista de referencias). Si hay dudas sobre el código hecho por la IA, consultar al docente en el foro.
5. Año de Box et al.: la guía usa 2016; las Sumativas 2 y 3, 2015. Usar uno solo.
6. Regenerar el ZIP de entrega (`entregas/mcdi505_s4rmoncada.zip`) con el notebook final, el CSV y el PDF del informe.

**El notebook se modificó en disco:** si está abierto en VS Code, recargarlo sin guardar el buffer abierto.

---

## Décima revisión (21 de octubre): PDF regenerado con la «Cadena de evidencia»

Se regeneró `entregas/mcdi505_s4rmoncada.pdf` incorporando al **bloque 2**, de forma **literal**, el párrafo «Cadena de evidencia» del autor (§2 del notebook). Sigue en 2 páginas y el texto completo cabe en la página 1.

- ✅ **Criterio 2 resuelto:** el bloque 2 ahora muestra la evidencia acumulada que pide la rúbrica: dependencia temporal (ADF −8,82 frente a −2,90; KPSS 0,040 frente a 0,463; H = 0,652, compatible con ruido blanco), volatilidad (ARCH-LM p = 0,639) y pronóstico (MASE 0,61). Nivel probable: **Excelente (9)**.
- **Rúbrica de la Formativa 4: 27 / 27 estimado.**
- **Pendiente del autor:** la declaración de IA debe decir que el asistente **armó el PDF** (diagramación, figura y tabla) con sus textos. Opcional: explicar «cuantil 75 %» sin jerga. Si cambia algún texto en el notebook, regenerar el PDF.

---

## Novena revisión (21 de octubre): PDF de la Formativa 4 (`entregas/mcdi505_s4rmoncada.pdf`)

**Cómo se armó:** con los **textos del autor copiados literalmente** de la §4 del notebook (bloques 1 a 3) y de la declaración de IA. La Figura 1 se regeneró con el mismo código del anexo y la Tabla 1 se reformateó desde la Tabla 2 del anexo (mismas cifras, redondeadas a 2 decimales). Únicos cambios de forma: se quitó la referencia interna «**Tabla 2 (§2).**» del bloque 2 y se agregaron el título, la línea de datos (curso, autor, fecha, archivo y anexo), los títulos de bloque, las notas de figura y tabla, y una línea que remite a la Tabla 1. Verificado: 2 páginas; las cifras de la Tabla 1 coinciden con el anexo.

### A. Instrucciones específicas

| Instrucción | En el PDF | Estado |
|---|---|---|
| Borrador de una página con 3 bloques, en el orden de la rúbrica | Página 1: bloques 1, 2 y 3 | ✅ |
| **Bloque 1:** párrafo de apertura de 5 a 8 líneas, sin jerga | 8 líneas: decisión, costo en ambas direcciones, datos, metodología y solución | ✅ |
| **Bloque 1:** figura clave (serie, pronóstico 2024 e intervalo) | Figura 1, página 2 | ✅ |
| **Bloque 2:** tabla del modelo final, las alternativas descartadas en S2 y S3 y el naive, con métricas 2023 y 2024 | Tabla 1: B, A, B + ARFIMA, B + GARCH y naive; RMSE, MAE y MASE en 2023 y 2024, más cobertura 2024 | ✅ |
| **Bloque 2:** una frase de por qué se eligió el modelo final | Frase con cifra (RMSE 6,85; empate en 2024; único que pasó Ljung-Box en la S2) | ✅ |
| **Bloque 3:** recomendación en 1-2 frases con su cifra y la limitación más importante | Cuantil 75 % = 1.499,3 GWh (+4,1 %); −39 % de costo en 2024; limitación: costo 3 a 1 y 12 meses | ✅ |

### B. Aspectos formales

| Requisito | Estado |
|---|---|
| PDF o DOCX | ✅ PDF |
| Una página (la tabla y la figura pueden ocupar una segunda) | ✅ Página 1 = texto; página 2 = figura y tabla. ⚠️ La **declaración de IA** también va en la página 2: no está prevista en ese espacio, pero la entrega debe declarar el uso de IA. Riesgo bajo; alternativa: acortarla y ponerla al pie de la página 1 |
| Nombre `mcdi505_s4inicialapellido` | ✅ `mcdi505_s4rmoncada.pdf` |
| Plazo | ⚠️ El PDF de instrucciones dice **miércoles 21 de octubre, 23:59** (hoy); la guía de compañía lo movió al viernes 23 |
| Anexo (guía) | ✅ `notebooks/mcdi505_s4rmoncada.ipynb`, ejecutado 9/9 |

### C. Cruce con la rúbrica (3 criterios de contenido)

| # | Criterio | Evidencia en el PDF | Nivel probable | Brecha |
|---|---|---|---|---|
| 1 | Problema, metodología y solución | Narrativa clara para la Gerencia + Figura 1 | **Excelente** (9) | Opcional: en el bloque 3, «cuantil 75 %» es jerga para la Gerencia; explicarlo en palabras simples (p. ej., «un volumen que cubre el consumo en 3 de cada 4 escenarios») |
| 2 | Sustento técnico | Tabla 1 + frase con cifra | **Bueno → Excelente** (6-9) | ⚠️ El descriptor de la rúbrica pide la evidencia **acumulada (dependencia temporal y volatilidad)**. El PDF solo muestra métricas: no dice **por qué** se descartaron ARFIMA y GARCH (H = 0,652, compatible con ruido blanco; ARCH-LM p = 0,639). Ya existe un texto propio que lo dice: el párrafo «**Cadena de evidencia**» de la §2 del notebook. Llevarlo al bloque 2 (cabe en la página 1) |
| 3 | Conclusiones y recomendaciones | Recomendación con cifra + limitación | **Excelente** (9) | — |
| | **Total estimado** | | **24-27 / 27** | |

### D. Pendientes del autor

1. **Declaración de IA (exactitud):** dice «se generó el PDF ejecutivo», pero no que el asistente **armó el PDF** (diagramación, figura y tabla) a partir de los textos del autor. Conviene agregarlo en «¿En qué partes específicas?».
2. **Criterio 2:** agregar al bloque 2 el párrafo propio «Cadena de evidencia» (o una frase con H = 0,652 y ARCH-LM p = 0,639).
3. Opcional: explicar «cuantil 75 %» sin jerga; ubicar la declaración al pie de la página 1.
4. Si se cambia algún texto en el notebook, regenerar el PDF para que ambos coincidan.

---

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
