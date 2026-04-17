# Conquer-Blocks-Journey

## 📖 Tabla de Contenidos (Navegación interna)
* ## 🐍 Fundamentos de Python
Documentación técnica sobre las bases del lenguaje y manipulación de datos.
*   **[Ver notas](./python/docs/NOTAS_STRINGS_BIENVENIDA.md):** Explicación detallada de métodos como `.upper()`, `.lower()` y el uso de f-strings.

*   **[Principios SOLID](./solid/NOTAS_SOLID.md)**  

## 📁 Mis Proyectos
Aquí puedes encontrar los ejercicios prácticos que voy desarrollando durante el máster:

*   **[Script Bienvenida](./python/scripts/mensaje_bienvenida.py):** Un ejercicio de normalización de datos, limpieza de strings y validación de usuarios con buenas prácticas de Python.
*   **[💰 Proyecto: Calculadora de Ahorros](./python/scripts/calculadora_ahorros.py):** Un sistema financiero completo que proyecta ahorros anuales y analiza la viabilidad económica bajo cambios en la jornada laboral y reducción de gastos.
*   **[🏦 Proyecto: Casa de Cambios](./python/scripts/casa_cambios.py):** Un script de lógica financiera que aplica operadores aritméticos, cálculo de tasas de gestión (porcentajes) y formateo de precisión decimal para el manejo de divisas.
*   **[🚗 Proyecto: Comisión de carros](./python/scripts/comisiones_carros.py):** Un script de gestión de ventas que calcula comisiones variables según el modelo de vehículo y el volumen de ventas mensual.
*   **[🔄 Proyecto: Repetir Caracteres](./python/scripts/duplicador_caracteres.py):** Un script que demuestra el uso de bucles para la transformación de datos y la concatenación dinámica de strings.
*   **[🚀 Script Bienvenida](./python/scripts/mensaje_bienvenida.py):** Un ejercicio de procesamiento avanzado de strings que implementa normalización de datos mediante métodos nativos (`.upper()`, `.lower()`, `.title()`), limpieza de caracteres especiales y uso de f-strings.
*   **[🏆 Proyecto: Olimpiadas Skeleton](./python/scripts/olimpiadas_skeleton.py):** Un script avanzado de conversión de unidades de tiempo y cálculo de velocidad media aplicado a resultados olímpicos.
*   **[🛡️ Proyecto: Protección de Tarjeta](./python/scripts/proteccion_tarjeta.py):** Un script de seguridad que aplica técnicas de enmascaramiento de datos (Data Masking) para ocultar información sensible.
*   **[🔄 Proyecto: Reordenando Números](./python/scripts/reordenando_numeros.py):** Un script que descompone números en sus componentes individuales e implementa la inversión de secuencias mediante slicing avanzado.
*   **[🍽️ Proyecto: Cuenta de Restaurante](./python/scripts/restaurante_cuenta.py):** Un sistema de facturación que utiliza diccionarios para gestionar un menú y generar un ticket de venta detallado.
*   **[Análisis: Lógica Condicional](./python/docs/NOTAS_CONDICIONALES_PRO.md):** Resumen de investigación sobre estructuras de decisión y operadores lógicos.
*   **[Script: Test de Lógica](./python/scripts/test_condicionales_pro.py):** Implementación práctica de comparaciones y operadores booleanos.
*   **[Proyecto: Gestión de Usuarios IF](./python/scripts/gestion_usuarios_if.py):** Un script de autenticación básica que utiliza condicionales para dar bienvenidas personalizadas tras normalizar la entrada del usuario.
*   **[Proyecto: Becas Estudiantes](./python/scripts/becas_estudiantes.py):** Un script de validación que utiliza operadores lógicos y comparaciones de rango para determinar la elegibilidad de becas académicas.
*   **[Proyecto: Declaración de la Renta](./python/scripts/declaracion_renta.py):** Un simulador tributario que implementa lógica de filtros previos (edad/ingresos) y cálculo de tramos impositivos mediante condicionales anidados.
*   **[Proyecto: Hamburguesería Online](./python/scripts/hamburgueseria_online.py):** Sistema de pedidos interactivo con menús dinámicos que cambian según la elección del usuario, aplicando normalización de entradas.
*   **[Proyecto: Gestión de Inventario](./python/scripts/gestion_inventario.py):** Una aplicación práctica de estructuras de datos que implementa la manipulación dinámica de listas (CRUD básico).


---
## 📖 Teoria

# 💻 Dominio de la Terminal y Linux

En el desarrollo de software moderno, la terminal no es solo una herramienta, es el entorno de trabajo principal. Este documento resume los comandos esenciales que utilizo para gestionar proyectos y sistemas de archivos de forma eficiente.

---

## 📂 Gestión de Archivos y Navegación

| Comando | Descripción | Uso Profesional |
| :--- | :--- | :--- |
| `pwd` | **Print Working Directory** | Confirmar en qué carpeta estoy antes de ejecutar un comando crítico. |
| `ls -la` | **Listar todo** | Ver archivos ocultos (como `.env` o `.git`) y permisos de usuario. |
| `cd ..` | **Change Directory** | Navegar hacia atrás en la estructura de carpetas. |
| `mkdir -p` | **Make Directory** | Crear rutas complejas de una sola vez (ej. `mkdir -p src/components`). |
| `touch` | **Crear archivo** | Generar archivos de código (`.py`, `.js`) sin salir de la terminal. |

---

## 🛠️ Manipulación y Visualización de Datos

*   **`cat / head / tail`**: Fundamentales para leer logs de errores o previsualizar archivos sin abrirlos en un editor pesado.
*   **`mv` (Move)**: Se utiliza tanto para mover archivos como para **renombrarlos**.
*   **`cp -r`**: Copiar directorios enteros de forma recursiva (ideal para hacer backups rápidos).
*   **`rm -rf`**: Borrado recursivo y forzado. Es el comando de "limpieza total" de carpetas de dependencias o temporales.

---

## ⚡ Comandos de Poder y Sistema

*   **`sudo`**: Ejecución con privilegios de administrador. Vital para instalaciones de software.
*   **`grep`**: El buscador universal. Permite encontrar una palabra específica dentro de cientos de archivos.
*   **`history`**: Para recuperar ese comando largo y complejo que escribiste hace 10 minutos.
*   **`clear`**: Mantener el espacio de trabajo limpio para evitar distracciones visuales.

---
> "Un buen desarrollador rara vez despega las manos del teclado." 
> *Notas de aprendizaje en Conquer Blocks enfocadas en estándares Linux.*


---
# 🐍 Python

# 📑 Análisis Técnico: Fundamentos y Aplicación en Python

Este documento detalla la base teórica y práctica asimilada durante el primer bloque del **Máster en Conquer Blocks**, vinculando cada concepto con los proyectos reales desarrollados en este repositorio.

---

# 📚 Teoría Aplicada a mis Proyectos

### 1. Uso de variables y nomenclatura
*   **En mis proyectos:** Usé variables como **`ingreso_hora`**, **`nombre_usuario`** y constantes en mayúsculas como **`TASA_CAMBIO`** 
*   **Estudio:** Apliqué el Snake Case **`nombre_bajo_guion`**, que es el estándar en Python. Diferencie entre variables que cambian y constantes que no.

### 2. Strings y sus funciones/métodos
*   **En mis proyectos:** El script de Protección de Tarjeta y el de Bienvenida.
*   **Estudio:** Usé **`.lower()`**, **`.upper()`**, **`.title()`** para formatear, y **`.replace()`** para limpiar datos sucios (como los puntos en el nombre). También el Slicing **`[-4:]`** para la tarjeta.

### 3. Números y operaciones aritméticas
*   **En mis proyectos:** La Casa de Cambios y las Olimpiadas.
*   **Estudio:** Usé **`*`** (multiplicación), **`/`** (división) y **`-`** (resta). Apliqué la lógica de porcentajes (comisiones) y conversiones físicas (velocidad).

### 4. Combinar números y strings
*   **En mis proyectos:** En todos los **`print()`** finales.
*   **Estudio:** Dominé las **`f-strings`** **`(f"Hola {nombre}, tienes {ahorro}€")`**. Es la forma más profesional de mezclar texto con resultados numéricos sin que el programa dé error.

### 5. Leer valores de entrada
*   **En mis proyectos:** El uso constante de **`input()`**.
*   **Estudio:** Entendí que todo lo que entra por **`input()`** es inicialmente un String. Sin este comando, mis programas no serían interactivos.

### 6. Conversión entre tipos de datos (Casting)
*   **En mis proyectos:** Calculadora de Ahorros y Olimpiadas.
*   **Estudio:** Usé **`float()`** para dinero e **`int()`** para minutos/segundos. Aprendí que para operar matemáticamente con un **`input()`**, primero se debe convertir a número.

### 7. Uso de los comentarios
*   **En mis proyectos:** Los encabezados con **`"""`** (Docstrings) y los **`#`** estos se usan para explicar pasos a otros desarrolladores que vean el código desde el backend.
*   **Estudio:** Documenté el "qué" y el "por qué" del código. Un código sin comentarios es un código "huérfano" que nadie quiere mantener en una empresa.

---
*Este análisis certifica mi capacidad para transformar conceptos teóricos en soluciones de código escalables y profesionales.*

# ⚖️ Lógica de Control: Test Condicionales y Expresiones Booleanas

En este módulo del máster de **Conquer Blocks**, profundizo en la capacidad del software para evaluar situaciones y tomar decisiones basadas en valores booleanos (**True** / **False**).

---

## 1. 🔄 Asignación vs. Comparación
*   **Asignación (`=`):** Se utiliza para asociar un valor a una variable.
    *   Ejemplo: `nombre_usuario = "Juan"`
*   **Comparación (`==`):** Evalúa si dos valores son iguales, devolviendo un booleano.
    *   Ejemplo: `nombre_usuario == "Juan"` (Resultado: `True`)

## 2. 🛠️ Operadores de Comparación

| Operador | Significado | Ejemplo |
| :--- | :--- | :--- |
| `==` | Igual a | `h == 10` |
| `!=` | Diferente de | `h != 10` |
| `>` | Mayor que | `h > 0` |
| `<` | Menor que | `h < 0` |
| `>=` | Mayor o igual que | `h >= 0` |
| `<=` | Menor o igual que | `h <= 0` |

## 3. 🧠 Testeos Condicionales Avanzados
*   **Case Sensitivity:** Las comparaciones de strings son sensibles a mayúsculas. Para una comparación profesional, usamos `.lower()` para hacerla *case insensitive*.
*   **Pertenencia:** Podemos comprobar si un string está contenido en otro.

## 4. ⛓️ Concatenación de Condiciones (Lógica Múltiple)
*   **Operador `AND`:** Todas las condiciones deben ser verdaderas para que el resultado sea `True`.
    *   *Ejemplo:* Buscar un usuario llamado "Juan" **Y** que sea mayor de 21 años.
*   **Operador `OR`:** Basta con que una de las condiciones sea verdadera para que el resultado sea `True`.
    *   *Ejemplo:* Acceso a un local si eres mayor de edad **O** vas acompañado de un tutor.

## 5. 🏗️ Estructura IF Statement
Es la implementación práctica de la lógica "Si-Entonces". Permite realizar un seguimiento del estado de nuestro programa y gestionar permisos o procesos de ejecución.

> **Habilidad Profesional:** El dominio de las expresiones booleanas es fundamental para el desarrollo de Backend, permitiendo crear flujos de trabajo seguros y validados.

## 6. 🌊 Evaluación en Cascada (IF-ELIF-ELSE)
*   **Orden de Prioridad:** Aprendí que Python evalúa las condiciones de arriba hacia abajo. Al usar `elif`, el programa se detiene en cuanto encuentra la primera coincidencia verdadera, optimizando el uso de recursos.
*   **Validación Defensiva:** Uso de `else` como clausura de seguridad para manejar casos no previstos o entradas inválidas del usuario.

## 📦 Estructuras de Datos: Listas y Colecciones (Parte 1)

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
---

# 🐍 Python Avanzado y Principios SOLID

Este documento forma parte de mi especialización en el **Máster de Conquer Blocks**. Aquí documento conceptos avanzados de Python y la implementación de arquitectura limpia.

---

## 🛠️ Python Avanzado

### 1. Tipado Dinámico y F-Strings
Python permite flexibilidad total, pero la legibilidad es clave:
```python
nombre = "Sam" 
# Uso de f-strings para mayor claridad y rendimiento
print(f"Desarrollador en formación: {nombre}")
```
# 🐍 2. List Comprehensions

Optimización de creación de listas en una sola línea:

---

# Crear lista de cuadrados de números pares
```python
cuadrados_pares = [x**2 for x in range(10) if x % 2 == 0]
```
# 3. 🚫 Manejo Progresivo de Errores (Excepciones)
Fundamental para que una aplicación no "explote" en producción:
```python
try:
    divisor = int(input("Introduce un divisor: "))
    print(10 / divisor)
except ZeroDivisionError:
    print("❌ Error: No se puede dividir por cero.")
except ValueError:
    print("❌ Error: Debes ingresar un número válido.")
```
---

## 🎓 Sobre el Máster
Estoy formándome en [Conquer Blocks](https://conquerblocks.com), una academia de alto rendimiento enfocada en tecnologías modernas y buenas prácticas de programación.


📍 Actualmente cursando el Máster en Conquer Blocks con el objetivo de especializarme en el mercado tecnológico español. Enfocado en Clean Code (SOLID) y arquitectura escalable.
Este repositorio es mi diario de aprendizaje mientras curso el Máster en Desarrollo Full Stack en Conquer Blocks. Aquí comparto mis propios resúmenes, lógica y soluciones a retos técnicos, respetando siempre los materiales privados de la academia.
