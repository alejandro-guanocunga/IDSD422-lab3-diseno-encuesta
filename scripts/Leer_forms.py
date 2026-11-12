"""Convierte la exportación de Google Forms al formato de su CSV.

Uso (desde la raíz del repositorio):
    python scripts/leer_forms.py plantillas/respuestas_forms.csv

Entrada : CSV descargado de Google Forms (Respuestas > hoja de cálculo > Descargar CSV).
Salidas : plantillas/encuesta_reales.csv        (solo las respuestas reales, ya codificadas)
          plantillas/encuesta_respuestas.csv    (reales + simuladas, si existe encuesta_simulados.csv)

IMPORTANTE: las columnas se leen por POSICIÓN (orden del formulario), y las
opciones deben estar escritas exactamente como en el cuestionario.
Orden esperado tras 'Marca temporal': P1, P2, P3, P4, P5 (5 filas), P6, P7, P8 (6 filas).
"""
import sys
import pandas as pd

RUTA = sys.argv[1] if len(sys.argv) > 1 else "plantillas/respuestas_forms.csv"

COLUMNAS = (
    ["respuesta_id", "origen", "p1_edad", "p2_prob_inscripcion", "p3_frecuencia", "p4_gasto"]
    + ["p5_atencion", "p5_precios", "p5_variedad", "p5_limpieza", "p5_comodidad"]
    + ["p6_abarrotes", "p6_lacteos", "p6_carnicos", "p6_frutas_vegetales",
       "p6_bebidas", "p6_limpieza_aseo", "p6_cuidado_personal", "p6_otro"]
    + ["p7_beneficio", "p7_otro_texto"]
    + ["p8_descuentos", "p8_puntos", "p8_2x1", "p8_cupones",
       "p8_entrega_domicilio", "p8_ofertas_personalizadas"]
)

# --- Códigos (iguales a la tabla del cuestionario) ---
P1 = {"18–20": 1, "21–30": 2, "31–40": 3, "41–50": 4, "51–60": 5, "Mayor a 60 años": 6}
P3 = {"Ninguna": 0, "1 a 2 veces": 1, "3 a 4 veces": 2, "5 a 6 veces": 3, "Más de 6": 4}
P4 = {"Menos de 100 USD": 1, "100 a 250 USD": 2, "251 a 500 USD": 3,
      "Más de 500 USD": 4, "Prefiero no responder": 5}
P5 = {"Muy insatisfecho": 1, "Insatisfecho": 2, "Ni satisfecho ni insatisfecho": 3,
      "Satisfecho": 4, "Muy satisfecho": 5}
P8 = {"Nada importante": 1, "Poco importante": 2, "Neutral": 3, "Importante": 4,
      "Muy importante": 5}
P6 = {"Abarrotes": "p6_abarrotes", "Lácteos": "p6_lacteos", "Cárnicos": "p6_carnicos",
      "Frutas y vegetales": "p6_frutas_vegetales", "Bebidas": "p6_bebidas",
      "Limpieza y aseo": "p6_limpieza_aseo", "Cuidado personal": "p6_cuidado_personal"}
P7 = {"Descuentos directos": "descuentos_directos", "Acumulación de puntos": "puntos",
      "Productos 2x1": "2x1", "Cupones de regalo": "cupones", "Ninguno": "ninguno"}


def limpiar(x):
    """Quita espacios y unifica guiones (18-20 / 18—20 -> 18–20)."""
    return str(x).strip().replace("—", "–").replace("-", "–")


def codificar(serie, mapa, nombre, limpiar_guiones=False):
    base = serie.map(limpiar) if limpiar_guiones else serie.astype(str).str.strip()
    codigos = base.map(mapa)
    if codigos.isna().any():
        malos = sorted(set(base[codigos.isna()]))
        sys.exit(f"ERROR en {nombre}: opciones que no coinciden con el cuestionario: {malos}")
    return codigos.astype(int)


forms = pd.read_csv(RUTA)
datos = forms.iloc[:, 1:18]          # descarta 'Marca temporal' (anonimato)
if datos.shape[1] != 17:
    sys.exit(f"ERROR: se esperaban 17 columnas de respuestas y hay {datos.shape[1]}")
datos.columns = range(17)

out = pd.DataFrame()
out["origen"] = ["real"] * len(datos)
out["p1_edad"] = codificar(datos[0], P1, "P1", limpiar_guiones=True)
out["p2_prob_inscripcion"] = pd.to_numeric(datos[1]).astype(int)   # escala lineal: ya es número
out["p3_frecuencia"] = codificar(datos[2], P3, "P3")
out["p4_gasto"] = codificar(datos[3], P4, "P4")
for i, col in enumerate(["p5_atencion", "p5_precios", "p5_variedad", "p5_limpieza", "p5_comodidad"]):
    out[col] = codificar(datos[4 + i], P5, col)

# P6: casillas de verificación -> una columna 0/1 por opción; lo desconocido cuenta como 'otro'
marcadas = datos[9].fillna("").astype(str).apply(lambda t: [s.strip() for s in t.split(",") if s.strip()])
for etiqueta, col in P6.items():
    out[col] = marcadas.apply(lambda l, e=etiqueta: int(e in l))
out["p6_otro"] = marcadas.apply(lambda l: int(any(s not in P6 for s in l)))

# P7: lo que no es una opción conocida se trata como 'otro' y se guarda el texto
p7 = datos[10].astype(str).str.strip()
out["p7_beneficio"] = p7.map(P7).fillna("otro")
out["p7_otro_texto"] = p7.where(~p7.isin(P7.keys()), "")

for i, col in enumerate(["p8_descuentos", "p8_puntos", "p8_2x1", "p8_cupones",
                         "p8_entrega_domicilio", "p8_ofertas_personalizadas"]):
    out[col] = codificar(datos[11 + i], P8, col)

# Filtro de población: quien no compró el mes anterior (P3 = 0) queda fuera
fuera = (out["p3_frecuencia"] == 0).sum()
out = out[out["p3_frecuencia"] != 0].reset_index(drop=True)
if fuera:
    print(f"Se excluyeron {fuera} respuesta(s) con P3 = Ninguna (fuera de la población).")

out.insert(0, "respuesta_id", [f"R{i:03d}" for i in range(1, len(out) + 1)])
out[COLUMNAS].to_csv("plantillas/encuesta_reales.csv", index=False)
print(f"{len(out)} respuestas reales -> plantillas/encuesta_reales.csv")

# Unir con las simuladas (si existen) y renumerar los IDs en secuencia
try:
    sim = pd.read_csv("plantillas/encuesta_simulados.csv")
    todo = pd.concat([out[COLUMNAS], sim[COLUMNAS]], ignore_index=True)
    todo["respuesta_id"] = [f"R{i:03d}" for i in range(1, len(todo) + 1)]
    todo.to_csv("plantillas/encuesta_respuestas.csv", index=False)
    print(f"{len(todo)} filas en total -> plantillas/encuesta_respuestas.csv")
except FileNotFoundError:
    print("No se encontró plantillas/encuesta_simulados.csv; corre generar_simulados.py para unirlas.")