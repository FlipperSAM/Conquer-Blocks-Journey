"""
Módulo: mensaje_bienvenida.py
Descripción: Script de bienvenida con procesamiento avanzado de strings.
Conceptos: .upper(), .lower(), .title(), .replace() y f-strings.
"""

def ejecutar_script():
    # 1. Almacenar mensaje base
    mensaje_base = "estas usando python"
    print(f"Contenido inicial: {mensaje_base}")

    # 2. Capturar nombre de usuario
    nombre_usuario = input("Sam")

    # 3. Formato en MAYÚSCULAS
    mensaje_caps = f"¡HOLA, {nombre_usuario}, {mensaje_base}!".upper()
    print(mensaje_caps)

    # 4. Formato en minúsculas
    print(mensaje_caps.lower())

    # 5, 6 y 7. Limpieza y formato final (Primera letra Mayúscula y sin puntos)
    # Limpiamos el punto y aplicamos .title() para corregir el formato (ej. ferNanDO -> Fernando)
    nombre_corregido = nombre_usuario.replace(".", "").title()
    
    # Mensaje final optimizado
    print(f"¡Hola, {nombre_corregido}, estas usando Python!")

if __name__ == "__main__":
    ejecutar_script()
