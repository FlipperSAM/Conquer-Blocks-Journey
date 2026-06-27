# Conquer-Blocks-Journey

## Tabla de Contenidos (Navegación interna)
* ## Fundamentos de Python
Documentación técnica sobre las bases del lenguaje y manipulación de datos.
*   **[Ver notas](./python/docs/NOTAS_STRINGS_BIENVENIDA.md):** Explicación detallada de métodos como `.upper()`, `.lower()` y el uso de f-strings.

*   **[Principios SOLID](./solid/NOTAS_SOLID.md)**  

## Mis Proyectos
Aquí puedes encontrar los ejercicios prácticos que voy desarrollando durante el máster:

*   **[Script Bienvenida](./python/scripts/mensaje_bienvenida.py):** Un ejercicio de normalización de datos, limpieza de strings y validación de usuarios con buenas prácticas de Python.
*   **[Proyecto: Calculadora de Ahorros](./python/scripts/calculadora_ahorros.py):** Un sistema financiero completo que proyecta ahorros anuales y analiza la viabilidad económica bajo cambios en la jornada laboral y reducción de gastos.
*   **[Proyecto: Casa de Cambios](./python/scripts/casa_cambios.py):** Un script de lógica financiera que aplica operadores aritméticos, cálculo de tasas de gestión (porcentajes) y formateo de precisión decimal para el manejo de divisas.
*   **[Proyecto: Comisión de carros](./python/scripts/comisiones_carros.py):** Un script de gestión de ventas que calcula comisiones variables según el modelo de vehículo y el volumen de ventas mensual.
*   **[Proyecto: Repetir Caracteres](./python/scripts/duplicador_caracteres.py):** Un script que demuestra el uso de bucles para la transformación de datos y la concatenación dinámica de strings.
*   **[Script Bienvenida](./python/scripts/mensaje_bienvenida.py):** Un ejercicio de procesamiento avanzado de strings que implementa normalización de datos mediante métodos nativos (`.upper()`, `.lower()`, `.title()`), limpieza de caracteres especiales y uso de f-strings.
*   **[Proyecto: Olimpiadas Skeleton](./python/scripts/olimpiadas_skeleton.py):** Un script avanzado de conversión de unidades de tiempo y cálculo de velocidad media aplicado a resultados olímpicos.
*   **[Proyecto: Protección de Tarjeta](./python/scripts/proteccion_tarjeta.py):** Un script de seguridad que aplica técnicas de enmascaramiento de datos (Data Masking) para ocultar información sensible.
*   **[Proyecto: Reordenando Números](./python/scripts/reordenando_numeros.py):** Un script que descompone números en sus componentes individuales e implementa la inversión de secuencias mediante slicing avanzado.
*   **[Proyecto: Cuenta de Restaurante](./python/scripts/restaurante_cuenta.py):** Un sistema de facturación que utiliza diccionarios para gestionar un menú y generar un ticket de venta detallado.
*   **[Análisis: Lógica Condicional](./python/docs/NOTAS_CONDICIONALES_PRO.md):** Resumen de investigación sobre estructuras de decisión y operadores lógicos.
*   **[Script: Test de Lógica](./python/scripts/test_condicionales_pro.py):** Implementación práctica de comparaciones y operadores booleanos.
*   **[Proyecto: Gestión de Usuarios IF](./python/scripts/gestion_usuarios_if.py):** Un script de autenticación básica que utiliza condicionales para dar bienvenidas personalizadas tras normalizar la entrada del usuario.
*   **[Proyecto: Becas Estudiantes](./python/scripts/becas_estudiantes.py):** Un script de validación que utiliza operadores lógicos y comparaciones de rango para determinar la elegibilidad de becas académicas.
*   **[Proyecto: Declaración de la Renta](./python/scripts/declaracion_renta.py):** Un simulador tributario que implementa lógica de filtros previos (edad/ingresos) y cálculo de tramos impositivos mediante condicionales anidados.
*   **[Proyecto: Hamburguesería Online](./python/scripts/hamburgueseria_online.py):** Sistema de pedidos interactivo con menús dinámicos que cambian según la elección del usuario, aplicando normalización de entradas.
*   **[Proyecto: Gestión de Inventario](./python/scripts/gestion_inventario.py):** Una aplicación práctica de estructuras de datos que implementa la manipulación dinámica de listas (CRUD básico).
*   **[Proyecto: Peluqueria](./python/scripts/gestion_listas_peluqueria.py):**  Sistema de gestión de flujo de clientes que implementa lógica de colas **FIFO** (First-In-First-Out) y procesamiento de datos con **List Comprehensions**. Incluye un motor de estadística rápida para el cierre de caja diario y segmentación de agenda mediante **Slicing** avanzado.


---
## Teoria

#  Dominio de la Terminal y Linux

En el desarrollo de software moderno, la terminal no es solo una herramienta, es el entorno de trabajo principal. Este documento resume los comandos esenciales que utilizo para gestionar proyectos y sistemas de archivos de forma eficiente.

---

## Gestión de Archivos y Navegación

| Comando | Descripción | Uso Profesional |
| :--- | :--- | :--- |
| `pwd` | **Print Working Directory** | Confirmar en qué carpeta estoy antes de ejecutar un comando crítico. |
| `ls -la` | **Listar todo** | Ver archivos ocultos (como `.env` o `.git`) y permisos de usuario. |
| `cd ..` | **Change Directory** | Navegar hacia atrás en la estructura de carpetas. |
| `mkdir -p` | **Make Directory** | Crear rutas complejas de una sola vez (ej. `mkdir -p src/components`). |
| `touch` | **Crear archivo** | Generar archivos de código (`.py`, `.js`) sin salir de la terminal. |

---

## Manipulación y Visualización de Datos

| Comando | Descripción | Uso Profesional |
| :--- | :--- | :--- |
| `cat / head / tail` | **Visualización de contenido** | Lectura rápida de logs de errores o previsualización de scripts sin abrir editores de texto. |
| `mv` | **Move / Rename** | Traslado de archivos a directorios específicos o cambio de nombre de módulos y paquetes. |
| `cp -r` | **Copy Recursive** | Duplicación de directorios completos para la creación de respaldos locales o clonación de entornos. |
| `rm -rf` | **Remove Recursive Force** | Eliminación definitiva de directorios de dependencias o archivos temporales de forma recursiva. |

---

## Comandos de Sistema y Utilidades

| Comando | Descripción | Uso Profesional |
| :--- | :--- | :--- |
| `sudo` | **Superuser Do** | Ejecución de tareas con privilegios administrativos necesarias para la configuración del sistema. |
| `grep` | **Global Regular Expression** | Búsqueda y filtrado de cadenas de texto específicas dentro de archivos o salidas de comandos. |
| `history` | **Command History** | Consulta de secuencias de comandos ejecutadas previamente para optimizar el flujo de trabajo. |
| `clear` | **Clear Screen** | Limpieza de la interfaz de la terminal para mantener el orden visual en el área de trabajo. |

---

## Permisos y Gestión de Flujos

| Comando | Descripción | Uso Profesional |
| :--- | :--- | :--- |
| `chmod` | **Change Mode** | Gestión de permisos de lectura, escritura y ejecución para asegurar scripts de backend. |
| `chown` | **Change Owner** | Cambio de propiedad de archivos y directorios en entornos de servidor. |
| `>` / `>>` | **Redireccionamiento** | Envío de la salida de un comando a un archivo (creación de archivos de log dinámicos). |
| `pipe (\|)` | **Tubería** | Conexión de comandos donde la salida de uno es la entrada del siguiente (automatización). |

---
> "Un buen desarrollador rara vez despega las manos del teclado." 
> *Notas de aprendizaje en Conquer Blocks enfocadas en estándares Linux.*


---
# Python

# Análisis Técnico: Fundamentos y Aplicación en Python

Este documento detalla la base teórica y práctica asimilada durante el primer bloque del **Máster en Conquer Blocks**, vinculando cada concepto con los proyectos reales desarrollados en este repositorio.

---

# Teoría Aplicada a mis Proyectos

### 1. Nomenclatura y Convenciones

| Elemento | Definición y Uso |
| :--- | :--- |
| **Variables** (`snake_case`) | Almacenan datos que el programa modificará. Ejemplo: `ingreso_hora`, `nombre_usuario`. |
| **Constantes** (`UPPER_CASE`) | Valores fijos que no cambian (estándar PEP 8). Ejemplo: `TASA_CAMBIO`. |

**Nota de estudio:** Implementé el estándar *Snake Case* "guiones_bajos" para mantener la legibilidad y diferencié claramente entre datos dinámicos y valores estáticos.

---

### 2. Strings y sus funciones/métodos


| Contexto | Detalle de Aplicación |
| :--- | :--- |
| **En mis proyectos** | Aplicado en el script de Protección de Tarjeta y el de Bienvenida. |
| **Estudio** | Uso de `.lower()`, `.upper()`, `.title()` para formateo, `.replace()` para limpieza de datos y **Slicing** `[-4:]` para seguridad de tarjetas. |

**Nota de estudio:** Aprendí a manipular cadenas de texto para normalizar entradas de usuario y apliqué técnicas de segmentación (slicing) para manejar información sensible de forma segura.

---

### 3. Números y operaciones aritméticas


| Contexto | Detalle de Aplicación |
| :--- | :--- |
| **En mis proyectos** | La Casa de Cambios y las Olimpiadas. |
| **Estudio** | Uso de **`*`** (multiplicación), **`/`** (división) y **`-`** (resta). Aplicación de lógica de porcentajes (comisiones) y conversiones físicas (velocidad). |

**Nota de estudio:** Aprendí a utilizar operadores aritméticos para resolver cálculos lógicos y matemáticos fundamentales dentro de un flujo de programa.

---

### 4. Combinar números y strings


| Contexto | Detalle de Aplicación |
| :--- | :--- |
| **En mis proyectos** | Aplicado en todos los **`print()`** finales de los proyectos desarrollados. |
| **Estudio** | Dominio de las **`f-strings`** `(f"Hola {nombre}, tienes {ahorro}€")`. Técnica profesional para integrar variables sin errores de tipo de dato. |

**Nota de estudio:** Las f-strings facilitan la legibilidad del código y evitan errores de concatenación comunes al mezclar tipos de datos distintos.

---

### 5. Leer valores de entrada


| Contexto | Detalle de Aplicación |
| :--- | :--- |
| **En mis proyectos** | Uso constante del comando **`input()`** para interactuar con el usuario. |
| **Estudio** | Captura de datos externos. Comprendí que todo valor recibido por esta vía es tratado inicialmente como un String (cadena de texto). |

**Nota de estudio:** El comando input es el pilar de la interactividad, permitiendo que el software responda a datos dinámicos proporcionados por el usuario.

---

### 6. Conversión entre tipos de datos (Casting)


| Contexto | Detalle de Aplicación |
| :--- | :--- |
| **En mis proyectos** | Calculadora de Ahorros y Olimpiadas. |
| **Estudio** | Uso de **`float()`** para valores monetarios e **`int()`** para medidas de tiempo. Transformación de entradas de texto en datos operables. |

**Nota de estudio:** El casting es un proceso crítico en ingeniería para asegurar que los datos tengan el formato correcto antes de realizar operaciones matemáticas.

---

### 7. Uso de los comentarios


| Contexto | Detalle de Aplicación |
| :--- | :--- |
| **En mis proyectos** | Encabezados con **`"""`** (Docstrings) y explicaciones técnicas con **`#`**. |
| **Estudio** | Documentación del "qué" y el "por qué". Práctica esencial para asegurar que el backend sea comprensible y mantenible en entornos colaborativos. |

**Nota de estudio:** Un código bien comentado refleja profesionalismo y reduce la deuda técnica, facilitando la escalabilidad y el mantenimiento del proyecto.

---

### 8. Listas e Iteración Avanzada



| Contexto | Detalle de Aplicación |
| :--- | :--- |
| **En mis proyectos** | Software de gestión de turnos **IA Peluqueria**. |
| **Estudio** | Uso de `.pop(0)` para **FIFO**, `.enumerate()` para menús, **Slicing** para segmentar agendas y **List Comprehensions** para filtros rápidos. |

**Nota de estudio:** Comprendí cómo las estructuras de datos y los bucles permiten automatizar la lógica de un negocio real, permitiendo que el sistema tome decisiones basadas en el estado de la lista.

---

*Este análisis certifica mi capacidad para transformar conceptos teóricos en soluciones de código escalables y profesionales.*

# Lógica de Control: Test Condicionales y Expresiones Booleanas

En este módulo del máster de **Conquer Blocks**, profundizo en la capacidad del software para evaluar situaciones y tomar decisiones basadas en valores booleanos (**True** / **False**).

---

## 1. Asignación vs. Comparación
*   **Asignación (`=`):** Se utiliza para asociar un valor a una variable.
    *   Ejemplo: `nombre_usuario = "Juan"`
*   **Comparación (`==`):** Evalúa si dos valores son iguales, devolviendo un booleano.
    *   Ejemplo: `nombre_usuario == "Juan"` (Resultado: `True`)

## 2. Operadores de Comparación

| Operador | Significado | Ejemplo |
| :--- | :--- | :--- |
| `==` | Igual a | `h == 10` |
| `!=` | Diferente de | `h != 10` |
| `>` | Mayor que | `h > 0` |
| `<` | Menor que | `h < 0` |
| `>=` | Mayor o igual que | `h >= 0` |
| `<=` | Menor o igual que | `h <= 0` |

## 3. Testeos Condicionales Avanzados
*   **Case Sensitivity:** Las comparaciones de strings son sensibles a mayúsculas. Para una comparación profesional, usamos `.lower()` para hacerla *case insensitive*.
*   **Pertenencia:** Podemos comprobar si un string está contenido en otro.

## 4. ⛓️ Concatenación de Condiciones (Lógica Múltiple)
*   **Operador `AND`:** Todas las condiciones deben ser verdaderas para que el resultado sea `True`.
    *   *Ejemplo:* Buscar un usuario llamado "Juan" **Y** que sea mayor de 21 años.
*   **Operador `OR`:** Basta con que una de las condiciones sea verdadera para que el resultado sea `True`.
    *   *Ejemplo:* Acceso a un local si eres mayor de edad **O** vas acompañado de un tutor.

## 5. Estructura IF Statement
Es la implementación práctica de la lógica "Si-Entonces". Permite realizar un seguimiento del estado de nuestro programa y gestionar permisos o procesos de ejecución.

> **Habilidad Profesional:** El dominio de las expresiones booleanas es fundamental para el desarrollo de Backend, permitiendo crear flujos de trabajo seguros y validados.

## 6. Evaluación en Cascada (IF-ELIF-ELSE)
*   **Orden de Prioridad:** Aprendí que Python evalúa las condiciones de arriba hacia abajo. Al usar `elif`, el programa se detiene en cuanto encuentra la primera coincidencia verdadera, optimizando el uso de recursos.
*   **Validación Defensiva:** Uso de `else` como clausura de seguridad para manejar casos no previstos o entradas inválidas del usuario.

##  Estructuras de Datos: Listas y Colecciones (Parte 1)

En esta etapa del máster, comienzo a trabajar con **colecciones de datos**, permitiendo almacenar y manipular múltiples valores bajo un mismo identificador.

*   **Definición de Listas:** Uso de corchetes `[]` para agrupar elementos de forma ordenada.
*   **Indexación:** Comprensión del sistema de índices (empezando desde `0`) para acceder a elementos específicos.
*   **Mutabilidad:** Capacidad de las listas para ser modificadas (añadir, eliminar o cambiar elementos) durante la ejecución del programa.
*   **Funciones Esenciales:**
    *   `.append()`: Para añadir elementos al final.
    *   `.insert()`: Para añadir en una posición específica.
    *   `.pop()` / `.remove()`: Para gestionar la salida de datos.
    *   `len()`: Para conocer la longitud dinámica de la colección.

> **Habilidad Tech:** El dominio de listas es el paso previo fundamental para manejar **Bases de Datos** y flujos de información masiva en el Backend.

# Estructuras de Datos e Iteración (Parte 2)

En este bloque profundizo en el procesamiento masivo de datos y la automatización de tareas repetitivas, herramientas esenciales para la lógica de un motor de gestión de turnos.

---

## 1. Bucles e Iteración de Colecciones


| Estructura | Definición y Uso | Aplicación en Peluquería |
| :--- | :--- | :--- |
| **Bucle `FOR`** | Recorre elementos de una secuencia finita. | Listar todos los servicios del catálogo para el cliente. |
| **Bucle `WHILE`** | Ejecuta código mientras una condición sea `True`. | Mantener el programa activo hasta que se decida "Cerrar Caja". |
| **`enumerate()`** | Devuelve el índice y el valor simultáneamente. | Generar un menú numerado de barberos o servicios automáticamente. |

**Nota de estudio:** El bucle `for` es excelente para la lectura y procesamiento de datos existentes, mientras que el `while` controla el flujo operativo continuo del software.

---

## 2. Modificación de Listas en Tiempo Real

*   **En mi proyecto (IA Turnos):** Gestión dinámica de la cola de espera.
*   **Estudio:** Utilicé `.pop(0)` para implementar una lógica **FIFO** (First In, First Out), asegurando que el primer cliente en llegar sea el primero en ser procesado por el sistema.
*   **Habilidad Pro:** El uso de `.sort()` permite organizar agendas por prioridad o por hora de llegada, optimizando la atención al cliente.

---

## 3. List Comprehensions (Eficiencia de Código)

Es la técnica avanzada para crear nuevas listas a partir de otras de forma compacta y eficiente en una sola línea.

*   **Sintaxis:** `[expresion for elemento in lista if condicion]`
*   **Aplicación Real:** 
    *   Filtrar solo los servicios de "Corte" en una agenda mixta.
    *   Extraer los nombres de clientes que tienen citas confirmadas.

**Nota de estudio:** Esta técnica no solo mejora la legibilidad (Clean Code), sino que es computacionalmente más rápida que los bucles tradicionales para la creación de listas.

---

## 4. Control de Flujo Interno (`break` y `continue`)


| Comando | Acción | Caso de Uso |
| :--- | :--- | :--- |
| **`break`** | Rompe el bucle inmediatamente. | Detener la asignación si se alcanza el cupo máximo de turnos. |
| **`continue`** | Salta a la siguiente iteración. | Ignorar a un cliente que "No asistió" y pasar al siguiente en la lista. |

---

> **Habilidad Tech:** La combinación de **List Comprehensions** e **Iteración** permite procesar agendas complejas en milisegundos. Esta es la base para que mi futura IA analice qué huecos son los más óptimos para ofrecer a nuevos clientes basándose en la duración de cada servicio.

---

### Ejemplo de Código Implementado (Lógica de Negocio)
```python
# Simulación de gestión de turnos del día
turnos_pendientes = ["Corte - 10:00", "Barba - 10:30", "Color - 11:00"]

print("📋 Agenda del día actualizada:")
for i, turno in enumerate(turnos_pendientes, 1):
    print(f"Turno #{i}: {turno}")

# Uso de List Comprehension para auditoría rápida
cortes = [t for t in turnos_pendientes if "Corte" in t]
print(f"\nTotal de servicios de corte hoy: {len(cortes)}")
```
---

# Python Avanzado y Principios SOLID

Este documento forma parte de mi especialización en el **Máster de Conquer Blocks**. Aquí documento conceptos avanzados de Python y la implementación de arquitectura limpia.

---

## Python Avanzado

### 1. Tipado Dinámico y F-Strings
Python permite flexibilidad total, pero la legibilidad es clave:
```python
nombre = "Sam" 
# Uso de f-strings para mayor claridad y rendimiento
print(f"Desarrollador en formación: {nombre}")
```
# 2. List Comprehensions

Optimización de creación de listas en una sola línea:

---

# Crear lista de cuadrados de números pares
```python
cuadrados_pares = [x**2 for x in range(10) if x % 2 == 0]
```
# 3. Manejo Progresivo de Errores (Excepciones)
Fundamental para que una aplicación no "explote" en producción:
```python
try:
    divisor = int(input("Introduce un divisor: "))
    print(10 / divisor)
except ZeroDivisionError:
    print(" Error: No se puede dividir por cero.")
except ValueError:
    print(" Error: Debes ingresar un número válido.")
```
---

# Estadística Aplicada a la Inteligencia Artificial

Este repositorio contiene los apuntes, conceptos fundamentales y ejercicios prácticos del curso de **Estadística Aplicada**, con un enfoque especial en su relevancia para el desarrollo de Redes Neuronales y modelos de Inteligencia Artificial.

---

## Temario del Curso

1. Introducción a la Estadística
2. Estadística Descriptiva
3. Gráficos y Visualización de Datos
4. Probabilidad
5. Distribuciones de Probabilidad
6. Correlación y Regresión
7. Métodos de Muestreo
8. Aplicaciones de la Estadística en Redes Neuronales
9. Ejercicio Práctico

---

## Importancia de la Estadística en Redes Neuronales

### ¿Por qué es importante?
La estadística es crucial para la inteligencia artificial porque proporciona las herramientas y métodos necesarios para analizar datos, construir y validar modelos, hacer inferencias, manejar la incertidumbre y optimizar algoritmos. Sin la estadística, muchos de los avances en IA no serían posibles.

### Aplicaciones de la estadística en IA
* **Análisis de datos:** Comprensión inicial de las variables y detección de patrones.
* **Validación de Modelos:** Evaluación del rendimiento mediante métricas estadísticas.
* **Modelos Predictivos:** Construcción de funciones de estimación basadas en datos históricos.
* **Reducción de dimensiones:** Simplificación del espacio de características (ej. PCA).
* **Análisis de la incertidumbre:** Cuantificación del riesgo y la probabilidad en las predicciones.
* **Optimización:** Ajuste de pesos y funciones de pérdida mediante cálculo y probabilidad.

---

## ¿Qué es la Estadística?

La **estadística** es una rama de las matemáticas que se encarga de recolectar, analizar, interpretar, presentar y organizar datos. Es una herramienta fundamental en muchas disciplinas, como la economía, la biología, la ingeniería, la psicología, la sociología y la inteligencia artificial, ya que permite tomar decisiones informadas basadas en datos y tendencias.

Se divide principalmente en dos grandes áreas:

| Área | Descripción | Técnicas Comunes |
| :--- | :--- | :--- |
| **Estadística Descriptiva** | Se enfoca en describir y resumir un conjunto de datos para representar la información de manera comprensible. | Media, mediana, moda, desviación estándar, histogramas y diagramas de dispersión. |
| **Estadística Inferencial** | Centrada en hacer inferencias o predicciones sobre una población a partir de una muestra de datos. | Estimación de intervalos de confianza, pruebas de hipótesis, análisis de regresión y ANOVA. |

---

## Estadística Descriptiva

Esta sección se enfoca en describir y resumir un conjunto de datos a través de cuatro pilares de medición:
* Medidas de tendencia central
* Medidas de dispersión
* Medidas de forma

### Medidas de Tendencia Central

#### 1. Media
La media aritmética indica el **valor promedio** de un conjunto de datos. Se utiliza para representar el valor típico de una muestra y es una de las medidas más comunes en la estadística descriptiva.

* **Fórmula de la Media:**
  $$\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$$

* **Otros tipos de media:**
  * Media Geométrica
  * Media Armónica
  * Media Ponderada
  * Media Cuadrática

#### 2. Mediana
Es el **valor central** de un conjunto de datos previamente ordenados de menor a mayor. A diferencia de la media, la mediana **no se ve afectada por valores extremos (outliers)**, por lo que proporciona una mejor representación del centro en distribuciones asimétricas.

* **¿Cómo se calcula?**
  1. Ordenar la muestra de menor a mayor.
  2. Elegir el elemento central:
     * **Si el número de elementos ($n$) es impar:** Se toma el valor en la posición $\frac{n + 1}{2}$. *(Ej: si hay 99 elementos, se toma la posición 50).*
     * **Si el número de elementos ($n$) es par:** Se calcula la media de los dos valores centrales que ocupan las posiciones $\frac{n}{2}$ y $\frac{n}{2} + 1$. *(Ej: si hay 100 elementos, se promedian los valores de las posiciones 50 y 51).*

#### 3. Moda
Es el **valor que aparece con mayor frecuencia** en un conjunto de datos (el número que más se repite). 
* Proporciona una idea rápida del valor más típico de la muestra.
* A diferencia de la media y la mediana, la moda **no necesariamente representa un valor central**.

---

## Dataset de Trabajo (Ejercicio Práctico)

Para el desarrollo práctico del curso y la generación de gráficos como histogramas, utilizaremos el siguiente conjunto de datos:

* **Enlace al dataset:** [Anual Salary reports survey en Kaggle](https://www.kaggle.com/datasets/micheldc55/anual-salary-reports-survey)
* **Descripción:** Contiene un informe salarial fabricado con 100,000 registros para realizar análisis predictivos y estimar el salario anual en función de variables demográficas y educativas.

### Columnas del Dataset:
* `ID`: Identificador único del candidato.
* `income`: Ingreso anual declarado por la persona.
* `age`: Edad de la persona al momento de la prueba.
* `gender`: Género declarado (50% femenino, 50% masculino).
* `education_level`: Nivel educativo alcanzado (0: Primaria completa, 1: Secundaria completa, 2: Terciaria completa, 3: Posgrado completo).

---

# Gráficos y Visualización de Datos en Inteligencia Artificial

Este módulo cubre la importancia de la representación gráfica de datos, los tipos de gráficos más comunes utilizados en la analítica de datos, el uso de la librería **Seaborn** y las buenas prácticas para diseñar visualizaciones efectivas.

---

## Temario de la Clase

1. La importancia de la visualización de datos
2. Tipos de gráficos más comunes
3. Ejemplos prácticos en Seaborn
4. Buenas prácticas de visualización

---

## Importancia de la Representación Gráfica

La visualización de datos juega un papel crucial tanto en el análisis exploratorio como en el desarrollo de modelos de Inteligencia Artificial (IA) por dos razones principales:

1. **Exploración de datos:** Ayuda a entender las características principales de los datos, permitiendo identificar patrones, tendencias y relaciones ocultas entre variables.
2. **Detección de anomalías:** Facilita la identificación rápida de valores atípicos (*outliers*) o errores en los datos que podrían perjudicar el entrenamiento de un modelo de IA.

> **"Una imagen vale más que mil palabras"**
> Comparar una tabla con 15 filas de texto frente a un gráfico de líneas permite procesar la evolución de una variable (como las ventas de una empresa a lo largo de los años) de forma instantánea.

---

## Representación Gráfica con Seaborn

**Seaborn** es una librería de visualización de datos para Python desarrollada sobre **Matplotlib**. Proporciona una interfaz de alto nivel para diseñar gráficos estadísticos atractivos, estilizados y con muy pocas líneas de código, lo que la hace **fácil y rápida de usar**.

---

## Tipos de Gráficos Útiles para el Análisis de Datos

| Tipo de Gráfico | ¿Qué Representan? | ¿Para Qué Se Usan? | Conclusiones que se extraen |
| :--- | :--- | :--- | :--- |
| **Gráfico de Dispersión** *(Scatter plot)* | Relación entre dos variables continuas mediante puntos en un plano cartesiano $(X, Y)$. | Identificar y analizar relaciones, patrones y tendencias bidimensionales. | Correlaciones positivas/negativas, agrupaciones naturales y valores atípicos. |
| **Gráfico de Barras** *(Bar plot)* | Datos categóricos representados con barras donde la longitud es proporcional al valor. | Comparar diferentes categorías o clases entre sí de forma directa. | Diferencias de magnitud e identificación de categorías con valores máximos o mínimos. |
| **Gráfico de Cajas** *(Box plot)* | Distribución de una variable continua mostrando su mediana, cuartiles y valores atípicos. | Resumir estadísticamente la dispersión y la simetría de los datos. | Nivel de dispersión, asimetría de la muestra y presencia inequívoca de *outliers*. |
| **Histograma** | Distribución de una variable continua dividiendo el rango de valores en intervalos (*bins*). | Entender la forma de la distribución y la frecuencia de los datos. | Patrones de simetría, sesgos, presencia de múltiples picos (multimodalidad) y brechas. |
| **Gráfico de Violín** *(Violin plot)* | Combinación de un gráfico de cajas (*box plot*) con un gráfico de densidad de kernel. | Visualizar la distribución exacta y la densidad de una variable en diferentes grupos. | Visión detallada de la concentración de los datos y comparación de formas entre categorías. |
| **Mapa de Calor** *(Heatmap)* | Relación de correlación entre múltiples variables numéricas dispuestas en una matriz. | Identificar patrones de correlación cruzada mediante una escala de colores. | Selección de características de entrada relevantes para IA y detección de colinealidad. |

---

## Dataset de Trabajo: Iris Dataset

El conjunto de datos **"Iris"** es uno de los datasets más célebres y utilizados en la estadística y el aprendizaje automático (*Machine Learning*).

* **Contenido:** Contiene **150 observaciones** de flores Iris divididas equitativamente en 3 especies distintas: *Iris setosa*, *Iris versicolor* e *Iris virginica*.
* **Columnas (Características):**
  * `Sepal Length (cm)`: Longitud del sépalo.
  * `Sepal Width (cm)`: Ancho del sépalo.
  * `Petal Length (cm)`: Longitud del pétalo.
  * `Petal Width (cm)`: Ancho del pétalo.
  * `Species`: Clase o especie de la flor (*setosa*, *versicolor*, *virginica*).

---

## Principios de un Buen Gráfico (Buenas Prácticas)

Para construir visualizaciones profesionales y evitar gráficos sobrecargados o confusos, se deben seguir cuatro principios fundamentales:

### 1. Claridad y Simplicidad (La Regla de Oro)
* **Evitar la sobrecarga:** No satures el gráfico con demasiados elementos visuales, líneas de cuadrícula excesivas o símbolos innecesarios que distraigan.
* **Título descriptivo:** Cada gráfico debe explicar por sí mismo qué información está mostrando.
* **Etiquetas legibles:** Coloca nombres claros en los ejes ($X$ e $Y$) y leyendas accesibles.

### 2. Escala Apropiada
* **Ejes proporcionados:** Las escalas deben ser correctas para no distorsionar la interpretación de los datos (por ejemplo, evitar estirar o comprimir el eje $Y$ para exagerar una tendencia de crecimiento).
* **Intervalos consistentes:** Mantén incrementos uniformes en las unidades de los ejes para facilitar las comparaciones visuales.

### 3. Colores y Etiquetas
* **Uso estratégico del color:** Utiliza el color para diferenciar categorías o resaltar puntos críticos, no por estética aleatoria. Demasiados colores confunden.
* **Contraste alto:** Asegúrate de que los textos y los elementos clave sean fácilmente distinguibles del fondo.

### 4. Narrativa y Contexto
* **Historias con datos:** Un gráfico no solo presenta datos, cuenta una historia. Debe guiar al espectador a comprender el significado real de las métricas.
* **Información complementaria:** Agrega notas al pie o leyendas directas si el contexto lo requiere.

---

## Limitaciones y Precauciones

Aunque los gráficos son herramientas de comunicación potentes, están sujetos a sesgos:
* **Sesgo de selección:** Omitir o recortar ciertos datos al construir un gráfico puede dirigir al espectador hacia interpretaciones erróneas o conclusiones convenientemente engañosas. Siempre se debe buscar la transparencia de la muestra.



## Sobre el Máster
Estoy formándome en [Conquer Blocks](https://conquerblocks.com), una academia de alto rendimiento enfocada en tecnologías modernas y buenas prácticas de programación.


Actualmente cursando el Máster en Conquer Blocks con el objetivo de especializarme en el mercado tecnológico español. Enfocado en Clean Code (SOLID) y arquitectura escalable.
Este repositorio es mi diario de aprendizaje mientras curso el Máster en Desarrollo Full Stack en Conquer Blocks. Aquí comparto mis propios resúmenes, lógica y soluciones a retos técnicos, respetando siempre los materiales privados de la academia.
