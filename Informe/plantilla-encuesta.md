# Plantilla de diseño — Encuesta de satisfacción (hito 1)

**Equipo:** 7 · **Integrantes:** Jeriel López, Alejandro-Guanocunga  · <br>**Fecha:** 28/10/2026 <br>
**Repositorio (fork):** github.com/alejandro-guanocunga/IDSD422-lab3-diseno-encuesta
<br>**Enfoque del equipo (aprobado en clase):** ___

Completa cada sección. Usa commits por sección; la historia del repositorio se revisa.

> **Formato del entregable:** exporta esta plantilla completada a PDF, con el enlace de tu fork en la carátula, y guarda el PDF en `informes/` del fork. Entrega el PDF y el enlace del fork en el aula virtual.

## 1. Objetivos de la encuesta

### Objetivo Principal:
Identificar qué beneficios y qué aspectos del servicio valoran más los clientes habituales de RetailAndina en Quito, para orientar el diseño de su programa de fidelización.

### Objetivo Secundario:
Aumentar la retención de clientes frecuentes en al menos 12% durante el primer trimestre de lanzamiento. Esa meta se evaluará después con los registros de compras de la empresa, no con esta encuesta.

## 2. Población objetivo

- Población: Personas de 18 años o más que realizan compras habituales de consumo en las tiendas y supermercados de RetailAndina S.A. En la ciudad de Quito al menos una vez al mes.

- Límites y justificación: Se restringe geográficamente a la ciudad de Quito urbano y a clientes mayores de edad con una frecuencia de compra mensual mínima, garantizando una población alcanzable para la recolección ágil de respuestas reales entre la red de contactos directos de los integrantes, asegurando además que conozcan la propuesta de valor de la cadena.


## 3. Método de muestreo


- **Método:** Muestreo por conveniencia declarada con referidos (contactos directos que cumplen el perfil de cliente en RetailAndina S.A.).

- **Tamaño y justificación:** Se empleara un tamaño de muestra de 80 encuestados, siendo 20 individuos  (10 por integrante) más 60 respuestas simuladas con código, totalizando 80 filas en el dataset final (dentro del rango exigido de 60–100 filas) para asegurar factibilidad en el levantamiento y suficiente potencia estadística en las auditorías.

- **Cómo se seleccionarán los participantes:** Se seleccionará a familiares, amigos y compañeros de universidad que compran habitualmente en las sucursales de RetailAndina en Quito, enviándoles el formulario digital por WhatsApp y correo.

- **Equivalente en código (Python o R):** La línea que implementa tu método sobre un CSV de clientes (aleatorio simple, estratificado o conveniencia) con el resultado de una corrida con semilla, y una frase sobre por qué tu método (y no la conveniencia) justifica el hito.


## 4. Cuestionario 



| # | Pregunta | Tipo de variable | Dtype al cargar | Opciones / escala |
|---|----------|------------------|-----------------|-------------------|
| 1 | ¿En qué rango de edad se encuentra? | Categórica ordinal | int64 | 1) 18–20<br>2) 21–30<br>3) 31–40<br>4) 41–50<br>5) 51–60<br>6) Mayor a 60 años |
| 2 | ¿Qué tan probable es que se inscriba en un programa de fidelización de RetailAndina? | Categórica ordinal (escala Likert) | int64 | 1) Nada probable<br>2) Poco probable<br>3) Neutral<br>4) Probable<br>5) Muy probable |
| 3 | Durante el mes anterior, ¿cuántas veces realizó compras en un supermercado? | Categórica ordinal | int64 | 0) Ninguna<br>1) 1 a 2 veces<br>2) 3 a 4 veces<br>3) 5 a 6 veces<br>4) Más de 6 |
| 4 | ¿En qué rango se ubica su gasto mensual aproximado en compras de supermercado? | Categórica ordinal | int64 | 1) Menos de 100 USD<br>2) 100 a 250 USD<br>3) 251 a 500 USD<br>4) Más de 500 USD<br>5) Prefiero no responder |
| 5 | ¿Qué tan satisfecho o satisfecha está con los siguientes aspectos de RetailAndina? (atención del personal, precios, variedad de productos, limpieza y comodidad) | Categórica ordinal (escala Likert) | int64 (una columna por aspecto) | 1) Muy insatisfecho<br>2) Insatisfecho<br>3) Ni satisfecho ni insatisfecho<br>4) Satisfecho<br>5) Muy satisfecho |
| 6 | ¿Qué tipos de productos compra con más frecuencia? Puede marcar más de uno. | Categórica nominal (selección múltiple) | int64 0/1 (una columna por opción) | Abarrotes<br>Lácteos<br>Cárnicos<br>Frutas y vegetales<br>Bebidas<br>Limpieza y aseo<br>Cuidado personal<br>Otro |
| 7 | ¿Qué tipo de beneficio valoraría más en un supermercado? | Categórica nominal | object / str | 1) Descuentos directos<br>2) Acumulación de puntos<br>3) Productos 2x1<br>4) Cupones de regalo<br>5) Otro (especifique)<br>6) Ninguno |
| 8 | ¿Qué tan importante es cada uno de estos beneficios para usted? (descuentos directos, acumulación de puntos, productos 2x1, cupones de regalo, entregas a domicilio, ofertas personalizadas) | Categórica ordinal (escala Likert) | int64 (una columna por beneficio) | 1) Nada importante<br>2) Poco importante<br>3) Neutral<br>4) Importante<br>5) Muy importante |



## 5. Análisis de sesgos

| Sesgo potencial | Mitigación |
|---|---|
|Sesgo de selección por conveniencia: Al recolectar datos en la red cercana (amigos y familiares), se subrepresenta a clientes mayores o de otros segmentos que compran habitualmente en RetailAndina. | Declarar el canal en la metodología, diversificar el envío del formulario a distintos rangos de edad y complementar el dataset con filas simuladas balanceadas para calibrar la representatividad. |
| Sesgo de respuesta: Los encuestados podrían responder lo que consideran socialmente aceptable en lugar de expresar sus preferencias reales. | Garantizar el anonimato de las respuestas y utilizar preguntas neutrales que no sugieran una respuesta deseada. |

## 6. Confidencialidad (RA3)

- **Datos personales que se piden y por qué:**
Se solicitan únicamente dos datos personales: el rango de edad y el género. Ambos son necesarios para realizar cruces de variables que den sentido al análisis: comparar la proporción de hombres y mujeres según el tipo de producto que compran con mayor frecuencia, y determinar si algún grupo etario prefiere un tipo de beneficio en particular (descuentos directos, puntos, 2x1 o cupones). Esta información permite segmentar los resultados y orientar el diseño del programa de fidelización de RetailAndina. No se solicitan nombre, correo, teléfono, cédula ni dirección, y la edad se recoge por rangos y no como valor exacto, para reducir la posibilidad de identificar a una persona.

- **Plan de anonimización (qué se quita o codifica antes de compartir):**
  - El formulario no recoge datos de identificación directa (nombre, correo, teléfono, cédula). Si el envío por WhatsApp o correo deja algún rastro, no se incluye en el dataset.
  - A cada respuesta se le asigna un ID numérico secuencial (R001, R002, …) que no guarda relación con la identidad del encuestado.
  - Las variables categóricas (edad, género, frecuencia, producto y beneficio) se codifican con números, según la tabla del cuestionario.
  - Las respuestas abiertas, como la de gasto, se revisan antes de compartir, para eliminar cualquier dato que permita identificar a alguien.
  - La lista de contactos a quienes se envió el formulario se mantiene fuera del repositorio y no se comparte con el dataset.
  - Solo se comparte el dataset anonimizado (20 respuestas reales y 60 simuladas) y se reportan resultados agregados, no respuestas individuales.
