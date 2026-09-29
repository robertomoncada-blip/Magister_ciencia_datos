"""Genera la serie del caso transversal MCDI505.

DOCUMENTO CONFIDENCIAL - solo equipo docente.
No distribuir antes del cierre de la Semana 4.

Proceso generador (CONFIDENCIAL - solo pauta docente):
  consumo_gwh = nivel * estacionalidad_multiplicativa * factor_covid * ruido
  nivel        : crecimiento ~2.2% anual ligado a numero de clientes
  estacional   : bimodal (verano austral: refrigeracion; invierno: calefaccion)
  covid        : caida abrupta 2020-03, minimo 2020-05, recuperacion gradual
  nivel_estoc  : componente de raiz unitaria en el log (sigma=0.008)
  ruido        : AR(1) leve sobre el log, phi=0.30, sigma=0.020
  Ademas: 3 valores faltantes (falla de telemetria) y 1 atipico (recalibracion).
"""
import numpy as np
import pandas as pd

SEMILLA = 505


def generar_caso(semilla=SEMILLA):
    rng = np.random.default_rng(semilla)
    idx = pd.date_range("2015-01-01", "2024-12-01", freq="MS")
    n = len(idx)
    t = np.arange(n)
    mes = idx.month.to_numpy()

    # --- clientes comerciales conectados (exogena, crece con saltos) ---
    clientes = 41800 + 118 * t + rng.normal(0, 60, n).cumsum() * 0.35
    clientes[idx.get_loc("2019-04-01"):] += 900     # incorporacion de un polo comercial
    clientes = np.round(clientes).astype(int)

    # --- temperatura media mensual (Region de Valparaiso, hemisferio sur) ---
    temp = 14.6 + 4.4 * np.cos(2 * np.pi * (mes - 1) / 12) + 0.018 * t + rng.normal(0, 0.75, n)

    # --- dias habiles del mes ---
    dias_habiles = np.array([np.busday_count(d.date(),
                                             (d + pd.offsets.MonthEnd(1) + pd.Timedelta(days=1)).date())
                             for d in idx])

    # --- nivel base ligado a clientes ---
    nivel = 0.00212 * clientes                       # GWh por cliente comercial

    # --- estacionalidad multiplicativa bimodal ---
    # refrigeracion en verano (ene-feb), calefaccion en invierno (jul-ago)
    estacional = (1.0
                  + 0.105 * np.cos(2 * np.pi * (mes - 1) / 12)     # verano alto
                  + 0.085 * np.cos(4 * np.pi * (mes - 1) / 12))    # segundo pico invernal
    estacional *= 1 + 0.0035 * t / 12                              # amplitud crece levemente

    # --- efecto de dias habiles ---
    ef_habiles = 1 + 0.011 * (dias_habiles - dias_habiles.mean())

    # --- shock COVID-19 ---
    covid = np.ones(n)
    pos = {d: i for i, d in enumerate(idx.strftime("%Y-%m"))}
    caida = {"2020-03": 0.93, "2020-04": 0.775, "2020-05": 0.755, "2020-06": 0.79,
             "2020-07": 0.83, "2020-08": 0.86, "2020-09": 0.885, "2020-10": 0.905,
             "2020-11": 0.925, "2020-12": 0.94}
    for k, v in caida.items():
        covid[pos[k]] = v
    for i, k in enumerate(pd.date_range("2021-01-01", "2021-12-01", freq="MS").strftime("%Y-%m")):
        covid[pos[k]] = 0.952 + 0.004 * i                          # recuperacion gradual

    # --- ruido AR(1) sobre el log ---
    phi, sigma = 0.30, 0.020
    e = rng.normal(0, sigma, n)
    u = np.empty(n)
    u[0] = e[0] / np.sqrt(1 - phi**2)
    for i in range(1, n):
        u[i] = phi * u[i - 1] + e[i]

    # --- nivel estocastico (raiz unitaria): lo que hace que ARIMA sea el
    #     modelo correcto y no una regresion con tendencia determinista ---
    nivel_estoc = np.exp(np.cumsum(rng.normal(0, 0.008, n)))

    consumo = nivel * nivel_estoc * estacional * ef_habiles * covid * np.exp(u)

    # --- atipico: recalibracion de medidores ---
    consumo[pos["2017-11"]] *= 1.13

    df = pd.DataFrame({
        "fecha": idx,
        "consumo_gwh": np.round(consumo, 2),
        "clientes_comerciales": clientes,
        "temperatura_media_c": np.round(temp, 1),
        "dias_habiles": dias_habiles,
    })

    # --- faltantes por falla de telemetria ---
    for k in ["2016-08", "2019-02", "2022-06"]:
        df.loc[pos[k], "consumo_gwh"] = np.nan

    return df


if __name__ == "__main__":
    df = generar_caso()
    print(df.head(14).to_string(index=False))
    print("...")
    print(df.tail(6).to_string(index=False))
    print("\nn =", len(df), "| faltantes:", df["consumo_gwh"].isna().sum())
    print(df["consumo_gwh"].describe().round(2).to_string())
