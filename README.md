# Conquer-Blocks-Journey

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



# 🐍 Tipado Dinámico y F-Strings

Python es de tipado dinámico, lo que significa que no necesito declarar el tipo de variable. Para imprimir de forma eficiente uso f-strings, que son más rápidas y legibles.
Un ejemplo claro puede ser:

```python
nombre = "Sam estudiante Conquer"
print(f"Hola, mi nombre es {Sam}")
```
# 🐍 List Comprehensions (Python Avanzado)
Una forma 'Pythonic' de crear listas es mediante List Comprehensions. Permite reducir líneas de código y mejorar la velocidad de ejecución.
```python
# Crear una lista de números pares
pares = [x for x in range(10) if x % 2 == 0]
```
# Principios SOLID (S de SRP)
El primer principio de SOLID es el de Responsabilidad Única (SRP). Una clase o función debe tener una sola razón para cambiar. Si una función calcula un impuesto, no debería encargarse también de imprimir el recibo.

## 🎓 Sobre el Máster
Estoy formándome en [Conquer Blocks](https://conquerblocks.com), una academia de alto rendimiento enfocada en tecnologías modernas y buenas prácticas de programación.

## 📖 Tabla de Contenidos (Navegación interna)
* [🐍 Fundamentos de Python](#fundamentos-de-python)
* [🟢 Principios SOLID](#principios-solid-s-de-srp)
* [📁 Mis Proyectos](#proyectos-realizados)


📍 Actualmente cursando el Máster en Conquer Blocks con el objetivo de especializarme en el mercado tecnológico español. Enfocado en Clean Code (SOLID) y arquitectura escalable.
Este repositorio es mi diario de aprendizaje mientras curso el Máster en Desarrollo Full Stack en Conquer Blocks. Aquí comparto mis propios resúmenes, lógica y soluciones a retos técnicos, respetando siempre los materiales privados de la academia.
