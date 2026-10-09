# Validación preliminar — `mcdi505_f2rmoncada.ipynb` frente a la Rúbrica Formativa 2 (f2_s2)

- **Fecha de revisión:** 9 de octubre de 2026
- **Versión revisada:** commit `8520d5a`, más las correcciones del 9 de octubre descritas en «Actualización» (notebook ejecutado completo, 11/11 celdas de código, sin errores)
- **Rúbrica:** `Rúbrica_formativa_f2_s2`, 6 criterios de 9 puntos (total 54)
- **Alcance:** revisión del contenido ejecutado, más mediciones aparte: extensión, citas, marcas pendientes y coeficientes de los modelos. Es una estimación de cumplimiento, no una nota.

## Actualización (9 de octubre de 2026): brechas resueltas

- **Tabla 2 con coeficientes e invertibilidad:** muestra cada coeficiente con su error estándar y valor-p, y una columna «mín. |raíz MA|». La verificación confirmó la brecha: sin la restricción de invertibilidad, el MA estacional de A y B y el MA regular de C llegan a −1,00, y la log-verosimilitud cambia menos de 0,03. El texto de la sección 2 incluye ahora una nota técnica: los errores estándar de esos términos no son fiables, un MA estacional cercano a −1 indica estacionalidad casi determinista y un MA regular cercano a −1, posible sobrediferenciación (241 palabras, dentro del límite).
- **Referencias y citas APA:** la lista sigue APA 7 en español: «y» en lugar de «&», editores y páginas en Seabold y Perktold (2010), número 366a en Dickey y Fuller (1979) y la referencia original de Box-Cox (Box y Cox, 1964). Las 13 referencias se citan en el texto: notas de método, Hoja de decisiones y textos de interpretación.
- **Coma decimal:** todas las tablas y los textos impresos usan coma decimal. Los ejes de los gráficos siguen con el formato de matplotlib.
- **Transformación con evidencia cuantitativa:** la validación mostró que el λ de Box-Cox (0,00) tiene un IC de 95 % de −1,45 a 1,49, que incluye 0 y 1, y que sin 2020-2021 la variabilidad anual crece poco con el nivel (elasticidad 0,25). El texto de la sección 1 y la Hoja ahora lo dicen, y el logaritmo se justifica por λ ≈ 0 y porque los efectos se leen en porcentaje, no por una variabilidad que crezca con fuerza.
- **Hoja de decisiones con cifras:** las 5 marcas `[COMPLETAR]` se reemplazaron por las cifras de la ejecución. La celda de apoyo verifica que las 15 cifras clave de la Hoja coincidan con los resultados (hoy coinciden todas).
- **Selección sin empate:** la regla usa el RMSE y MAE promedio con origen móvil (pronósticos de 2021, 2022 y 2023, reestimando con los datos hasta el año anterior) y exige superar al naive y pasar Ljung-Box en los rezagos 12 y 24. Puntajes: A 1, B 2 y C 3. A queda primero pero no es elegible (Ljung-Box p = 0,019 en el rezago 24), y C tampoco (no supera al naive y p = 0,047). Se elige **B**: RMSE móvil 7,12 frente a 7,72 GWh del naive (7,8 % menos), pero MAE móvil prácticamente igual (6,64 frente a 6,66). El cambio de regla se declara en la Hoja como ajuste respecto de la versión anterior.
- **Normalidad que falla, analizada:** los residuos de B tienen colas pesadas (curtosis en exceso 1,83). Sin marzo-junio de 2020, Jarque-Bera da p = 0,215 y Shapiro-Wilk p = 0,111: la falta de normalidad se concentra en el inicio del COVID-19, que un solo indicador `covid` no captura. El intervalo de 95 % cubrió 94,4 % de los 36 meses del origen móvil (binomial p = 0,701), así que está bien calibrado en la práctica. Un indicador adicional para abril-junio de 2020 corrige la normalidad (p = 0,226), pero deja autocorrelación en el rezago 24 (p = 0,039); queda en las conclusiones como mejora posible. La Tabla 4, el texto de la sección 4 (202 palabras), la fila 4 de la Hoja y su verificación de cifras están actualizados.
- **Efecto en la extensión:** con todos los cambios, el notebook pasa de unas 7,6 a unas **9,3 páginas** (3.122 palabras, 5 figuras y 32 filas de tabla, sin contar el código). Sigue por debajo de las 10 que pide la rúbrica.

Las demás brechas siguen abiertas; las tablas siguientes marcan cuáles quedaron resueltas.

## Resumen

| # | Criterio | Nivel probable hoy | Puntaje probable | Brecha principal |
|---|---|---|---|---|
| 1 | Estacionariedad y transformaciones (ID 2.2) | Excelente / Bueno | 6–9 | **Resuelto:** Hoja con cifras y transformación cuantificada. Pendiente: interpretación propia |
| 2 | Identificación y estimación (ID 2.1) | Bueno / Excelente | 6–9 | **Resuelto:** coeficientes e invertibilidad reportados y comentados. Pendiente: candidatos AR o MA puros, o explicar por qué no se incluyen |
| 3 | Selección y comparación (ID 2.1) | Bueno / Excelente | 6–9 | **Resuelto:** sin empate (origen móvil + Ljung-Box) y justificación explícita. Pendiente: la ventaja de B sobre el naive es moderada en RMSE y nula en MAE; discutirlo con palabras propias |
| 4 | Diagnóstico de residuos (ID 2.2) | Excelente / Bueno | 6–9 | **Resuelto:** causa de la falta de normalidad y calibración de los intervalos, con cifras. Pendiente: interpretación propia |
| 5 | Ortografía y redacción | Bueno | 6 | Textos aún marcados como «Borrador» y algunos giros poco académicos (la coma decimal ya está corregida) |
| 6 | Formato y entrega | Insuficiente / Bueno | 3–6 | Extensión de unas 9,3 páginas (pide 10–15), nombre de archivo, celda de apoyo y declaración de IA pendientes (las citas ya están corregidas) |
| | **Total estimado** | | **33–48 / 54** | |

Las brechas que más pesan ahora están en el **formato** (criterio 6) y en las **interpretaciones propias**, que afectan a los criterios 1 a 5.

---

## 1. Análisis de estacionariedad y transformaciones (ID 2.2)

**Lo que cumple**
- Aplica ADF y KPSS a la serie original, a la serie en logaritmos y a tres diferenciaciones (Tabla 1). Clasifica cada caso con una regla explícita: estacionaria, no estacionaria o discrepante.
- Decide d = 1 y D = 1 con una regla fijada de antemano (veredicto «estacionaria» y ACF(12) < 0,5). Con esa combinación, ADF da p < 0,001, KPSS p = 0,100 y ACF(12) = −0,30.
- Justifica el logaritmo con cifras: λ de Box-Cox = 0,00 (IC 95 % de −1,45 a 1,49) y elasticidad de la variabilidad anual = 0,25 (sin 2020-2021), reconociendo que el IC también incluye 1.
- Verifica visualmente la estacionariedad resultante (Figura 2). La afirmación de que la variabilidad aumenta en el COVID-19 se comprobó: la desviación de la serie diferenciada es 0,039 fuera de ese periodo y 0,065 dentro.

**Brechas**
| Brecha | Impacto | Acción sugerida |
|---|---|---|
| ~~La fila 1 de la Hoja tiene dos `[COMPLETAR]`~~ **Resuelto:** d = 1 y D = 1, con los valores-p, el IC de λ y la elasticidad | — | — |
| ~~«La variabilidad crece con el nivel» se afirmaba sin cuantificar~~ **Resuelto:** IC de λ y elasticidad en la Tabla 1, la sección 1 y la Hoja | — | — |
| No se aclara que el KPSS p = 0,100 está truncado («0,10 o más») | Riesgo menor de mala lectura | Una frase bajo la Tabla 1 |
| Falta la interpretación propia (el texto actual es un borrador generado) | La rúbrica exige *interpretar* | Reescribir con palabras propias |

## 2. Identificación y estimación de modelos (ID 2.1)

**Lo que cumple**
- ACF y PACF de la serie estacionaria (Figura 3), con banda de ±0,215. Solo el rezago 12 es significativo en la ACF; en la PACF lo son el 12 y el 24.
- La regla explícita sugiere SARIMA(0,1,0)(0,1,1)₁₂, coherente con la evidencia.
- Cuatro candidatos, con parte estacional y una referencia sin estacionalidad, todos con el regresor `covid`. Los cuatro convergen.

**Brechas**
| Brecha | Impacto | Acción sugerida |
|---|---|---|
| ~~La Tabla 2 no muestra coeficientes, errores estándar ni valores-p~~ **Resuelto:** la Tabla 2 los muestra, como dice la Hoja | — | — |
| ~~Términos MA en la frontera de invertibilidad sin comentar~~ **Resuelto:** columna «mín. \|raíz MA\|» (A y B 1,002; C 1,013), reestimación sin restricción (−1,00, Δ log-verosimilitud < 0,03) y nota técnica en la sección 2 | — | Considerar en la reescritura si conviene un modelo con estacionalidad determinista (variables indicadoras de mes) como candidato adicional |
| No hay modelos AR ni MA puros, y no se prueba un AR estacional pese a que la PACF es significativa en el rezago 24 | La identificación es correcta, pero estrecha frente a «AR, MA, ARMA, ARIMA, SARIMA» | Agregar uno o dos candidatos, por ejemplo SARIMA(0,1,1)(1,1,0)₁₂ o un MA(1), o justificar por qué no se incluyen |
| C se llama «ARMA(1,1)», pero es ARIMA(1,1,1)(0,1,0)₁₂ | Puede confundir al evaluador | Nombrarlo «ARMA(1,1) sobre la serie diferenciada (d = 1, D = 1)» |
| ~~La fila 2 de la Hoja tiene un `[COMPLETAR]`~~ **Resuelto:** banda, rezagos significativos, efecto del COVID-19 e invertibilidad | — | — |

## 3. Selección y comparación de modelos (ID 2.1)

**Lo que cumple**
- Compara AIC, BIC, RMSE y MAE en la validación 2023 y con origen móvil (2021-2023) contra el naive estacional, con Ljung-Box de cada candidato, y restringe AIC y BIC a modelos con la misma diferenciación (Tabla 3).
- Regla explícita, coherente con la Hoja: mejor puntaje (AIC, BIC, RMSE y MAE móviles) entre los modelos que superan al naive y pasan Ljung-Box. Elegido: **B, SARIMA(0,1,1)(0,1,1)₁₂ «airline»**, porque A, con mejor puntaje, deja autocorrelación.

**Brechas**
| Brecha | Impacto | Acción sugerida |
|---|---|---|
| ~~A, B y C empataban en el puntaje (2,0)~~ **Resuelto:** con origen móvil los puntajes son 1, 2 y 3 | — | — |
| B supera al naive en RMSE móvil (7,12 frente a 7,72 GWh, 7,8 % menos), pero el MAE móvil es prácticamente igual (6,64 frente a 6,66) | La ventaja sobre la referencia mínima es moderada | El texto ya lo dice; desarrollarlo en la interpretación propia (qué significa para contratar energía) |
| ~~C pronosticaba mejor en 2023 pese a peor AIC/BIC~~ **Resuelto:** con origen móvil, C es el peor de los comparables (RMSE móvil 8,30) y tampoco pasa Ljung-Box (p = 0,047) | — | — |
| ~~Validación de solo 12 meses~~ **Resuelto en parte:** origen móvil con tres años; sigue siendo una muestra corta, y así lo indica el texto | — | — |
| ~~La fila 3 de la Hoja tiene un `[COMPLETAR]`~~ **Resuelto:** regla ajustada, puntajes y métricas móviles | — | — |

## 4. Diagnóstico de residuos y validación de supuestos (ID 2.2)

**Lo que cumple**
- Diagnóstico completo, como pide la rúbrica: Ljung-Box en los rezagos 12 y 24, con 2 grados de libertad descontados (p = 0,355 y 0,061); normalidad con Jarque-Bera (p = 0,001) y Shapiro-Wilk (p = 0,019); homocedasticidad con ARCH-LM (p = 0,639) y test F (p = 0,246). Hay figura de residuos, histograma, Q-Q y ACF.
- Concluye sobre la validez: válido para pronosticar; los intervalos de 95 % son aproximados, pero su cobertura empírica fue de 94,4 % (36 meses).

**Brechas**
| Brecha | Impacto | Acción sugerida |
|---|---|---|
| ~~La normalidad falla y no se discute la causa~~ **Resuelto:** colas pesadas (curtosis 1,83) concentradas en marzo-junio de 2020; sin esos meses se cumple (Jarque-Bera p = 0,215); cobertura del IC 95 % de 94,4 % | — | En la interpretación propia, decidir si conviene el indicador de abril-junio de 2020 frente a su costo en Ljung-Box |
| ~~Ljung-Box en el rezago 24 (p = 0,061) cerca del umbral, sin matizar~~ **Resuelto:** el texto lo menciona | — | — |
| ~~La fila 4 de la Hoja tiene un `[COMPLETAR]`~~ **Resuelto:** valores-p de Ljung-Box, Jarque-Bera, Shapiro-Wilk, ARCH-LM y F | — | — |
| Falta la interpretación propia | La rúbrica exige interpretar | Reescribir |

## 5. Ortografía y redacción

| Brecha | Dónde | Acción sugerida |
|---|---|---|
| Los 5 textos de interpretación y conclusiones dicen «**Borrador (reescribir con mis palabras)**» | Secciones 1–4 y Conclusiones | Reescribir y quitar la marca |
| El encabezado está en modo instrucción: «El **miércoles** entregue la Hoja…», «Estado de este borrador» | Celda 0 | Reemplazar por un encabezado formal |
| ~~Mezcla de punto y coma decimal~~ **Resuelto:** tablas y textos con coma decimal | — | — |
| Anglicismo «naive» | Varias secciones | Usar «ingenuo estacional» |
| Giros poco académicos o confusos: «La serie en logaritmos y en nivel recibe el veredicto…», «2023 sigue siendo una validación honesta» | Conclusiones y sección 2 | Revisar en la reescritura |

## 6. Formato y entrega

| Requisito (rúbrica) | Estado | Detalle |
|---|---|---|
| Notebook ejecutable (.ipynb) | Cumple | Se ejecuta completo de principio a fin |
| **Extensión 10–15 páginas equivalentes** | **No cumple** | Unas **9,3 páginas** (3.122 palabras, 5 figuras, 32 filas de tabla; sin contar el código). La celda de apoyo controla otro límite (250 palabras, una tabla y hasta 3 figuras por sección), que **contradice** las 10–15 páginas de la rúbrica |
| **Nombre de archivo** `sigla_sXinicialapellido` | **Revisar** | El archivo es `mcdi505_f2rmoncada.ipynb`; la rúbrica pide el formato `mcdi505_s2rmoncada`. El encabezado dice «s2», pero ese nombre ya lo usa otro notebook del repositorio |
| Referencias APA | Cumple | 13 referencias en APA 7 (español), todas citadas en el texto |
| Marcas pendientes | No cumple | 3 `[COMPLETAR]` en la declaración de IA (la Hoja ya está completa) |
| Celda de trabajo | No cumple | «Apoyo para el autor (borrar antes de entregar)» sigue en el notebook |
| Estructura (portada, introducción, criterios, conclusiones, referencias) | Parcial | Falta portada formal (programa, curso, fecha); la introducción es un solo párrafo |
| Entrega dentro del plazo | Sin verificar | |

---

## Plan de acción priorizado

1. **Aclarar con el docente la extensión exigida para la Formativa 2:** 10–15 páginas según la rúbrica, o los límites por sección que usa el notebook. Si son 10–15, faltan unas 2,5 páginas, que pueden salir de las interpretaciones propias y de la discusión de la selección.
2. ~~Completar la Hoja de decisiones~~ **Hecho.** Falta **borrar la celda de apoyo** antes de entregar, después de revisar su verificación de cifras.
3. **Reescribir con palabras propias** las 4 interpretaciones y las conclusiones, quitando la marca «Borrador». Incluir el empate de la selección, la ventaja mínima sobre el naive y las causas de la falta de normalidad.
4. ~~Agregar citas en el texto (APA)~~ **Hecho.**
5. ~~Mostrar los coeficientes y comentar los MA cercanos a −1~~ **Hecho.**
6. **Corregir formato:** encabezado formal, «ingenuo» en vez de «naive» y nombre de archivo (la coma decimal ya está hecha).
7. **Completar la declaración de uso de IA** según lo realmente hecho. Revisar que el uso declarado (borrador de código y textos) sea compatible con la norma de la evaluación, que permite la IA solo para organizar ideas o mejorar la redacción.
