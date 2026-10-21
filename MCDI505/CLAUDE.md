# MCDI505 · Análisis de Series de Tiempo — convenciones del proyecto

Proyecto de Roberto Moncada (Magíster en Ciencia de Datos, UNAB Online). Caso: consumo eléctrico mensual del segmento comercial de DEL. Todo en español.

## Entorno
- Ejecutar notebooks con `C:/Magister_ciencia_datos/.venv/Scripts/jupyter.exe` y Python con `C:/Magister_ciencia_datos/.venv/Scripts/python.exe` (`jupyter` no está en el PATH).
- Ejecución completa: `jupyter nbconvert --to notebook --execute --inplace <notebook>`. Para validar sin tocar el archivo del autor, ejecutar una copia con `--output-dir` en el scratchpad.
- El autor suele tener el notebook abierto en VS Code: si se modifica en disco, recordarle que recargue sin guardar el buffer abierto.

## Estructura
- Notebooks: `notebooks/mcdi505_s{n}rmoncada.ipynb` (S1 usa `consumo_electrico_litoral.csv`; S2 y S3 `consumo_electrico_litoral_depurado.csv`; S4 `consumo_electrico_litoral_depurado_s4.csv`).
- Material del profesor (instrucciones, rúbricas, plantillas, guías): `notebooks/S{n}eje_profe/`.
- Informes de brechas: `docs/brechas_s{n}rmoncada.md` (S2: `docs/validacion_sumativa2_s2rmoncada.md`). Cada revisión nueva se agrega arriba, numerada, sin borrar las anteriores.
- Entregas: `entregas/mcdi505_s{n}rmoncada.zip` (notebook + CSV; en la S4 también el PDF). Validar siempre descomprimiendo en una carpeta vacía y ejecutando con kernel nuevo.

## Decisiones metodológicas vigentes
- Modelo final: SARIMA(0,1,1)(0,1,1)12 sobre el logaritmo, con la indicadora `covid` (modelo B). Sin ARFIMA ni GARCH (S3).
- Pronósticos puntuales con **media corregida por sesgo** exp(μ + σ²/2) en todas las semanas (feedback del profesor); intervalos y cuantiles con exp() sin corrección.
- Ljung-Box con `model_df` = número de parámetros AR/MA. ADF y KPSS con estadístico y valor crítico al 5 % (feedback del profesor).
- Volumen a contratar (S4): cuantil q* = c_u / (c_u + c_o); con c_u = 3·c_o, cuantil 75 %.

## Política de IA del curso (obligatoria)
- La IA **no redacta** interpretaciones, conclusiones ni el informe: solo código, organización de ideas, verificación de cifras y correcciones de redacción u ortografía.
- Las celdas del autor no se modifican sin pedido explícito. Las propuestas van en celdas `[BORRADOR]` (recuadro rojo) con tabla «Dice / Debe decir / Por qué», verificando que cada «Dice» sea texto literal del autor.
- Las correcciones mecánicas de ortografía y formato pueden aplicarse directamente solo si el autor lo pide.
- Toda cifra del texto debe aparecer en una salida del notebook o citar su fuente (Semana 2 o 3).

## Validaciones
- Contra el PDF de instrucciones/rúbrica de la semana: instrucciones específicas, aspectos formales (extensión, una tabla y ≤ 3 figuras por sección, ≤ 250 palabras de interpretación en S2 y S3, nombre de archivo, APA) y nivel probable por criterio.
- Revisar también la concordancia texto–resultados y la declaración de uso de IA.

## Git
- Al terminar cada entregable: commit (mensaje en español, prefijo `MCDI505:`) y push a `origin main` sin preguntar.
