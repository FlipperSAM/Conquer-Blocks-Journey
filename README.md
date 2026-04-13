# Conquer-Blocks-Journey

## 📖 Tabla de Contenidos (Navegación interna)
* ## 🐍 Fundamentos de Python
Documentación técnica sobre las bases del lenguaje y manipulación de datos.
*   **[📚 Ver notas](./python/NOTAS_STRINGS.md):** Explicación detallada de métodos como `.upper()`, `.lower()` y el uso de f-strings.

*   **[🟢 Principios SOLID](./solid/NOTAS_SOLID.md)**  

## 📁 Mis Proyectos
Aquí puedes encontrar los ejercicios prácticos que voy desarrollando durante el máster:

*   **[🚀 Script Bienvenida](./python/docs/mensaje_bienvenida.py):** Un ejercicio de normalización de datos, limpieza de strings y validación de usuarios con buenas prácticas de Python.
*   **[🏦 Proyecto: Casa de Cambios](./python/docs/casa_cambios.py):** Un script de lógica financiera que aplica operadores aritméticos, cálculo de tasas de gestión (porcentajes) y formateo de precisión decimal para el manejo de divisas.
*   **[🏆 Proyecto: Olimpiadas Skeleton](./python/docs/olimpiadas_skeleton.py):** Un script avanzado de conversión de unidades de tiempo y cálculo de velocidad media aplicado a resultados olímpicos.
*   **[🚗 Proyecto: Comisión de Automóviles](./python/docs/comisiones_carros.py):** Un script de gestión de ventas que calcula comisiones variables según el modelo de vehículo y el volumen de ventas mensual.
*   **[🍽️ Proyecto: Cuenta de Restaurante](./python/docs/restaurante_cuenta.py):** Un sistema de facturación que utiliza diccionarios para gestionar un menú y generar un ticket de venta detallado.
*   **[🛡️ Proyecto: Protección de Tarjeta](./python/docs/proteccion_tarjeta.py):** Un script de seguridad que aplica técnicas de enmascaramiento de datos (Data Masking) para ocultar información sensible.
*   **[🔄 Proyecto: Reordenando Números](./python/docs/reordenando_numeros.py):** Un script que descompone números en sus componentes individuales e implementa la inversión de secuencias mediante slicing avanzado.


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
