# Revisión de cumplimiento de la rúbrica — Sumativa 1 (MCDI505)

**Archivo revisado:** `mcdi505_s1rmoncada.ipynb`
**Alcance de la revisión:** ejecución completa, revisión ortográfica y contraste criterio por criterio con la rúbrica del PDF.

## 1. Resultado de la ejecución (Restart & Run All)

| Verificación | Resultado |
|---|---|
| Ejecución limpia de las 17 celdas de código, en un proceso nuevo y desde el archivo entregado | Sin errores |
| Rutas relativas, semilla fija, sin modificar el CSV original | Cumple |
| Conjunto de prueba (2024) excluido en la carga | Cumple |

**Limitación importante.** El entorno donde trabajé no permite instalar `statsmodels` (el acceso a PyPI está bloqueado). La ejecución se hizo con implementaciones equivalentes de `seasonal_decompose`, `acf`, `pacf`, `plot_acf` y `plot_pacf`, y no con un kernel de Jupyter. Las salidas incrustadas son válidas para las cifras, pero **debes repetir *Restart & Run All* en tu propio entorno** antes de entregar. Los gráficos de ACF/PACF pueden verse distintos en estilo (por ejemplo, `statsmodels` usa bandas de Bartlett en la ACF).

## 2. Revisión ortográfica y de redacción

No había diccionario de español disponible, así que la revisión fue parcial: comprobaciones mecánicas (palabras repetidas, espacios, signos), lectura de las ~180 palabras técnicas poco frecuentes y relectura del texto (~4.600 palabras). No se encontraron errores ortográficos.

Correcciones aplicadas: "reexaminarse" → "volver a examinarse" y "significancia" → "significación".

**Recomendación:** pasar el texto final por el corrector de Word o de otra herramienta antes de entregar, porque esta revisión no equivale a un corrector con diccionario completo.

## 3. Cumplimiento criterio por criterio

| Criterio | Estado | Observaciones |
|---|---|---|
| 1. Exploración y visualización (9 pts) | Cumple | Gráficos con título, ejes y leyenda; describe tendencia, estacionalidad, ciclo, cambios de nivel y varianza; contextualiza el dataset. |
| 2. Descomposición (9 pts) | **Cumple con un punto débil** | Aplica el esquema multiplicativo, pero la evidencia para elegirlo es mixta (ver brecha B2). |
| 3. ACF y PACF (9 pts) | Cumple | Cálculo, tabla de rezagos significativos e interpretación de persistencia, estacionalidad y dependencia. |
| 4. Interpretación integrada (9 pts) | Cumple | Tabla de evidencia cruzada, conclusión técnica e implicancias; código comentado; notebook ejecutable. |
| 5. Ortografía y redacción (9 pts) | Cumple (revisión parcial) | Ver sección 2. |
| 6. Formato y entrega (9 pts) | **Riesgo** | Extensión sin verificar, archivo y plazo a confirmar (ver brechas B1, B3, B4). |

## 4. Brechas y riesgos detectados

### B1 — Extensión de 10 a 15 páginas equivalentes (riesgo alto)
No pude medir las páginas. El notebook tiene unas 4.600 palabras de texto (≈9 a 10 páginas), 9 figuras (varias con varios paneles), tablas y 397 líneas de código con sus salidas. Si se exporta con el código visible, **podría superar las 15 páginas**.
**Qué hacer:** exportar a HTML o PDF y contar. Si excede, acortar las salidas impresas o resumir la sección 6. Si se cuenta sin el código, podría quedar cerca del mínimo.

### B2 — Elección del esquema aditivo o multiplicativo (riesgo medio)
La rúbrica pide "determinar el esquema a partir de las características observadas". Los datos dan señales mixtas: la amplitud relativa estable (~30 %) favorece el multiplicativo, pero la elasticidad de la dispersión (0,31) y la dispersión residual casi idéntica en ambos esquemas no lo respaldan con fuerza. El notebook lo reconoce, pero un evaluador podría considerar la decisión poco concluyente.
**Qué hacer (opcional):** agregar una comparación adicional, como la desviación móvil de la serie en logaritmos frente a la de la serie original, y declarar con más firmeza el criterio de desempate.

### B3 — Nombre de archivo (verificar)
El formato exigido es `mcdi505_s1inicialapellido`. El archivo se llama `mcdi505_s1rmoncada`. Confirma que tu inicial y apellido coinciden con el registro del curso.

### B4 — Plazo de entrega
La entrega vence el domingo de la Semana 1 a las 23:59. No puedo verificarlo; queda de tu parte.

### B5 — Declaración de uso de IA
El PDF no permite IA generativa para producir respuestas completas, y exige declarar su uso "en el material de apoyo correspondiente". Me indicaste que en tu caso está permitido. El notebook incluye la declaración en la sección 9, pero **confirma que refleja lo permitido y lo que realmente hiciste**, y decide si también debe figurar en el formulario de entrega de Canvas.

### B6 — Citas y referencias APA (cerrado)
Se detectó que la referencia de Seabold y Perktold (2010) no estaba citada en el texto; ya se agregó la cita en la sección 2. Todas las referencias listadas están ahora citadas.

### B7 — Supuestos del análisis que conviene conocer
- El contrafactual del COVID supone crecimiento nulo respecto de 2018-2019; es conservador.
- El ciclo se declara no identificable con nueve años de datos; un evaluador podría esperar que se discuta más.
- La explicación del mecanismo de la doble estacionalidad (turismo y calefacción) es una hipótesis coherente con el contexto, no un hallazgo de los datos.
- La descomposición clásica pierde 6 observaciones en cada extremo y es sensible al shock; STL se menciona pero no se aplica.

## 5. Lista de verificación final

- [ ] Ejecutar *Restart & Run All* en tu entorno con `statsmodels` real y confirmar que las cifras del texto coinciden con las salidas.
- [ ] Exportar a HTML/PDF y contar las páginas (objetivo: 10 a 15).
- [ ] Pasar el texto por un corrector ortográfico con diccionario completo.
- [ ] Confirmar el nombre del archivo y la declaración de uso de IA.
- [ ] Entregar antes del domingo a las 23:59.
