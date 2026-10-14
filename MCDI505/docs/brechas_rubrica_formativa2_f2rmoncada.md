# Validación — `mcdi505_s2rmoncada.ipynb` (antes `mcdi505_f2rmoncada.ipynb`) frente a la Rúbrica Formativa 2 (f2_s2)

- **Fecha de revisión:** 11 de octubre de 2026, sexta revisión (anteriores: 9 y 11 de octubre)
- **Versión revisada:** commit `78937ef` más la sección «5. Discusión» reescrita por el autor (sin commit). Sin marcas `[AUTOR]`, `[COMPLETAR]` ni de propuesta
- **Ejecución de control:** «Reiniciar kernel y ejecutar todo» (kernel nuevo): **5/5 celdas de código, ejecutadas en orden (1 a 5) y sin errores**
- **Rúbrica:** `Rúbrica_formativa_f2_s2`, 6 criterios de 9 puntos (total 54)
- **Alcance:** validación completa de resultados tras las correcciones del autor; concordancia de todos los textos y de la Hoja de decisiones con la ejecución; extensión y formato. Es una estimación de cumplimiento, no una nota.

## Resumen

| # | Criterio | Nivel probable | Puntaje probable | Estado |
|---|---|---|---|---|
| 1 | Estacionariedad y transformaciones (ID 2.2) | Excelente | 9 | **Resuelto.** Error de atribución corregido, elasticidad explicada y KPSS truncado aclarado |
| 2 | Identificación y estimación (ID 2.1) | Excelente | 9 | **Resuelto.** 7 candidatos que cubren AR, MA, ARMA, ARIMA y SARIMA (incluido un AR estacional como contraste), nombres precisos y precisiones del texto corregidas |
| 3 | Selección y comparación (ID 2.1) | Excelente | 9 | **Resuelto.** Rezago 24 de Ljung-Box, «RMSE móvil de 25,90 GWh» y una frase sobre E y F |
| 4 | Diagnóstico de residuos (ID 2.2) | Excelente | 9 | **Resuelto.** Tipeo corregido, «no se rechaza que sean ruido blanco» con el rezago 24 cerca del umbral, e «intervalo de predicción» con prueba binomial |
| 5 | Ortografía y redacción | Excelente | 9 | **Resuelto.** Declaración de IA corregida, «Limitaciones:» en las conclusiones y celda 4 |
| 6 | Formato y entrega | Bueno | 6 | Discusión reescrita por el autor. Pendientes: extensión de **~9,9 páginas** (falta ~0,1), párrafo de instrucciones en el encabezado y nombre de archivo |
| | **Total estimado** | | **51 / 54** (54 si se resuelven los pendientes del criterio 6) | |

**Resultado de la validación (sexta revisión):** todas las cifras de los textos del autor, incluida la Discusión reescrita, y de la Hoja de decisiones tienen respaldo en las salidas de la ejecución (comprobación automática con el mismo redondeo). No quedan marcas pendientes. Lo único abierto es de formato (criterio 6).

### Revisión de la Discusión reescrita por el autor (celda 17, 326 palabras)
| Afirmación | Resultado ejecutado | Estado |
|---|---|---|
| A: menor RMSE móvil (5,78 GWh), autocorrelación (Ljung-Box p = 0,019) | 5,782; p = 0,019 en el rezago 24 | ✅ ⚠️ opcional: indicar «en el rezago 24» |
| E y F: MAE móvil 6,03 y 6,10 frente a 6,64 de B; p = 0,031 y 0,030 | 6,033; 6,096; 6,644; 0,031; 0,030 | ✅ |
| C y G no mejoran al ingenuo (RMSE móvil 8,30 y 8,51 GWh); p = 0,047 y 0,003 | 8,299; 8,505 frente a 7,721; 0,047; 0,003 | ✅ |
| ARIMA sin estacionalidad: RMSE móvil 25,90 GWh | 25,900 | ✅ |
| «B es el único modelo con residuos sin autocorrelación y un error menor que la referencia» | B es el único elegible (Tabla 3) | ✅ |
| Indicador abril-junio 2020: Jarque-Bera 0,226 frente a 0,001; Ljung-Box 0,039; cobertura 94,4 % (binomial p = 0,701) | Iguales (sección 4) | ✅ |
| Error promedio de B 6,64 GWh = 6,2 % de 107,65 GWh; RMSE 7,8 % menor que el ingenuo | Iguales (sección 3) | ✅ |
| «El efecto de COVID-19 fue de −6,0 %» | −5,987 % en el modelo B | ✅ ⚠️ precisar «en el modelo B» |
| Redacción | — | ⚠️ falta un espacio en «estacionalidad anual.En consecuencia»; sobra una línea en blanco antes de «Implicancias» |

---

## 1. Correcciones aplicadas en esta revisión

### Criterio 1: Estacionariedad y transformaciones
| Brecha | Corrección | Dónde |
|---|---|---|
| ❌ «La **serie original** no fue concluyente (ADF p = 0,391…)»: esas cifras eran de la serie en logaritmos | «La **serie en logaritmos sin diferenciar** no fue concluyente…» | Celdas 7 y 18 (punto 1) |
| ⚠️ Elasticidad 0,25 sin contexto | «Sin 2020-2021, la elasticidad… es 0,25, es decir, la variabilidad crece poco con el nivel» | Celda 7 |
| ⚠️ KPSS p = 0,100 truncado sin aclarar | Nota impresa bajo la Tabla 1 y una frase en la interpretación | Celdas 6 y 7 |
| ⚠️ Redacción | Título «Interpretación de la estacionariedad»; «por sí solo no permite decidir»; «se utiliza **el** λ» y punto final | Celdas 5 y 7 |

### Criterio 2: Identificación y estimación
| Brecha | Corrección | Dónde |
|---|---|---|
| Sin candidatos AR o MA puros ni AR estacional como contraste | Se agregan **E. AR(1)**, **F. MA(1)** y **G. SARIMA(0,1,1)(1,1,0)₁₂** (AR estacional). Los 7 candidatos cubren las cinco familias que pide la rúbrica | Celda 9 (código), Tabla 2 y Tabla 3 |
| C se llamaba «ARMA(1,1) con la misma diferenciación» | «ARMA(1,1) sobre la serie diferenciada»; igual para E y F | Celda 9 |
| ⚠️ «rezago significativo en [12]… [12, 24]» (notación de Python) | «La ACF mostró un único rezago significativo, el 12, y la PACF, los rezagos 12 y 24» | Celda 10 |
| ⚠️ «reducción estimada de -4,2 %» (doble negación) | «reducción estimada de 4,2 %… (6,0 % en el modelo B)» | Celda 10 |
| ⚠️ «algunos modelos» en la frontera de invertibilidad | «los modelos A, B y C» | Celda 10 |
| «cuatro modelos» en el texto, las conclusiones y la Hoja | «siete modelos de las familias AR, MA, ARMA, ARIMA y SARIMA» | Celdas 1, 10 y 18 |
| El PACF = −0,32 del rezago 12 solo se veía en la Figura 3 | La salida de la sección 2 imprime ACF y PACF en el rezago 12 | Celda 9 |

**Efecto de los nuevos candidatos (verificado):** E, F y G se estiman bien: convergen, y F y G están lejos de la frontera de invertibilidad (\|raíz MA\| de 14,7 y 5,4; E no tiene término MA). Sin embargo, **ninguno es elegible**: fallan Ljung-Box en el rezago 24 (E p = 0,031; F p = 0,030; G p = 0,003). La selección **no cambia**: B sigue siendo el único elegible, con las mismas cifras (RMSE móvil 7,12 frente a 7,72 GWh del naive). Puntajes: A 1,0; B 2,5; E y F 4,25; C y G 4,5.

### Criterio 4: Diagnóstico de residuos (tercera revisión)
| Brecha | Corrección | Dónde |
|---|---|---|
| ⚠️ «test F entre mitades p = 0246» | «el test F entre mitades p = 0,246» | Celda 16 |
| ⚠️ «los residuos pueden considerarse ruido blanco» (afirma la hipótesis nula) | «no se rechaza que los residuos sean ruido blanco, aunque el valor del rezago 24 está cerca del umbral» (p = 0,061) | Celda 16 |
| ⚠️ «intervalo de confianza del 95 %… (p = 0,701)» | «intervalo de **predicción** del 95 %… en el origen móvil (prueba binomial, p = 0,701)» | Celda 16 |
| Término distinto en la tabla y la Hoja («IC 95 %») | «Cobertura del intervalo de predicción del 95 %» en la Tabla 4 y en la fila 4 de la Hoja | Celdas 15 y 1 |

### Criterios 3, 5 y 6 (cuarta revisión)
| Brecha | Corrección | Dónde |
|---|---|---|
| Criterio 3: Ljung-Box p = 0,019 sin indicar el rezago | «(Ljung-Box p = 0,019 en el rezago 24)» | Celda 13 |
| Criterio 3: «alcanzó 25,90 GWh» | «alcanzó un RMSE móvil de 25,90 GWh» | Celda 13 |
| Criterio 3: nuevos candidatos sin mencionar | «Los modelos E y F también superaron al naive en RMSE móvil (7,16 y 7,19 GWh), pero, al igual que C y G, dejaron autocorrelación en el rezago 24…» | Celda 13 |
| Criterio 5: «Trabajo solo con consumo_gwh, y el periodo estacional de 12 meses» | «Se trabaja solo con la variable consumo_gwh y el periodo estacional es de 12 meses» (impersonal, como el resto); «nov-2017» → «noviembre de 2017» | Celda 4 |
| Criterio 6: extensión de unas 9,0 páginas | Propuesta de sección **«5. Discusión»** (~470 palabras), antes de las conclusiones: candidatos no elegibles, indicador abril-junio de 2020 e implicancias para la contratación de energía. Todas sus cifras están en las salidas; se agregó la impresión del consumo medio 2021-2023 (107,65 GWh; MAE móvil de B = 6,2 % de ese nivel) | Celdas 12 y 17 |

### Otras correcciones de concordancia
| Hallazgo | Corrección |
|---|---|
| Las conclusiones (punto 5) citan Jarque-Bera p = 0,226 y Ljung-Box p = 0,039 del indicador abril-junio de 2020, pero la celda que los mostraba fue eliminada | La sección 4 imprime ahora esa sensibilidad: «Jarque-Bera p = 0,226 y Ljung-Box (rezago 24) p = 0,039» |
| Hoja, filas 2 y 3 | Actualizadas con los 7 candidatos, el rango del efecto COVID-19 (−4,2 % a −6,7 %) y que C, E, F y G no pasan Ljung-Box (p de 0,003 a 0,047) |

---

## 2. Validación de concordancia: textos `[AUTOR]` y Hoja frente a la ejecución

Leyenda: ✅ concuerda · ⚠️ pendiente de redacción o precisión (no afecta las cifras) · 🔧 corregido en esta revisión

| Celda | Contenido | Cifras verificadas | Estado |
|---|---|---|---|
| 1 | Hoja de decisiones | 42 cifras: d = 1 y D = 1; ADF y KPSS; IC de λ (−1,45 a 1,49); elasticidad 0,25; banda ±0,22; ACF −0,30; efecto COVID-19 (−4,2 % a −6,7 %); raíces MA 1,002–1,013; RMSE y MAE móviles; Ljung-Box, Jarque-Bera, ARCH-LM y F; cobertura 94,4 % | ✅ 🔧 (filas 2 y 3) |
| 4 | Contexto del conjunto de datos | 3 imputados; atípico de noviembre de 2017; `covid` de marzo de 2020 a diciembre de 2021 (22 meses); 96/12 meses; origen móvil 2021-2023 | ✅ 🔧 |
| 5 | Método, sección 1 | — | ✅ 🔧 |
| 7 | Interpretación, sección 1 | λ, IC, elasticidad, ADF y KPSS antes y después, ACF(12), 13 observaciones; la variabilidad aumenta en el COVID-19 (desviación 0,039 fuera frente a 0,065 dentro) | ✅ 🔧 |
| 8 | Método, sección 2 | — | ✅ |
| 10 | Interpretación, sección 2 | Banda ±0,22; ACF −0,30; PACF −0,32; p = q = P = 0 y Q = 1; efecto 4,2 % (A) y 6,0 % (B); raíces 1,002–1,013; −1,00 y Δ < 0,03 | ✅ 🔧 |
| 11 | Método, sección 3 | — | ✅ |
| 13 | Interpretación, sección 3 | A con el mejor puntaje (5,78 GWh); Ljung-Box p = 0,019 (rezago 24); E y F 7,16 y 7,19 GWh; B: AIC −300,9, BIC −291,2, RMSE móvil 7,12; −7,8 % frente al naive (7,72); MAE 6,64 frente a 6,66; ARIMA 25,90 | ✅ 🔧 |
| 14 | Método, sección 4 | — | ✅ |
| 16 | Interpretación, sección 4 | Ljung-Box 0,355 y 0,061; Jarque-Bera 0,001; Shapiro-Wilk 0,019; sin mar-jun 2020: 0,215 y 0,111; ARCH-LM 0,639; F 0,246; cobertura 94,4 % (binomial p = 0,701) | ✅ 🔧 |
| 17 | **5. Discusión** (reescrita por el autor) | 22 cifras, todas respaldadas (ver la tabla de revisión arriba) | ✅ ⚠️ espacio en «anual.En» |
| 19 | Conclusiones (antes celda 18) | Puntos 1 a 5, incluidos 0,226 y 0,039 | ✅ ⚠️ «Limitaciones, la validación…» → «Limitaciones: la validación…» |

---

## 3. Brechas abiertas

### Criterio 5: Ortografía y redacción
- ~~Ortografía de la declaración de IA~~ **Resuelto** (quinta revisión): «utilizó», «análisis», «reescribieron», «Ejecuté», «sección por sección», «interpreté», «verifiqué», «Además», «rúbrica» y concordancia «Las interpretaciones fueron…».
- ~~«Limitaciones, la validación…»~~ **Resuelto:** «Limitaciones: la validación…» (celda 19).
- Opcional: usar un solo término, «ingenuo estacional» o «naive estacional» (hoy aparecen los dos).

### Criterio 6: Formato y entrega
| Requisito | Estado | Detalle / acción |
|---|---|---|
| Notebook ejecutable | ✅ Cumple | 5/5 celdas en orden, sin errores, desde un kernel nuevo |
| Textos duplicados (borradores generados) | ✅ Resuelto por el autor | Se eliminaron las 5 celdas de borrador |
| **Extensión 10–15 páginas** | **No cumple por poco** | Unas **9,9 páginas** (3.349 palabras, 5 figuras, 36 filas de tabla; sin contar código). La Discusión reescrita pasó de ~470 a 326 palabras. Faltan **~50 palabras** de contenido propio; por ejemplo, desarrollar en la Discusión cómo usar el intervalo de predicción como margen de compra, o por qué se prefiere validez de residuos sobre precisión |
| Marcas `[AUTOR]` | ✅ Resuelto | El autor las quitó todas |
| Encabezado (celda 0) | Parcial | El autor agregó programa, curso, archivo y fecha. Queda el párrafo de instrucciones «Este es el único notebook… El miércoles entregue…»; conviene reemplazarlo por una o dos frases de presentación del informe (así no se pierde extensión) |
| Ejemplo ilustrativo bajo la Hoja | ✅ Resuelto | El autor lo eliminó |
| Nombre de archivo | ✅ Resuelto | Renombrado a `mcdi505_s2rmoncada.ipynb` (formato `sigla_sXinicialapellido`); el encabezado del notebook ya usa ese nombre. Entrega en `MCDI505/entregas/mcdi505_s2rmoncada.zip` (notebook + CSV depurado), validada al ejecutarse desde una carpeta vacía |
| Declaración de IA y coherencia | ✅ Cumple | Ortografía corregida; la Discusión está reescrita por el autor, así que la declaración es coherente |
| Propuesta «5. Discusión» | ✅ Resuelto por el autor | Reescrita con palabras propias, sin recuadro de propuesta; todas sus cifras concuerdan |
| Referencias APA | ✅ Cumple | 13 referencias, todas citadas |

---

## 4. Plan de acción para la entrega

1. ~~Reescribir la propuesta «5. Discusión»~~ **Hecho por el autor.** Corregir «anual.En» y, si se quiere, precisar «rezago 24» y «en el modelo B».
2. ~~Ortografía de la declaración de IA~~ **Hecho.**
3. ~~Agregar ~1 página de contenido propio~~ **Propuesta agregada** (ver punto 1). ~~«Limitaciones:»~~ **Hecho.**
4. **Formato y extensión:** reemplazar el párrafo de instrucciones del encabezado por una presentación breve, agregar ~50 palabras de contenido propio para llegar a 10 páginas y confirmar el nombre de archivo.
5. **Reiniciar kernel y ejecutar todo**, guardar y verificar que no haya errores.

---

## Historial de brechas resueltas

- **9 de octubre:** Tabla 2 con coeficientes e invertibilidad; referencias APA 7 citadas en el texto; coma decimal; transformación cuantificada (IC de λ y elasticidad); Hoja de decisiones completa; selección sin empate (origen móvil + Ljung-Box); análisis de la normalidad y cobertura de los intervalos.
- **11 de octubre (primera revisión):** el autor redactó las 10 celdas `[AUTOR]`; validación de concordancia: todas las cifras correctas salvo la atribución «serie original».
- **11 de octubre (segunda revisión):** criterios 1 y 2 corregidos (atribución, elasticidad, KPSS truncado, 7 candidatos, nombres y precisiones); sensibilidad y PACF del rezago 12 visibles en las salidas; el autor eliminó los borradores duplicados; ejecución limpia desde un kernel nuevo.

- **11 de octubre (tercera revisión):** criterio 4 corregido (tipeo 0,246, «no se rechaza», intervalo de predicción con prueba binomial y término unificado en la Tabla 4 y la Hoja); ejecución limpia desde un kernel nuevo, con todas las cifras respaldadas.
- **11 de octubre (cuarta revisión):** criterio 3 (rezago 24, RMSE móvil del ARIMA, mención de E y F) y celda 4 (criterio 5) corregidos; propuesta de sección «5. Discusión» con todas sus cifras respaldadas; extensión estimada de ~10,1 páginas.
- **11 de octubre (quinta revisión):** ortografía de la declaración de IA y «Limitaciones:» corregidos; el autor quitó las marcas `[AUTOR]` y el ejemplo de la Hoja; ejecución limpia (5/5, sin errores), ~10,1 páginas.
- **11 de octubre (18:18–18:21):** un guardado desde VS Code sobrescribió el archivo con una versión anterior y se perdieron la sección «5. Discusión» y cinco correcciones (celda 4, celda 13, consumo medio impreso, «Limitaciones:» y ortografía de la declaración). Se repusieron respetando los cambios propios del autor (encabezado de la celda 0 y tercera fila de la declaración, cuya ortografía también se corrigió). La Discusión quedó en la **celda 17**, destacada en un recuadro rojo. Ejecución limpia (5/5), ~10,3 páginas.

- **11 de octubre (sexta revisión):** el autor reescribió la Discusión (326 palabras) y quitó el recuadro; ejecución limpia (5/5) y todas las cifras respaldadas; extensión ~9,9 páginas.
- **14 de octubre:** notebook renombrado a `mcdi505_s2rmoncada.ipynb` (encabezado actualizado); ejecución limpia (5/5, 5 figuras); ZIP de entrega regenerado y validado desde una carpeta vacía.
- **14 de octubre (corrección de lectura del rezago 24):** se corrigió la justificación del modelo G en la §2, en la fila 2 de la Hoja y en su nombre («contraste» en vez de «PACF en el rezago 24»). La PACF significativa en el rezago 24, junto con la ACF que se corta en el 12, es el patrón de un MA estacional y no de un AR estacional; G se mantiene como contraste de esa alternativa. Esa lectura incorrecta había sido introducida por el asistente en la segunda revisión del 11 de octubre. Se corrigió también la guía de lectura. ZIP de entrega regenerado.

- **14 de octubre (revisión con la tabla de errores frecuentes de la IA):** de 8 puntos, 6 ya concordaban. Se corrigieron los otros dos: (1) **criterio de varianza**: la Tabla 1 agrega d = 2, D = 1 y d = 1, D = 2; ambas pasan ADF (p < 0,001), pero su desviación estándar sube de 0,047 a 0,065 y 0,079, lo que confirma que (1,1) no está sobrediferenciada (nota impresa, frase en la §1 y fila 1 de la Hoja); (2) **corrección de sesgo** al retransformar: los pronósticos puntuales usan exp(μ + σ²ₕ/2) (Hyndman y Athanasopoulos, 2021, sección 5.6); los intervalos, no. La selección no cambia (B, único elegible). Cifras actualizadas en la Hoja, §3, Discusión, Conclusiones y guía: RMSE móvil de B 7,11 (antes 7,12), mejora de 7,9 % sobre el naive, MAE móvil 6,62; A 5,87; E 7,05; F 7,12; C 8,27; G 8,44; D 31,95. Puntajes: A 1,00; B 2,75; E 4,00; F 4,25; C y G 4,50. ZIP regenerado.
