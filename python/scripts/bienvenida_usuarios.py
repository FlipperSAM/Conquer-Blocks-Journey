## 🧪 Ejercicios Prácticos: Validación de Usuarios

En este ejercicio practiqué la **limpieza de strings** y el control de flujo. 

**Conceptos aplicados:**
*   `.upper(): Convierte todo el texto a MAYÚSCULAS. Útil para destacar mensajes importantes.
*   `.replace()`: Para eliminar caracteres especiales (como `.` o `#`).
*   `.lower()`: Para estandarizar la entrada y evitar errores por mayúsculas/minúsculas.
*   `.title()`: Para dar un formato profesional al nombre en la salida.
*   `if / else`: Lógica de decisión para usuarios registrados vs. invitados.

> [Ver código fuente del script aquí](./scripts/bienvenida_usuarios.py)


# Script de Bienvenida Personalizada
# Objetivo: Limpiar la entrada del usuario y validar acceso

nombre = input("Introduce el nombre de usuario: ")

# Limpieza de caracteres no deseados (Puntos y Almohadillas)
nombre_limpio = nombre.replace(".", "").replace("#", "")

# Lista de usuarios autorizados
usuarios_registrados = ["alejandro", "naomi", "sergio"]

# Validación (Convertimos a minúsculas para comparar)
if nombre_limpio.lower() in usuarios_registrados:
    # Usamos .title() para que siempre salga la primera en Mayúscula
    print(f"¡Bienvenido, {nombre_limpio.title()}!")
else:
    print("Bienvenido, usuario invitado.")
