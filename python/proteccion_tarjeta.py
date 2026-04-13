"""
Módulo: proteccion_tarjeta.py
Descripción: Script para enmascarar números de tarjeta de crédito (Data Masking).
Conceptos: Slicing de strings, longitud dinámica y seguridad de datos.
"""
def enmascarar_tarjeta():
    print("--- 🛡️ SISTEMA DE SEGURIDAD DE DATOS ---")
    
    # 1. Entrada de datos (Eliminamos espacios para que la lógica no falle)
    tarjeta = input("Introduce el número de la tarjeta: ").replace(" ", "")

    # 2. Validación de longitud mínima
    if len(tarjeta) < 4:
        print("❌ Error: El número es demasiado corto.")
    else:
        # 3. Lógica de enmascaramiento:
        # Creamos asteriscos para todos los números menos los últimos 4
        # Usamos slicing [-4:] para obtener el final de la cadena
        visibles = tarjeta[-4:]
        ocultos = "*" * (len(tarjeta) - 4)
        
        # 4. Resultado formateado
        print(f"\nNúmero protegido: {ocultos}{visibles}")

if __name__ == "__main__":
    enmascarar_tarjeta()
