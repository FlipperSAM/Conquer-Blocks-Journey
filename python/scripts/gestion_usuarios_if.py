"""
Módulo: gestion_usuarios_if.py
Descripción: Sistema de bienvenida personalizada con limpieza de caracteres y lógica IF-ELIF-ELSE.
Temas: Control de flujo, normalización de strings y operadores de comparación.
"""

def bienvenida_personalizada():
    # 1. Entrada de datos
    entrada = input("Introduce tu nombre de usuario: ")

    # 2. Limpieza de datos (Normalización)
    # Eliminamos puntos y almohadillas, y convertimos a minúsculas para comparar
    nombre = entrada.replace(".", "").replace("#", "").lower()

    # 3. Lógica de Bienvenida con IF-ELIF-ELSE
    # Esta estructura es más clara que una lista para este ejercicio académico
    if nombre == "alejandro":
        print("¡Hola Alejandro! Es un gusto verte de nuevo en el sistema.")
    elif nombre == "naomi":
        print("¡Bienvenida Naomi! Tus proyectos están listos para revisión.")
    elif nombre == "sergio":
        print("¡Qué tal Sergio! El servidor está funcionando correctamente.")
    else:
        print("Bienvenido, usuario invitado. Tienes acceso limitado.")

if __name__ == "__main__":
    bienvenida_personalizada()
