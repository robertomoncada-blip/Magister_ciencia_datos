# Brechas por corregir: `mcdi505_s3rmoncada.ipynb` (Semana 3, ARFIMA / GARCH)

- **Fecha de revisión:** 14 de octubre de 2026 (miércoles: hoy se entrega la Hoja de decisiones, Formativa 3)
- **Versión revisada:** archivo sin commit, con todas las salidas de la ejecución guardadas
- **Ejecución de control:** «Reiniciar kernel y ejecutar todo» con kernel nuevo. **Las 8 celdas de código corren en orden y sin errores**
- **Referencias de control:** notebook de la S2 (`mcdi505_s2rmoncada.ipynb`), plantilla del profesor (`S3eje_profe/mcdi505_s3_plantilla.ipynb`) y guía de compañía de la Semana 3 (`S3eje_profe/MCDI505_S3_guia_de_compania.pdf`), incluida su tabla «Errores frecuentes de la IA en esta unidad»
- **Fuera de alcance:** el PDF de instrucciones de la Formativa y la Sumativa 3, que no está en el repositorio. Según la guía es el único documento evaluativo y prevalece sobre todo lo demás; revisar contra él la extensión, el formato y el nombre del archivo.

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
