# Esquema y banco de evidencia: Informe ejecutivo, Sumativa 4

> Material para **organizar ideas**, como permiten las instrucciones de la Sumativa 4. No contiene redacción del informe: la prosa la escribe el autor. Declarar este apoyo en la sección «Declaración de uso de IA» del informe.

## 0. Bloqueos antes de escribir

| # | Pendiente | Por qué bloquea |
|---|---|---|
| 1 | ~~Plantilla oficial de la S4~~ ✅ Resuelto: `notebooks/mcdi505_s4rmoncada.ipynb`, construido sobre `mcdi505_s4_plantilla.ipynb` con `consumo_electrico_litoral_depurado_s4.csv` | Las cifras de 2024 de abajo salen de ese notebook (cifras finales) |
| 2 | ~~Sumativa 3 cerrada~~ ✅ Resuelto: S3 final con M1-M3 aplicados y media corregida por sesgo (commit `f20de26`) | Las cifras de abajo ya son las finales de la S3 |
| 3 | Retroalimentación del borrador de la Formativa 4 | Las instrucciones piden incorporarla |

## 1. Mapa rúbrica → secciones (5 a 7 páginas)

| Sección del informe | Criterio | Extensión orientativa | Debe contener |
|---|---|---|---|
| Portada o encabezado | 5 | ¼ pág. | Título, autor, curso, fecha; archivo `mcdi505_s4rmoncada` |
| 1. Síntesis: problema, datos, metodología y solución | 1 (ID 4.1) | 1½ pág. | Problema de DEL (para qué sirve el pronóstico mensual); datos (120 meses, depurados, covid); flujo metodológico S1→S4; solución en una frase; **1-2 figuras** |
| 2. Sustento técnico del modelo | 2 (ID 3.2) | 2 pág. | Evidencia de las semanas 2 a 4: dependencia temporal, volatilidad, métricas 2023 y 2024; por qué los modelos avanzados no aportan, con cifras; **1 tabla resumen + 1-2 figuras** |
| 3. Conclusiones y recomendaciones | 3 (ID 4.1) | 1½ pág. | Recomendaciones **accionables** para la Gerencia, cada una ligada a una cifra; limitaciones y alcances |
| Referencias (APA) | 5 | ½ pág. | Solo las citadas |
| Declaración de uso de IA | — | ¼ pág. | Herramienta, partes y verificación |
| Anexo | 5 | — | Notebook de la plantilla S4 **ejecutado** (no se califica, respalda las cifras) |

Reglas de formato: PDF o DOCX; **sin código** en el informe; figuras numeradas; tablas reformateadas (no capturas de pandas); interpretación en prosa.

## 2. Banco de evidencia (cifras verificadas en las ejecuciones)

### Semana 2: modelo clásico (`mcdi505_s2rmoncada.ipynb`)
| Tema | Cifra |
|---|---|
| Transformación | λ Box-Cox = 0,00 (IC 95 %: −1,45 a 1,49) → logaritmo |
| Estacionariedad | log sin diferenciar: ADF p = 0,391; KPSS p = 0,100; ACF(12) = 0,62 → d = 1 y D = 1: ADF p < 0,001; ACF(12) = −0,30 |
| Sobrediferenciación | desv. est.: 0,047 (d = 1, D = 1); 0,065 (d = 2); 0,079 (D = 2) |
| Candidatos | 7 (AR, MA, ARMA, ARIMA, SARIMA), todos con covid |
| Modelo elegido | **B: SARIMA(0,1,1)(0,1,1)₁₂ + covid**, en log. AIC = −300,9; BIC = −291,2 |
| Efecto COVID-19 | −6,0 % sobre el nivel esperado (p < 0,001) |
| Origen móvil 2021-2023 | RMSE 7,11 frente a 7,72 GWh del naive (−7,9 %); MAE 6,62 frente a 6,66 |
| Validación 2023 | RMSE 6,85 frente a 7,26; MAE 6,40 frente a 6,53 GWh (con corrección de sesgo) |
| Nivel de referencia | Consumo medio mensual 2021-2023 = 107,65 GWh (MAE ≈ 6,2 %) |
| Residuos | Ljung-Box p = 0,355 (12) y 0,061 (24); Jarque-Bera p = 0,001 (0,215 sin mar-jun 2020); ARCH-LM p = 0,639 |
| Intervalos | Cobertura del 95 % en origen móvil = 94,4 % (binomial p = 0,701) |
| Alerta | MA estacional = −0,981 (frontera de invertibilidad) |

### Semana 3: modelos avanzados (`mcdi505_s3rmoncada.ipynb`)
| Tema | Cifra | Nota |
|---|---|---|
| Memoria larga: Hurst R/S | H = 0,652 → d = 0,152 | |
| Sesgo del R/S (n = 83) | Ruido blanco: H medio 0,612; IC 95 % [0,392; 0,823]; 37 % supera 0,652 | Argumento central del «no» |
| ACF de residuos | Solo el rezago 24 (−0,22) toca la banda ±0,215 | |
| Ljung-Box de residuos | 0,355 / 0,061 / 0,076 (12/24/36), con `model_df=2` | Aplicado en la S3 |
| Efecto ARFIMA | −0,24 GWh medio; ΔRMSE 2023 = +0,21 GWh (empeora) | |
| Volatilidad | Ljung-Box residuos² p = 0,485; ARCH-LM p = 0,639 | |
| GARCH(1,1) | ω = 0,457; α = 0,066; β = 0,442; α + β = 0,509 | |
| Residuos estandarizados | Ljung-Box z² p = 0,654; ARCH-LM p = 0,832 | |
| Bandas GARCH frente a SARIMA | Cobertura 12/12 en ambos; ancho 29,3 frente a 29,4 GWh | |
| Sesgo 2023 | 12/12 errores positivos; +6,40 GWh (5,6 %), con media corregida | Feedback aplicado en la S3 |
| Decisión | Se mantiene B; ARFIMA y GARCH no aportan | |

### Semana 4: prueba 2024 (`notebooks/mcdi505_s4rmoncada.ipynb`, plantilla oficial)
| Métrica | Modelo B (reestimado 2015-2023) | Naive estacional |
|---|---|---|
| RMSE 2024 (GWh), media corregida por sesgo como en S2 y S3 | **4,87** (4,96 sin corrección) | 8,19 |
| MAE 2024 (GWh) | **4,00** (4,07) | 6,67 |
| MASE 2024 | **0,614** (0,626) | 1,024 |
| Cobertura IC 95 % (meses dentro / 12) | 12/12; ancho medio 29,7 GWh | n. a. |
| ¿Persiste el sesgo de nivel de 2023? | Se reduce de +6,40 a **+2,89 GWh** (2,4 % del consumo medio de 2024); 9/12 errores positivos | — |
| Modelo reestimado | AIC −350,3; covid −6,6 %; ma.S.L12 = −0,994 (más cerca de la frontera); Ljung-Box p = 0,541 / 0,383; ARCH-LM p = 0,450 | — |

## 3. Preguntas guía para redactar (respuestas del autor)

**Criterio 1, síntesis**
- ¿Qué decisión de la Gerencia depende del pronóstico (compra o contratación de energía mensual)? ¿Qué cuesta equivocarse por arriba y por abajo?
- ¿Cómo explicar «SARIMA en logaritmos con indicador covid» a un público no técnico, en una frase?
- ¿Qué figura muestra mejor la solución? (Sugerencia: serie 2015-2024 con pronóstico 2024 e IC 95 %.)

**Criterio 2, sustento técnico**
- ¿Qué evidencia de cada semana descarta cada alternativa (orden de diferenciación, candidatos, ARFIMA, GARCH)?
- ¿El resultado de 2024 confirma o contradice lo de 2023? ¿Se corrigió el sesgo al incluir 2023 en el entrenamiento?
- ¿Cómo leer el MASE (menor que 1 = mejor que el naive)?

**Criterio 3, conclusiones y recomendaciones**
- Por cada recomendación: ¿qué cifra la respalda? (p. ej., ancho del IC → margen de compra; sesgo → ajuste o monitoreo; reestimación anual → origen móvil.)
- Limitaciones: tamaño de la validación (12 meses), un solo indicador covid, sin temperatura, MA en el límite de invertibilidad, R/S con 83 datos.
- Alcance: ¿hasta qué horizonte y en qué condiciones es confiable el pronóstico?

## 4. Figuras y tablas candidatas (de los notebooks; rehacer sin código visible)

| N.º sugerido | Contenido | Origen |
|---|---|---|
| Fig. 1 | Serie mensual 2015-2024 con el periodo covid sombreado | S2 §1 o plantilla S4 |
| Fig. 2 | Pronóstico 2024 del modelo B con IC 95 % frente al observado y al naive | Plantilla S4 |
| Fig. 3 | ACF de residuos + histograma de H bajo ruido blanco (memoria larga) | S3, Figuras 1-2 |
| Tabla 1 | Resumen de la evidencia S2-S3-S4 (una fila por decisión) | Banco de evidencia |
| Tabla 2 | Métricas 2023 y 2024: B frente al naive (RMSE, MAE, MASE, cobertura) | S2, S3 y S4 |

## 5. Lista de verificación final

- [ ] 5 a 7 páginas, PDF o DOCX, nombre `mcdi505_s4rmoncada`
- [ ] Anexo: plantilla S4 ejecutada desde un kernel reiniciado
- [ ] Sin código; figuras numeradas y citadas en el texto; tablas reformateadas
- [ ] Cada cifra del informe coincide con el anexo o con los notebooks S2 y S3
- [ ] Referencias APA, todas citadas (Box et al., 2015; Hyndman y Athanasopoulos, 2021; Hurst, 1951; Bollerslev, 1986; Engle, 1982; Ljung y Box, 1978; Universidad Andrés Bello, s. f.)
- [ ] Declaración de uso de IA con herramienta, partes y verificación
- [ ] Retroalimentación de la Formativa 4 incorporada
- [ ] Entrega antes de las 23:59 del domingo de la Semana 4
