# Guía paso a paso --- Notebook de análisis de series de tiempo con ACF y PACF

**Curso:** MCDI505 --- Análisis de Series de Tiempo\
**Caso:** Consumo eléctrico del litoral\
**Notebook explicado:**
`mcdi505_s1_GUIA_COMPLETA_RESULTADOS_EJECUTADO.ipynb`\
**Dataset:** `consumo_electrico_litoral.csv`

------------------------------------------------------------------------

## 1. Objetivo de esta guía

Esta guía explica **cómo fue construido el notebook, por qué se ejecuta
cada paso, qué librerías se utilizan y cómo interpretar técnicamente sus
resultados**.

El flujo implementado sigue esta lógica:

``` text
Dataset CSV
   ↓
Carga y validación
   ↓
Conversión a serie temporal
   ↓
Control de fechas y valores faltantes
   ↓
Imputación temporal
   ↓
Exploración gráfica y estadística
   ↓
Evaluación tendencia / estacionalidad / varianza
   ↓
Descomposición STL
   ↓
ACF
   ↓
PACF
   ↓
Diferenciación regular y estacional
   ↓
Integración de evidencia
   ↓
Hipótesis de modelamiento SARIMA
```

La idea central es **comprender primero la estructura temporal** antes
de intentar construir un modelo predictivo.

------------------------------------------------------------------------

# 2. Librerías utilizadas

El notebook utiliza las siguientes importaciones reales:

``` python
from pathlib import Path
import zipfile
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import STL
from statsmodels.tsa.stattools import acf, pacf
```

## 2.1 pandas

``` python
import pandas as pd
```

`pandas` se utiliza para:

-   cargar el archivo CSV;
-   manipular tablas mediante `DataFrame`;
-   convertir fechas;
-   ordenar observaciones;
-   establecer un índice temporal;
-   detectar valores nulos;
-   calcular estadísticas descriptivas;
-   realizar interpolación;
-   calcular medias móviles;
-   agrupar por mes y año;
-   aplicar diferencias temporales.

Conceptualmente:

``` text
CSV → DataFrame → Serie temporal indexada por fecha
```

------------------------------------------------------------------------

## 2.2 NumPy

``` python
import numpy as np
```

NumPy proporciona operaciones numéricas utilizadas en cálculos como:

``` python
np.sqrt(N)
np.arange(...)
```

Por ejemplo, se utiliza para construir el umbral aproximado de
significancia de ACF/PACF:

``` text
± 1.96 / √N
```

------------------------------------------------------------------------

## 2.3 Matplotlib

``` python
import matplotlib.pyplot as plt
```

Es la librería principal de visualización.

Se utiliza para representar:

-   serie temporal original;
-   media móvil;
-   perfil mensual;
-   variabilidad;
-   componentes de STL;
-   ACF;
-   PACF;
-   series diferenciadas.

Los gráficos no son solamente decorativos: constituyen evidencia para
identificar **tendencia, estacionalidad, cambios de nivel y posibles
anomalías**.

------------------------------------------------------------------------

## 2.4 statsmodels

Es la librería estadística central del ejercicio.

### STL

``` python
from statsmodels.tsa.seasonal import STL
```

Permite separar una serie en:

``` text
Serie observada = Tendencia + Estacionalidad + Residuo
```

para el esquema aditivo utilizado.

### ACF y PACF gráficas

``` python
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
```

Generan los correlogramas.

### ACF y PACF numéricas

``` python
from statsmodels.tsa.stattools import acf, pacf
```

Permiten recuperar los coeficientes de autocorrelación y autocorrelación
parcial para cada rezago y analizarlos cuantitativamente.

------------------------------------------------------------------------

# 3. ¿Qué es una serie de tiempo?

Una serie temporal es un conjunto de observaciones ordenadas
cronológicamente.

En este caso:

``` text
fecha → consumo_gwh
```

Ejemplo conceptual:

``` text
2015-01 → consumo
2015-02 → consumo
2015-03 → consumo
...
2024-12 → consumo
```

A diferencia de una tabla convencional, **el orden temporal importa**.

El consumo de un mes puede estar relacionado con:

-   el mes anterior;
-   meses recientes;
-   el mismo mes del año anterior;
-   una tendencia de largo plazo.

ACF y PACF permiten estudiar precisamente estas dependencias.

------------------------------------------------------------------------

# 4. Paso 1 --- Carga del dataset

El primer objetivo es transformar el CSV en un `DataFrame`.

Conceptualmente:

``` python
df = pd.read_csv("consumo_electrico_litoral.csv")
```

Después se inspeccionan:

-   dimensiones;
-   columnas;
-   tipos de datos;
-   primeras observaciones;
-   valores faltantes.

Esto responde preguntas básicas:

``` text
¿Tengo los datos esperados?
¿La fecha se reconoce correctamente?
¿El consumo es numérico?
¿Existen valores faltantes?
¿Existen duplicados?
```

**Regla profesional:** nunca comenzar ACF/PACF antes de comprobar la
calidad y estructura temporal del dataset.

------------------------------------------------------------------------

# 5. Paso 2 --- Construcción del eje temporal

La fecha debe transformarse a un tipo temporal:

``` python
df["fecha"] = pd.to_datetime(df["fecha"])
```

Posteriormente se ordena:

``` python
df = df.sort_values("fecha")
```

y se utiliza la fecha como índice.

El objetivo final es obtener:

``` text
DatetimeIndex
2015-01
2015-02
...
2024-12
```

Esto permite que pandas y statsmodels comprendan que los registros
forman una secuencia temporal.

------------------------------------------------------------------------

# 6. Paso 3 --- Validación de continuidad temporal

Una serie mensual debería tener una observación por mes.

Para 10 años:

``` text
10 años × 12 meses = 120 observaciones
```

El notebook trabaja con **120 meses entre enero de 2015 y diciembre de
2024**.

Se debe comprobar que:

``` text
fecha(t+1) = fecha(t) + 1 mes
```

Además se buscan:

-   meses ausentes;
-   fechas duplicadas;
-   consumo faltante.

Esta validación es crítica porque un rezago 12 solo significa realmente
"mismo mes del año anterior" cuando la frecuencia mensual está
correctamente conservada.

------------------------------------------------------------------------

# 7. Paso 4 --- Tratamiento de valores faltantes

El dataset presenta tres observaciones faltantes de consumo.

Para conservar la estructura mensual se utiliza **interpolación
temporal**.

Conceptualmente:

``` python
serie = serie.interpolate(method="time")
```

La interpolación estima un valor utilizando la posición temporal de los
puntos conocidos cercanos.

Ejemplo:

``` text
Mes t-1       Mes t       Mes t+1
  100          NaN          104
                ↓
              ≈102
```

## ¿Por qué no eliminar esos meses?

Porque eliminar observaciones podría romper la regularidad temporal:

``` text
enero → febrero → abril
```

y entonces un rezago ya no representaría necesariamente la distancia
cronológica esperada.

## Precaución

Un valor imputado **no es una observación real**. Debe documentarse
porque puede afectar ligeramente:

-   varianza;
-   autocorrelación;
-   residuos;
-   ajuste de modelos posteriores.

------------------------------------------------------------------------

# 8. Paso 5 --- Exploración de la serie

Antes de descomponer o calcular ACF/PACF se grafica la serie completa.

El objetivo es reconocer visualmente:

``` text
Nivel
Tendencia
Estacionalidad
Cambios estructurales
Variabilidad
Outliers
```

En el notebook se observa una trayectoria de largo plazo creciente,
acompañada de fluctuaciones recurrentes durante el año y una
perturbación relevante alrededor de 2020.

------------------------------------------------------------------------

# 9. Paso 6 --- Media móvil

Una serie mensual contiene variación de corto plazo que puede dificultar
la visualización de la tendencia.

Por ello se calcula una media móvil de 12 meses:

``` python
rolling(12).mean()
```

Conceptualmente:

``` text
Promedio móvil(t) =
promedio de los últimos 12 meses
```

La ventana 12 tiene sentido porque la frecuencia es mensual.

La media móvil suaviza la estacionalidad y permite visualizar mejor el
movimiento de largo plazo.

------------------------------------------------------------------------

# 10. Paso 7 --- Perfil estacional mensual

Se agrupan los consumos según el mes calendario:

``` text
Todos los enero
Todos los febrero
...
Todos los diciembre
```

y se calcula el promedio de cada grupo.

Esto permite responder:

> ¿Existe un patrón que se repite aproximadamente cada 12 meses?

En el análisis realizado, enero y diciembre presentan promedios
elevados, mientras abril y mayo se encuentran entre los meses de menor
consumo promedio.

La repetición sistemática por mes es evidencia de **estacionalidad
anual**.

------------------------------------------------------------------------

# 11. Paso 8 --- Evaluación nivel--varianza

Antes de elegir entre una representación aditiva o multiplicativa
conviene estudiar si la amplitud de las fluctuaciones aumenta con el
nivel.

## Modelo aditivo

``` text
Y(t) = T(t) + S(t) + R(t)
```

Adecuado cuando la amplitud estacional permanece aproximadamente estable
en unidades absolutas.

## Modelo multiplicativo

``` text
Y(t) = T(t) × S(t) × R(t)
```

Más apropiado cuando las fluctuaciones crecen proporcionalmente con el
nivel.

El notebook analiza la relación entre nivel y dispersión móvil. La
correlación obtenida es aproximadamente:

``` text
-0.078
```

Al ser cercana a cero, no existe evidencia fuerte de que la dispersión
aumente proporcionalmente con el nivel.

Esto respalda el uso de una **descomposición STL aditiva**.

------------------------------------------------------------------------

# 12. Paso 9 --- Descomposición STL

Se aplica:

``` python
STL(serie, period=12)
```

## ¿Qué significa `period=12`?

La serie es mensual:

``` text
12 observaciones = 1 año
```

Por tanto, se busca un patrón estacional que se repita cada doce meses.

STL produce:

``` text
Observed
Trend
Seasonal
Resid
```

------------------------------------------------------------------------

# 13. Componente de tendencia

La tendencia representa la evolución suavizada de largo plazo.

En este caso permite distinguir:

-   crecimiento hasta aproximadamente 2019;
-   perturbación/retroceso alrededor de 2020--2021;
-   recuperación y crecimiento posterior.

La tendencia no debe confundirse con cada fluctuación mensual.

------------------------------------------------------------------------

# 14. Componente estacional

El componente estacional captura el patrón que se repite aproximadamente
cada año.

La descomposición entrega una fuerza estacional cercana a:

``` text
0.885
```

lo que muestra una estructura estacional importante.

La fuerza de tendencia calculada es aproximadamente:

``` text
0.818
```

Ambos resultados indican que una fracción importante de la variabilidad
de la serie posee estructura temporal y no corresponde simplemente a
ruido.

------------------------------------------------------------------------

# 15. ¿Dónde aparece el ciclo?

Es importante distinguir:

``` text
Tendencia ≠ ciclo
Estacionalidad ≠ ciclo
Residuo ≠ ciclo
```

STL separa explícitamente:

``` text
tendencia + estacionalidad + residuo
```

pero **no genera un componente cíclico independiente**.

Una oscilación de mediano plazo puede quedar absorbida dentro de la
tendencia. Por ello, la caída y recuperación alrededor de 2020--2021
puede describirse como una fluctuación de mediano plazo, pero no debe
declararse automáticamente como un ciclo periódico.

------------------------------------------------------------------------

# 16. Componente residual

El residuo representa lo que queda después de retirar tendencia y
estacionalidad:

``` text
Residuo =
Observado - Tendencia - Estacionalidad
```

Idealmente debería comportarse de forma aproximadamente aleatoria.

El notebook obtiene una desviación estándar residual cercana a:

``` text
3.79 GWh
```

frente a una desviación considerablemente mayor de la serie original.

Esto indica que STL explica una porción importante de la estructura.

También aparecen residuos especialmente grandes alrededor de
abril--junio de 2020, lo que señala una perturbación que los componentes
regulares no explican completamente.

------------------------------------------------------------------------

# 17. Paso 10 --- ¿Qué es ACF?

**ACF --- Autocorrelation Function** mide cuánto se correlaciona una
serie con versiones rezagadas de sí misma.

Para un rezago `k`:

``` text
ACF(k) = Corr(Yt, Yt-k)
```

Ejemplos en una serie mensual:

``` text
lag 1  → relación con el mes anterior
lag 2  → relación con dos meses atrás
lag 12 → relación con el mismo mes del año anterior
lag 24 → relación con dos años atrás
```

Una autocorrelación positiva alta indica que valores separados por ese
número de períodos tienden a moverse de manera similar.

------------------------------------------------------------------------

# 18. Paso 11 --- ACF del caso

El notebook calcula hasta 48 rezagos:

``` python
plot_acf(y, lags=48)
```

porque:

``` text
48 meses = 4 años
```

Resultados importantes:

    Lag   ACF aproximada Lectura
  ----- ---------------- ------------------------------------
      1            0.771 fuerte persistencia de corto plazo
      2            0.415 dependencia todavía relevante
     12            0.654 fuerte relación anual
     24            0.448 patrón anual persiste
     36            0.336 persistencia a tres años
     48            0.317 estructura anual todavía visible

La presencia de valores elevados en:

``` text
12, 24, 36, 48
```

es evidencia particularmente clara de periodicidad anual.

------------------------------------------------------------------------

# 19. Paso 12 --- ¿Qué es PACF?

**PACF --- Partial Autocorrelation Function** mide la relación directa
entre `Yt` y `Yt-k` eliminando estadísticamente el efecto de los rezagos
intermedios.

Ejemplo:

ACF en lag 3 puede contener indirectamente:

``` text
Yt → Yt-1 → Yt-2 → Yt-3
```

PACF intenta responder:

> ¿Cuánta relación directa queda entre `Yt` y `Yt-3` después de
> controlar los rezagos 1 y 2?

Por eso ACF y PACF **no significan lo mismo**.

------------------------------------------------------------------------

# 20. Paso 13 --- PACF del caso

El notebook utiliza:

``` python
plot_pacf(
    y,
    lags=48,
    method="ywm"
)
```

Los rezagos aproximadamente significativos encontrados son:

``` text
1, 2, 4, 6, 9, 10 y 13
```

El rezago 1 es especialmente importante porque representa una
dependencia directa fuerte respecto del mes anterior.

Un punto conceptual importante es que:

``` text
PACF(12) no significativo
```

**no implica que no exista estacionalidad anual**.

La estacionalidad se sustenta conjuntamente en:

-   perfil mensual;
-   STL;
-   ACF(12);
-   ACF(24);
-   ACF(36);
-   ACF(48).

PACF responde una pregunta distinta porque controla las dependencias
intermedias.

------------------------------------------------------------------------

# 21. Paso 14 --- Significancia aproximada

El notebook utiliza como referencia:

``` python
1.96 / np.sqrt(N)
```

Con `N = 120`:

``` text
1.96 / √120 ≈ 0.179
```

Por tanto, como regla aproximada:

``` text
ACF/PACF > +0.179
o
ACF/PACF < -0.179
```

se consideran fuera de la banda aproximada del 95 %.

Este umbral es una ayuda diagnóstica, no una regla absoluta para
seleccionar automáticamente un modelo.

------------------------------------------------------------------------

# 22. Paso 15 --- ¿Por qué diferenciar?

Una serie con tendencia o estacionalidad puede no ser estacionaria.

La diferenciación transforma la serie para estudiar si esas estructuras
pueden reducirse.

## Primera diferencia

``` python
y.diff()
```

equivale a:

``` text
Y't = Yt - Yt-1
```

Compara cada mes con el inmediatamente anterior y ayuda a reducir
tendencia/cambios persistentes de nivel.

------------------------------------------------------------------------

# 23. Diferencia estacional

``` python
y.diff(12)
```

equivale a:

``` text
Y't = Yt - Yt-12
```

Compara cada observación con el mismo mes del año anterior.

Ejemplo:

``` text
enero 2024 - enero 2023
febrero 2024 - febrero 2023
```

Esto ataca directamente una estacionalidad de periodicidad 12.

------------------------------------------------------------------------

# 24. Diferenciación combinada

El notebook también evalúa:

``` python
y.diff().diff(12)
```

que combina:

``` text
d = 1
D = 1
s = 12
```

La finalidad no es afirmar automáticamente que esa configuración sea la
correcta, sino **comparar cómo cambia la estructura de
autocorrelación**.

------------------------------------------------------------------------

# 25. Paso 16 --- ACF/PACF después de diferenciar

Se generan nuevamente ACF y PACF para:

``` text
1. primera diferencia;
2. diferencia estacional;
3. diferencia regular + estacional.
```

Se compara cada correlograma con el de la serie original.

La pregunta es:

> ¿Las autocorrelaciones persistentes disminuyeron?

Si ocurre, existe evidencia de que tendencia y/o estacionalidad
explicaban parte importante de la dependencia temporal original.

------------------------------------------------------------------------

# 26. ¿ACF y PACF entregan directamente un modelo ARIMA?

No.

Son herramientas de **identificación y diagnóstico**.

De forma orientativa:

``` text
PACF → ayuda a estudiar componente AR
ACF  → ayuda a estudiar componente MA
```

pero en una serie real no corresponde seleccionar un modelo únicamente
porque un gráfico "parezca" cortar en cierto rezago.

La selección profesional requiere además:

``` text
estacionariedad
AIC
BIC
validación temporal
análisis de residuos
comparación de modelos
```

------------------------------------------------------------------------

# 27. Paso 17 --- Hipótesis SARIMA

Dado que existe estructura anual, el notebook propone evaluar
posteriormente una familia:

``` text
SARIMA(p,d,q)(P,D,Q,12)
```

donde:

  Parámetro   Significado
  ----------- ----------------------------------------
  `p`         orden autorregresivo
  `d`         diferenciación regular
  `q`         orden de media móvil
  `P`         AR estacional
  `D`         diferenciación estacional
  `Q`         MA estacional
  `12`        periodicidad anual de la serie mensual

Esto es una **hipótesis de modelamiento posterior**, no un modelo
seleccionado definitivamente.

------------------------------------------------------------------------

# 28. Cómo se conectan todos los análisis

El valor del notebook no está en ejecutar técnicas aisladas, sino en
comprobar si entregan una historia coherente.

``` text
GRÁFICO ORIGINAL
      ↓
sugiere tendencia + patrón anual
      ↓
MEDIA MÓVIL
      ↓
hace visible la evolución de largo plazo
      ↓
PERFIL MENSUAL
      ↓
confirma diferencias sistemáticas entre meses
      ↓
STL
      ↓
separa tendencia + estacionalidad + residuo
      ↓
ACF
      ↓
muestra persistencia y picos 12,24,36,48
      ↓
PACF
      ↓
identifica dependencias directas
      ↓
DIFERENCIACIÓN
      ↓
evalúa reducción de tendencia/estacionalidad
      ↓
CONCLUSIÓN
      ↓
serie con estructura temporal → evaluar SARIMA s=12
```

------------------------------------------------------------------------

# 29. Resultados principales que conviene comprender

No es recomendable memorizar números sin entender qué significan.

### 120 observaciones

Representan 10 años × 12 meses.

### ACF(1) ≈ 0.771

El consumo actual tiene una relación fuerte con el del mes anterior.

### ACF(12) ≈ 0.654

Existe una relación importante con el mismo mes del año anterior.

### ACF(24), ACF(36), ACF(48)

La dependencia anual continúa apareciendo a múltiplos de doce.

### Fuerza estacional ≈ 0.885

STL encuentra un componente estacional fuerte.

### Fuerza de tendencia ≈ 0.818

La evolución de largo plazo explica una parte relevante de la
estructura.

### Residuo ≈ 3.79 GWh de desviación estándar

Después de extraer tendencia y estacionalidad queda bastante menos
variabilidad que en la serie original.

------------------------------------------------------------------------

# 30. Errores conceptuales que deben evitarse

## Error 1 --- "ACF y PACF son modelos"

Incorrecto.

Son funciones estadísticas utilizadas para estudiar dependencia
temporal.

## Error 2 --- "Lag 12 significa diciembre"

Incorrecto.

Lag 12 significa:

``` text
12 períodos hacia atrás
```

En una serie mensual equivale a aproximadamente un año.

## Error 3 --- "PACF(12) no significativo significa que no hay estacionalidad"

Incorrecto.

La estacionalidad debe evaluarse con evidencia conjunta.

## Error 4 --- "STL encontró un ciclo"

No necesariamente.

STL separa tendencia, estacionalidad y residuo, no un ciclo
independiente.

## Error 5 --- "Un pico de ACF determina automáticamente q"

Es una simplificación excesiva.

ACF/PACF orientan; la selección debe validarse estadísticamente.

## Error 6 --- "Diferenciar siempre mejora la serie"

Incorrecto.

Una diferenciación excesiva puede destruir estructura útil e introducir
dependencia artificial.

------------------------------------------------------------------------

# 31. Cómo ejecutar el notebook

Coloque en una misma carpeta:

``` text
mcdi505_s1_GUIA_COMPLETA_RESULTADOS.ipynb
consumo_electrico_litoral.csv
```

Abra el notebook en Jupyter Notebook, JupyterLab o VS Code.

Luego ejecute:

``` text
Kernel
  ↓
Restart Kernel
  ↓
Run All
```

El objetivo es verificar reproducibilidad:

``` text
celda 1
  ↓
celda 2
  ↓
...
  ↓
última celda
  ↓
sin errores
```

------------------------------------------------------------------------

# 32. Librerías requeridas para un ambiente nuevo

En un entorno Python nuevo, las dependencias principales son:

``` bash
pip install pandas numpy matplotlib statsmodels jupyter
```

Una forma más controlada consiste en utilizar un entorno virtual:

``` bash
python -m venv .venv
```

Activarlo y posteriormente instalar las dependencias.

El notebook debe ejecutarse con el intérprete correspondiente a ese
entorno.

------------------------------------------------------------------------

# 33. Relación con la rúbrica

La estructura técnica se diseñó para cubrir los cuatro bloques
analíticos principales:

  -----------------------------------------------------------------------
  Criterio                            Evidencia del notebook
  ----------------------------------- -----------------------------------
  Exploración                         serie completa, media móvil, perfil
                                      mensual, variabilidad

  Descomposición                      STL, elección del esquema,
                                      tendencia, estacionalidad y residuo

  ACF/PACF                            correlogramas, valores numéricos,
                                      rezagos significativos

  Interpretación integrada            conexión entre exploración, STL,
                                      ACF/PACF y modelamiento posterior
  -----------------------------------------------------------------------

La guía de la evaluación exige precisamente que el análisis relacione
gráficos exploratorios, descomposición, ACF y PACF y que la conclusión
técnica considere las implicancias para el modelamiento posterior.

------------------------------------------------------------------------

# 34. Preguntas de autoevaluación

Después de estudiar el notebook debería poder responder sin mirar el
código:

1.  ¿Por qué el período estacional utilizado es 12?
2.  ¿Qué diferencia existe entre ACF y PACF?
3.  ¿Qué significa ACF(1) = 0.771?
4.  ¿Qué significa un pico de ACF en lag 12?
5.  ¿Por qué se utiliza STL?
6.  ¿Por qué el esquema aditivo resulta razonable en este caso?
7.  ¿Qué representa el residuo de STL?
8.  ¿Por qué se realiza `diff(12)`?
9.  ¿Qué diferencia existe entre `d` y `D` en SARIMA?
10. ¿Por qué ACF/PACF no son suficientes para elegir definitivamente un
    modelo?
11. ¿Por qué no corresponde afirmar automáticamente que la fluctuación
    de 2020 es un ciclo?
12. ¿Qué evidencia conjunta demuestra estacionalidad anual?

Si puede explicar estas preguntas con sus propias palabras, ya comprende
la lógica fundamental del notebook.

------------------------------------------------------------------------

# 35. Resumen final

El notebook sigue una secuencia metodológica deliberada:

``` text
1. Comprender el dataset
2. Validar el eje temporal
3. Corregir faltantes sin romper la frecuencia
4. Visualizar la serie
5. Identificar tendencia y estacionalidad
6. Justificar el tipo de descomposición
7. Aplicar STL
8. Interpretar tendencia, estacionalidad y residuo
9. Calcular ACF
10. Calcular PACF
11. Identificar rezagos relevantes
12. Diferenciar para estudiar estacionariedad estructural
13. Comparar los correlogramas
14. Integrar toda la evidencia
15. Plantear SARIMA(s=12) como familia candidata para una fase posterior
```

La idea más importante es:

> **ACF y PACF no deben analizarse aisladas.** Su interpretación cobra
> sentido cuando se conecta con la frecuencia de la serie, los gráficos
> exploratorios y la descomposición temporal.

------------------------------------------------------------------------

## Referencias utilizadas en el notebook

Cleveland, R. B., Cleveland, W. S., McRae, J. E., & Terpenning, I.
(1990). *STL: A seasonal-trend decomposition procedure based on loess*.
Journal of Official Statistics, 6(1), 3--73.

Hyndman, R. J., & Athanasopoulos, G. (2021). *Forecasting: Principles
and Practice* (3rd ed.). OTexts.

Seabold, S., & Perktold, J. (2010). Statsmodels: Econometric and
statistical modeling with Python. *Proceedings of the 9th Python in
Science Conference*, 92--96.
