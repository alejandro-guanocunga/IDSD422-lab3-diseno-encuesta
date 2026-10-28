# Plantilla de diseño — Encuesta de satisfacción (hito 1)

**Equipo:** ___ · **Integrantes:** ___ · **Fecha:** 20/10/2026
**Repositorio (fork):** github.com/[usuario]/IDSD422-lab2-diseno-encuesta
**Enfoque del equipo (aprobado en clase):** ___

Completa cada sección. Usa commits por sección; la historia del repositorio se revisa.

> **Formato del entregable:** exporta esta plantilla completada a PDF, con el enlace de tu fork en la carátula, y guarda el PDF en `informes/` del fork. Entrega el PDF y el enlace del fork en el aula virtual.

## 1. Objetivo de la encuesta

Apoyar la decisión de gerencia de RetailAndina S.A. para diseñar el esquema de beneficios y recompensas de su nuevo programa de fidelización, con la meta de incrementar la tasa de retención de clientes frecuentes en al menos un 12% durante el primer trimestre de lanzamiento.


## 2. Población objetivo

- Población: Personas de 18 años o más que realizan compras habituales de consumo masivo en las tiendas y supermercados de RetailAndina S.A. en la ciudad de Quito al menos una vez al mes.
- Límites y justificación: Se restringe geográficamente a la ciudad de Quito urbano y a clientes mayores de edad con una frecuencia de compra mensual mínima, garantizando una población alcanzable para la recolección ágil de respuestas reales entre la red de contactos directos de los integrantes, asegurando además que conozcan la propuesta de valor de la cadena.


## 3. Método de muestreo

*Elige aleatorio simple, estratificado o conveniencia y justifica. Meta: 15–30 respuestas reales (3–6 por integrante); opcional: relleno simulado hasta 60–100 filas marcadas con la columna `origen`.*

- Método: Muestreo por conveniencia declarada con referidos (contactos directos que cumplen el perfil de cliente en RetailAndina S.A.).
- Tamaño y justificación: 25 respuestas reales (5 por integrante) más 55 respuestas simuladas con código, totalizando 80 filas en el dataset final (dentro del rango exigido de 60–100 filas) para asegurar factibilidad en el levantamiento y suficiente potencia estadística en las auditorías.
- Cómo se seleccionarán los participantes: Se seleccionará a familiares, amigos y compañeros de universidad que compran habitualmente en las sucursales de RetailAndina en Quito, enviándoles el formulario digital por WhatsApp y correo.
- **Equivalente en código (Python o R):** la línea que implementa tu método sobre un CSV de clientes (aleatorio simple, estratificado o conveniencia) con el resultado de una corrida con semilla, y una frase sobre por qué tu método (y no la conveniencia) justifica el hito.
 




## 4. Cuestionario (5–10 preguntas)

*Preguntas neutras, específicas, una idea por pregunta, opciones exhaustivas y excluyentes.*

| # | Pregunta | Tipo de variable | Dtype al cargar | Opciones / escala |
|---|---|---|---|---|
| 1 | ¿Con qué frecuencia mensual realiza sus compras en RetailAndina S.A.? | Categórica ordinal | `int64` | 1: 1 a 2 veces al mes, 2: 3 a 4 veces al mes, 3: Más de 4 veces al mes |
| 2 | ¿Cuál es su gasto promedio aproximado por visita en la tienda? (USD) | Numérica continua | `float64` | Menos de $20, $20 a $50, Más de $50 |
| 3 | ¿Qué tan satisfecho está con los beneficios actuales de las tiendas RetailAndina? | Categórica ordinal | `int64` | Escala del 1 (Nada satisfecho) al 5 (Muy satisfecho) |
| 4 | ¿Qué tipo de beneficio valoraría más en el nuevo programa de fidelización? | Categórica nominal | `object` / `str` | 1: Descuentos directos, 2: Acumulación de puntos, 3: Productos 2x1, 4: Cupones de regalo |
| 5 | ¿Recomendaría el nuevo programa de fidelización a un familiar o amigo? | Categórica ordinal (Likert) | `int64` | Escala del 1 (Nada probable) al 10 (Muy probable) |

*Nota: la columna "tipo de variable" usa la clasificación del cap. 3 (numérica continua/discreta, categórica binaria/ordinal). "Dtype al cargar" es cómo crees que llegará la columna en `df.dtypes`/`str()` (`int64`, `float64`, `str`/`object` según la versión de pandas). Pista: el dtype es una pista, no la clasificación — una ordinal puede llegar como `int`.*

## 5. Análisis de sesgos

*Identifica 2 problemas potenciales de esta encuesta y su mitigación.*

| Sesgo potencial | Mitigación |
|---|---|
| 1. Sesgo de selección por conveniencia: Al recolectar datos en la red cercana (amigos y familiares), se subrepresenta a clientes mayores o de otros segmentos que compran habitualmente en RetailAndina. | Declarar el canal en la metodología, diversificar el envío del formulario a distintos rangos de edad y complementar el dataset con filas simuladas balanceadas para calibrar la representatividad. |

## 6. Confidencialidad (RA3)

- Datos personales que se piden y por qué:
- Plan de anonimización (qué se quita o codifica antes de compartir):

## 7. Verificación con herramientas (Python/R)

*Escribe `scripts/verificacion_encuesta.py` (o `.R`): debe cargar `plantillas/encuesta_respuestas.csv` y reportar los tipos de cada columna, los datos faltantes por columna y la distribución de `satisfaccion_general` y `recomendaria`. Incluye la salida y responde:*

- ¿Coinciden los tipos con tu predicción de la sección 4?
- ¿Cuántos datos faltantes hay por columna?

*Ejecuta el script sobre el CSV final (separa con un filtro de la columna `origen` las filas reales de las simuladas): ¿qué resultado delataría un sesgo de **no respuesta** y cuál un sesgo de **respuesta**? Escribe tu interpretación usando solo las respuestas reales.*
