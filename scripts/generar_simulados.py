"""Genera la plantilla del CSV y las 60 filas simuladas de la encuesta.
Los IDs son secuenciales: R001-R020 para las reales, R021-R080 para las simuladas.

Uso (desde la raíz del repositorio):  python scripts/generar_simulados.py
Salidas:
  plantillas/encuesta_plantilla.csv  -> solo encabezados, para pegar las 20 respuestas reales
  plantillas/encuesta_simulados.csv  -> 60 filas simuladas (origen = simulada)
Después, junten las filas reales y simuladas en un solo plantillas/encuesta_respuestas.csv.
"""
import os
import numpy as np
import pandas as pd

SEMILLA = 42
CARPETA = "plantillas"   # se crea en la raíz del repositorio si no existe
os.makedirs(CARPETA, exist_ok=True)
N_SIMULADOS = 60

COLUMNAS = (
    ["respuesta_id", "origen", "p1_edad", "p2_prob_inscripcion", "p3_frecuencia", "p4_gasto"]
    + ["p5_atencion", "p5_precios", "p5_variedad", "p5_limpieza", "p5_comodidad"]
    + ["p6_abarrotes", "p6_lacteos", "p6_carnicos", "p6_frutas_vegetales",
       "p6_bebidas", "p6_limpieza_aseo", "p6_cuidado_personal", "p6_otro"]
    + ["p7_beneficio", "p7_otro_texto"]
    + ["p8_descuentos", "p8_puntos", "p8_2x1", "p8_cupones",
       "p8_entrega_domicilio", "p8_ofertas_personalizadas"]
)

BENEFICIOS = ["descuentos_directos", "puntos", "2x1", "cupones", "otro", "ninguno"]

# Plantilla vacía (solo encabezados) para las respuestas reales
pd.DataFrame(columns=COLUMNAS).to_csv(f"{CARPETA}/encuesta_reales.csv", index=False)

# Filas simuladas
rng = np.random.default_rng(SEMILLA)
n = N_SIMULADOS
datos = {
    "respuesta_id": [f"R{i:03d}" for i in range(21, 21 + n)],
    "origen": ["simulada"] * n,
    "p1_edad": rng.integers(1, 7, n),
    "p2_prob_inscripcion": rng.integers(1, 6, n),
    "p3_frecuencia": rng.integers(1, 5, n),   # 1-4: quien marca 0 queda fuera de la población
    "p4_gasto": rng.integers(1, 6, n),
}
for col in ["p5_atencion", "p5_precios", "p5_variedad", "p5_limpieza", "p5_comodidad"]:
    datos[col] = rng.integers(1, 6, n)
for col in ["p6_abarrotes", "p6_lacteos", "p6_carnicos", "p6_frutas_vegetales",
            "p6_bebidas", "p6_limpieza_aseo", "p6_cuidado_personal", "p6_otro"]:
    datos[col] = rng.integers(0, 2, n)
datos["p7_beneficio"] = rng.choice(BENEFICIOS, n)
datos["p7_otro_texto"] = [""] * n
for col in ["p8_descuentos", "p8_puntos", "p8_2x1", "p8_cupones",
            "p8_entrega_domicilio", "p8_ofertas_personalizadas"]:
    datos[col] = rng.integers(1, 6, n)

pd.DataFrame(datos, columns=COLUMNAS).to_csv(f"{CARPETA}/encuesta_simulados.csv", index=False)
print(f"Listo: archivos guardados en {CARPETA}/")