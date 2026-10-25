"""Construye el informe ejecutivo de la Sumativa 4 (PDF) a partir de notebooks/mcdi505_s4rmoncada.ipynb.

Maqueta: los textos se copian LITERALMENTE de las celdas del autor (las celdas [BORRADOR] se ignoran);
las tablas y figuras se recalculan con el mismo código del notebook (anexo), sin mostrar código.
Uso (desde MCDI505/):  ../.venv/Scripts/python.exe -I scripts/construir_informe_s4.py [salida.pdf]
"""
import io
import json
import os
import re
import sys
from datetime import date

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (Image, KeepTogether, ListFlowable, ListItem, Paragraph, SimpleDocTemplate,
                                Spacer, Table, TableStyle)

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NB = os.path.join(RAIZ, "notebooks", "mcdi505_s4rmoncada.ipynb")
SALIDA = sys.argv[1] if len(sys.argv) > 1 else os.path.join(RAIZ, "entregas", "mcdi505_s4rmoncada.pdf")

# ------------------------------------------------------------------------------------------------
# 1. Notebook: textos del autor y re-ejecución del código (para tablas y figuras)
# ------------------------------------------------------------------------------------------------
nb = json.load(open(NB, encoding="utf-8"))
celdas = [("".join(c["source"]), c["cell_type"]) for c in nb["cells"]]
md = [s for s, t in celdas if t == "markdown" and "[BORRADOR]" not in s]


def celda(inicio):
    """Celda markdown del autor que empieza con `inicio` (falla si no existe o hay más de una)."""
    c = [s for s in md if s.startswith(inicio)]
    assert len(c) == 1, f"no se encontró una única celda que empiece con {inicio!r}"
    return c[0]


def bloques(texto):
    """Separa una celda en párrafos (líneas en blanco) y listas (líneas que empiezan con '- ')."""
    out = []
    for b in re.split(r"\n\s*\n", texto.strip()):
        lineas = [l for l in b.splitlines() if l.strip()]
        if lineas and all(l.startswith("- ") for l in lineas):
            if out and out[-1][0] == "lista":
                out[-1][1].extend(l[2:] for l in lineas)
            else:
                out.append(("lista", [l[2:] for l in lineas]))
        elif lineas and lineas[0].startswith("- ") is False and any(l.startswith("- ") for l in lineas):
            # encabezado en la primera línea seguido de viñetas
            out.append(("parrafo", lineas[0]))
            out.append(("lista", [l[2:] for l in lineas[1:]]))
        else:
            out.append(("parrafo", " ".join(lineas)))
    return out


figuras = []
_show = plt.show


def _capturar(*a, **k):
    fig = plt.gcf()
    for ax in fig.axes:                      # el título va como leyenda APA, fuera de la imagen
        if ax.get_title(loc="left").startswith("Figura"):
            ax.set_title("", loc="left")
    if fig._suptitle is not None and fig._suptitle.get_text().startswith("Figura"):
        fig._suptitle.set_text("")
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=220, bbox_inches="tight")
    figuras.append((buf, fig.get_size_inches()))
    plt.close(fig)


plt.show = _capturar
ns = {"__name__": "__main__"}
os.chdir(os.path.join(RAIZ, "notebooks"))
for s, t in celdas:
    if t == "code":
        exec(compile(s, "notebook", "exec"), ns)
plt.show = _show
assert len(figuras) == 2, f"se esperaban 2 figuras y hay {len(figuras)}"

# ------------------------------------------------------------------------------------------------
# 2. Estilos (Calibri 11, APA 7: tablas y figuras con número en negrita y título en cursiva)
# ------------------------------------------------------------------------------------------------
F = "C:/Windows/Fonts/"
for nombre, archivo in [("Cal", "calibri.ttf"), ("Cal-B", "calibrib.ttf"), ("Cal-I", "calibrii.ttf"), ("Cal-BI", "calibriz.ttf")]:
    pdfmetrics.registerFont(TTFont(nombre, F + archivo))
pdfmetrics.registerFontFamily("Cal", normal="Cal", bold="Cal-B", italic="Cal-I", boldItalic="Cal-BI")

GRANATE = colors.HexColor("#b30338")
GRIS = colors.HexColor("#555555")
st = {
    "titulo": ParagraphStyle("titulo", fontName="Cal-B", fontSize=17, leading=21, textColor=GRANATE, spaceAfter=4),
    "meta": ParagraphStyle("meta", fontName="Cal", fontSize=9.5, leading=12.5, textColor=GRIS),
    "h1": ParagraphStyle("h1", fontName="Cal-B", fontSize=13, leading=16, textColor=GRANATE, spaceBefore=10, spaceAfter=4, keepWithNext=1),
    "h2": ParagraphStyle("h2", fontName="Cal-B", fontSize=11, leading=14, spaceBefore=6, spaceAfter=2, keepWithNext=1),
    "p": ParagraphStyle("p", fontName="Cal", fontSize=11, leading=14.2, alignment=TA_JUSTIFY, spaceAfter=5),
    "li": ParagraphStyle("li", fontName="Cal", fontSize=11, leading=14.2, alignment=TA_JUSTIFY),
    "cap_n": ParagraphStyle("cap_n", fontName="Cal-B", fontSize=10.5, leading=13, spaceBefore=6),
    "cap_t": ParagraphStyle("cap_t", fontName="Cal-I", fontSize=10.5, leading=13, spaceAfter=3),
    "nota": ParagraphStyle("nota", fontName="Cal", fontSize=9, leading=11.2, textColor=GRIS, spaceBefore=2, spaceAfter=6, alignment=TA_JUSTIFY),
    "td": ParagraphStyle("td", fontName="Cal", fontSize=9, leading=11, alignment=TA_LEFT),
    "th": ParagraphStyle("th", fontName="Cal-B", fontSize=9, leading=11, alignment=TA_LEFT),
    "ref": ParagraphStyle("ref", fontName="Cal", fontSize=10.5, leading=13.2, leftIndent=0.9 * cm, firstLineIndent=-0.9 * cm, spaceAfter=3),
}


def md_a_rl(t):
    """Markdown mínimo del autor → marcado de ReportLab (negrita, cursiva, subíndices c_u y c_o)."""
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", t)
    t = re.sub(r"\bc_([uo])\b", r"c<sub>\1</sub>", t)
    return t


def P(t, estilo="p"):
    return Paragraph(md_a_rl(t), st[estilo])


def lista(items):
    return ListFlowable([ListItem(P(i, "li"), leftIndent=12, value="•") for i in items],
                        bulletType="bullet", start="•", leftIndent=12, bulletFontName="Cal", spaceAfter=5)


def poner(bls, omitir_primero=False):
    out = []
    for i, (tipo, c) in enumerate(bls):
        if omitir_primero and i == 0:
            continue
        out.append(lista(c) if tipo == "lista" else P(c))
    return out


def num(x, d=1):
    """Formato chileno: separador de miles '.', decimal ','."""
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return "—"
    s = f"{x:,.{d}f}"
    return s.replace(",", "§").replace(".", ",").replace("§", ".").replace("-", "−")   # signo menos tipográfico


def tabla(numero, titulo, filas, anchos, nota, cabeceras=1, alinear_der_desde=1, extra=()):
    datos = [[Paragraph(str(c), st["th" if r < cabeceras else "td"]) for c in fila] for r, fila in enumerate(filas)]   # marcado propio, no texto del autor
    t = Table(datos, colWidths=anchos, repeatRows=cabeceras, hAlign="LEFT")
    estilo = [("LINEABOVE", (0, 0), (-1, 0), 0.9, colors.black),
              ("LINEBELOW", (0, cabeceras - 1), (-1, cabeceras - 1), 0.6, colors.black),
              ("LINEBELOW", (0, -1), (-1, -1), 0.9, colors.black),
              ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
              ("TOPPADDING", (0, 0), (-1, -1), 1.6), ("BOTTOMPADDING", (0, 0), (-1, -1), 1.6),
              ("LEFTPADDING", (0, 0), (-1, -1), 3), ("RIGHTPADDING", (0, 0), (-1, -1), 3)]
    estilo += list(extra)
    t.setStyle(TableStyle(estilo))
    for r in range(cabeceras, len(datos)):                     # cifras alineadas a la derecha
        for c in range(alinear_der_desde, len(filas[0])):
            datos[r][c].style = ParagraphStyle("tdr", parent=st["td"], alignment=2)
    return KeepTogether([Paragraph(f"Tabla {numero}", st["cap_n"]), Paragraph(titulo, st["cap_t"]), t,
                         Paragraph("<i>Nota.</i> " + nota, st["nota"])])


def figura(numero, titulo, idx, ancho_cm, nota):
    buf, (w, h) = figuras[idx]
    buf.seek(0)
    from reportlab.lib.utils import ImageReader
    iw, ih = ImageReader(buf).getSize()
    buf.seek(0)
    ancho = ancho_cm * cm
    return KeepTogether([Paragraph(f"Figura {numero}", st["cap_n"]), Paragraph(titulo, st["cap_t"]),
                         Image(buf, width=ancho, height=ancho * ih / iw),
                         Paragraph("<i>Nota.</i> " + nota, st["nota"])])


# ------------------------------------------------------------------------------------------------
# 3. Tablas (mismas cifras que el anexo)
# ------------------------------------------------------------------------------------------------
res = ns["resumen"]
t1 = [["Periodo", "Método", "RMSE (GWh)", "MAE (GWh)", "MASE", "Cobertura IC 95 %"]]
for (periodo, metodo), f in res.iterrows():
    t1.append([periodo, metodo, num(f["RMSE"], 2), num(f["MAE"], 2), num(f["MASE"], 2),
               "—" if np.isnan(f["Cobertura IC 95 %"]) else f"{int(round(12 * f['Cobertura IC 95 %']))}/12"])
err24 = ns["err24"]
y = ns["y"]
nota_t1 = (f"Modelo final: SARIMA(0,1,1)(0,1,1)<sub>12</sub> sobre el logaritmo del consumo, con indicadora covid, "
           f"reestimado con datos hasta diciembre de 2022 (validación 2023) y hasta diciembre de 2023 (prueba 2024). "
           f"Pronóstico puntual con la media corregida por sesgo. MASE &lt; 1 indica un error menor que el del naive estacional. "
           f"En 2024, el sesgo medio fue {num(err24.mean(), 2)} GWh ({num(100 * err24.mean() / y['2024'].mean(), 1)} % del consumo medio), "
           f"con {(err24 > 0).sum()} de 12 meses subestimados y un ancho medio del intervalo de {num(np.mean(ns['sup24'] - ns['inf24']), 1)} GWh. "
           f"Fuente: anexo, §1.")

tm = ns["tabla_modelos"]
cortos = {"B. SARIMA(0,1,1)(0,1,1)12 + covid (final)": ("B. SARIMA(0,1,1)(0,1,1)<sub>12</sub> + covid", "Modelo final"),
          "A. SARIMA(0,1,0)(0,1,1)12 + covid (S2: descartado por Ljung-Box)": ("A. SARIMA(0,1,0)(0,1,1)<sub>12</sub> + covid", "Descartado en la S2: Ljung-Box"),
          "B + ARFIMA(0,d,0) (S3: sin memoria larga)": ("B + ARFIMA(0,<i>d</i>,0)", "S3: sin memoria larga"),
          "B + bandas GARCH(1,1) (S3: sin volatilidad)": ("B + bandas GARCH(1,1)", "S3: sin volatilidad condicional"),
          "Naive estacional (referencia)": ("Naive estacional", "Referencia")}
t2 = [["Modelo", "Situación", "RMSE", "MAE", "MASE", "RMSE", "MAE", "MASE", "Ancho IC"],
      ["", "", "Validación 2023", "", "", "Prueba 2024", "", "", "2024"]]
for nombre, (corto, sit) in cortos.items():
    a, b = tm.loc[("Validación 2023", nombre)], tm.loc[("Prueba 2024", nombre)]
    t2.append([corto, sit, num(a["RMSE"], 2), num(a["MAE"], 2), num(a["MASE"], 2),
               num(b["RMSE"], 2), num(b["MAE"], 2), num(b["MASE"], 2), num(b["Ancho medio"], 1)])
nota_t2 = ("RMSE, MAE y ancho medio del intervalo al 95 % en GWh. Todos los modelos cubrieron 12 de 12 meses con su intervalo al 95 % "
           "en ambos periodos. El <i>d</i> del ARFIMA se reestimó con el exponente de Hurst de los residuos "
           f"({num(tm.loc[('Validación 2023', 'B + ARFIMA(0,d,0) (S3: sin memoria larga)'), 'd (ARFIMA)'], 3)} en 2023 y "
           f"{num(tm.loc[('Prueba 2024', 'B + ARFIMA(0,d,0) (S3: sin memoria larga)'), 'd (ARFIMA)'], 3)} en 2024). Fuente: anexo, §2.")

tc = ns["tabla_costo"]
t3 = [["c<sub>u</sub>/c<sub>o</sub>", "Volumen contratado", "Contratado (GWh)", "Faltó (GWh)", "Sobró (GWh)", "Costo relativo", "Meses cortos"]]
for (k, vol), f in tc.iterrows():
    t3.append([f"{k}:1", vol.capitalize().replace("%", " %"), num(f["contratado 2024 (GWh)"]), num(f["faltó (GWh)"]), num(f["sobró (GWh)"]),
               num(f["costo relativo"]), str(int(f["meses cortos"]))])
nota_t3 = (f"Consumo real de 2024: {num(ns['real24'].sum())} GWh. Costo relativo = (c<sub>u</sub>/c<sub>o</sub>) × faltante + sobrante, "
           "en GWh-equivalentes del costo de sobrar. Los cuantiles se calculan con exp(μ + z·σ), sin corrección de sesgo. Fuente: anexo, §3.")

plan = ns["plan"]
meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
t4 = [["Mes 2025", "Media corregida", "IC 95 % inf.", "IC 95 % sup.", "Cuantil 67 %", "Cuantil 75 % (a contratar)", "Cuantil 80 %"]]
for m, (_, f) in zip(meses, plan.iterrows()):
    t4.append([m] + [num(v) for v in f.to_numpy()])
t4.append(["<b>Total</b>", f"<b>{num(plan['media corregida'].sum())}</b>", "—", "—", num(plan["cuantil 67 %"].sum()),
           f"<b>{num(plan['cuantil 75 % (a contratar)'].sum())}</b>", num(plan["cuantil 80 %"].sum())])
nota_t4 = ("Volúmenes en GWh. Modelo reestimado con 2015-2024, sin efecto covid en 2025. El cuantil 75 % corresponde a "
           "c<sub>u</sub> = 3·c<sub>o</sub>, el valor central del rango de 2 a 4 veces del caso. Fuente: anexo, §3.")

ts = ns["tabla_sens"]
t5 = [["k = c<sub>u</sub>/c<sub>o</sub>", "q*", "Volumen 2025 con q* (GWh)", "Sobre la media", "Sobrecosto esperado del 75 %",
       "Sobrecosto esperado de la media", "Ahorro 2024 de q* frente a la media"]]
for k, f in ts.iterrows():
    t5.append([num(k, 1).replace(",0", ""), f"{num(f['q* (%)'], 1)} %", num(f["vol. 2025 q*"]),
               f"{'+' if f['sobre media (%)'] >= 0 else ''}{num(f['sobre media (%)'])} %",
               f"{num(f['sobrecosto 75 % (%)'])} %", f"{num(f['sobrecosto media (%)'])} %", f"{num(f['ahorro 2024 (%)'])} %"])
filas_rango = [i + 1 for i, k in enumerate(ts.index) if 2 <= k <= 4]
nota_t5 = (f"q* = k/(k + 1). Sobrecosto esperado: costo esperado de 2025 según la distribución predictiva del modelo, "
           f"respecto de contratar q*. Ahorro 2024: costo real de la prueba retrospectiva con q* frente a contratar la media. "
           f"En gris, el rango de 2 a 4 del caso. Con k &lt; {num(ns['k_cruce'], 2)}, contratar la media tiene menor costo esperado "
           f"que contratar el 75 %. Fuente: anexo, §3.1.")

# ------------------------------------------------------------------------------------------------
# 4. Textos literales del autor
# ------------------------------------------------------------------------------------------------
notas = celda("## 4. Notas para el informe")
partes = re.split(r"\*\*\d\. [^*]+:\*\*", notas)
assert len(partes) == 4, "la §4 debe tener los bloques 1, 2 y 3"
bloque1, bloque2, bloque3 = (bloques(p) for p in partes[1:])
bloque2 = [(t, re.sub(r"^\*\*Tabla 2 \(§2\)\.\*\*\s*", "", c)) for t, c in bloque2]    # referencia interna al notebook

lectura = bloques(celda("**Lectura de la evaluación 2023 y 2024"))
porque = celda("**¿Por qué se eligió el modelo final?**")
porque_txt, cadena_txt = porque.split("**Cadena de evidencia**")
porque_b = bloques(porque_txt)[1:]
cadena_b = bloques(cadena_txt)
volumen = bloques(celda("**Del pronóstico al volumen a contratar"))
i_plan = next(i for i, (t, c) in enumerate(volumen) if c == "**Plan 2025**")
i_lim = next(i for i, (t, c) in enumerate(volumen) if c == "**Limitaciones**")
sens = bloques(celda("**Principales conclusiones de la Tabla 5"))
refs = [l for l in celda("### Referencias").splitlines()[1:] if l.strip()]
decl = celda("## Declaración de uso de asistentes de IA")
filas_decl = [[c.strip() for c in l.strip().strip("|").split("|")] for l in decl.splitlines() if l.startswith("| ") and "---" not in l]

# ------------------------------------------------------------------------------------------------
# 5. Documento
# ------------------------------------------------------------------------------------------------
ANCHO = letter[0] - 2 * 2.3 * cm
hoy = date.today()
meses_largos = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
fecha = f"{hoy.day} de {meses_largos[hoy.month - 1]} de {hoy.year}"

h = [Paragraph("Informe ejecutivo: consumo eléctrico comercial de DEL", st["titulo"]),
     Paragraph("Pronóstico mensual para 2025 y volumen de energía a contratar", ParagraphStyle("sub", parent=st["h2"], textColor=GRIS, spaceBefore=0)),
     Paragraph(f"Universidad Andrés Bello · Magíster en Ciencia de Datos · MCDI505 Análisis de Series de Tiempo · Sumativa 4 (Semana 4)<br/>"
               f"Estudiante: Roberto Moncada · {fecha} · Archivo: mcdi505_s4rmoncada · "
               f"Anexo: mcdi505_s4rmoncada.ipynb (plantilla de evaluación 2024 ejecutada)", st["meta"]),
     Spacer(1, 4),
     Table([[""]], colWidths=[ANCHO], rowHeights=[1.2], style=[("LINEABOVE", (0, 0), (-1, 0), 1.2, GRANATE)])]

h += [Paragraph("1. Problema, datos, metodología y solución propuesta", st["h1"])]
h += poner(bloque1)
h += [figura(1, "Consumo eléctrico comercial de DEL: pronóstico 2024 frente a lo observado", 0, 16.5,
             "Consumo mensual observado (2021-2024), pronóstico de 2024 del modelo final reestimado con datos hasta diciembre de 2023 "
             "e intervalo de predicción al 95 %. La línea punteada vertical marca el inicio del periodo de prueba. Fuente: anexo, §1.")]
h += [Paragraph("Evaluación en validación 2023 y en prueba 2024", st["h2"])]
h += poner(lectura, omitir_primero=True)
h += [tabla(1, "Modelo final frente al naive estacional en la validación 2023 y la prueba 2024", t1,
            [2.8 * cm, 3.4 * cm, 2.2 * cm, 2.2 * cm, 1.8 * cm, 3.0 * cm], nota_t1, alinear_der_desde=2)]

h += [Paragraph("2. Sustento técnico del modelo seleccionado", st["h1"])]
h += poner(bloque2)
h += [Paragraph("¿Por qué se eligió el modelo final?", st["h2"])]
h += poner(porque_b)
h += [tabla(2, "Modelo final, alternativas descartadas en las semanas 2 y 3 y naive estacional", t2,
            [4.4 * cm, 3.5 * cm, 1.15 * cm, 1.15 * cm, 1.15 * cm, 1.15 * cm, 1.15 * cm, 1.15 * cm, 1.3 * cm], nota_t2,
            cabeceras=2, alinear_der_desde=2,
            extra=[("SPAN", (2, 1), (4, 1)), ("SPAN", (5, 1), (7, 1)), ("LINEBELOW", (0, 1), (-1, 1), 0.6, colors.black),
                   ("BACKGROUND", (0, 2), (-1, 2), colors.HexColor("#f6e6eb"))])]
h += [Paragraph("Cadena de evidencia", st["h2"])]
h += poner(cadena_b)

h += [Paragraph("3. Conclusiones y recomendaciones", st["h1"])]
h += [Paragraph("Recomendación principal y limitación más importante", st["h2"])]
h += poner(bloque3)
h += [Paragraph("Del pronóstico al volumen a contratar", st["h2"])]
h += poner(volumen[1:i_plan])
h += [tabla(3, "Prueba retrospectiva 2024: costo de contratar la media o el cuantil óptimo", t3,
            [1.5 * cm, 3.2 * cm, 2.6 * cm, 2.0 * cm, 2.0 * cm, 2.3 * cm, 2.0 * cm], nota_t3, alinear_der_desde=2,
            extra=[("BACKGROUND", (0, 3), (-1, 4), colors.HexColor("#f6e6eb"))])]
h += [Paragraph("Plan 2025", st["h2"])]
h += poner(volumen[i_plan + 1:i_lim])
h += [tabla(4, "Plan de contratación 2025 por mes", t4,
            [1.9 * cm, 2.4 * cm, 2.2 * cm, 2.2 * cm, 2.2 * cm, 3.2 * cm, 2.2 * cm], nota_t4,
            extra=[("BACKGROUND", (5, 1), (5, -1), colors.HexColor("#f6e6eb")), ("LINEABOVE", (0, -1), (-1, -1), 0.6, colors.black)])]
h += [Paragraph("Sensibilidad del cuantil a la razón de costos", st["h2"])]
h += [tabla(5, "Sensibilidad del volumen a contratar y de su costo a la razón de costos", t5,
            [2.0 * cm, 1.6 * cm, 2.6 * cm, 1.9 * cm, 2.6 * cm, 2.6 * cm, 2.8 * cm], nota_t5,
            extra=[("BACKGROUND", (0, filas_rango[0]), (-1, filas_rango[-1]), colors.HexColor("#eeeeee"))])]
h += [figura(2, "Volumen 2025 y sobrecosto esperado según la razón de costos", 1, 16.5,
             "Izquierda: volumen total de 2025 con el cuantil óptimo q* = k/(k + 1) y con la media corregida. Derecha: sobrecosto "
             "esperado de fijar el cuantil 75 % o la media cuando la razón real es k. Área gris: rango de 2 a 4 del caso; línea "
             "punteada: k = 3. Fuente: anexo, §3.1.")]
h += poner(sens)
h += [Paragraph("Limitaciones", st["h2"])]
h += poner(volumen[i_lim + 1:])

h += [Paragraph("Referencias", st["h1"])]
h += [Paragraph(md_a_rl(r), st["ref"]) for r in refs]

h += [Paragraph("Declaración de uso de IA", st["h1"])]
td = Table([[Paragraph(md_a_rl(a), st["th"]), Paragraph(md_a_rl(b), st["td"])] for a, b in filas_decl[1:]],
           colWidths=[4.2 * cm, ANCHO - 4.2 * cm], hAlign="LEFT")
td.setStyle(TableStyle([("LINEABOVE", (0, 0), (-1, 0), 0.9, colors.black), ("LINEBELOW", (0, -1), (-1, -1), 0.9, colors.black),
                        ("LINEBELOW", (0, 0), (-1, -2), 0.3, colors.HexColor("#bbbbbb")), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                        ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
h += [td]


def pie(canvas, doc):
    canvas.saveState()
    canvas.setFont("Cal", 8.5)
    canvas.setFillColor(GRIS)
    canvas.drawString(2.3 * cm, 1.3 * cm, "mcdi505_s4rmoncada · Informe ejecutivo · Sumativa 4")
    canvas.drawRightString(letter[0] - 2.3 * cm, 1.3 * cm, f"{doc.page}")
    canvas.restoreState()


doc = SimpleDocTemplate(SALIDA, pagesize=letter, leftMargin=2.3 * cm, rightMargin=2.3 * cm, topMargin=2.0 * cm, bottomMargin=2.0 * cm,
                        title="mcdi505_s4rmoncada · Informe ejecutivo", author="Roberto Moncada",
                        subject="MCDI505 · Sumativa 4 · Informe ejecutivo del proyecto")
doc.build(h, onFirstPage=pie, onLaterPages=pie)
print("PDF:", SALIDA)
