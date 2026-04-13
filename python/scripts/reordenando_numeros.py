"""
Módulo: reordenando_numeros.py
Descripción: Descomposición e inversión de números enteros.
Conceptos: Iteración de strings y Slicing negativo [::-1].
"""

def procesar_numero():
    print("--- 🔢 PROCESADOR DE NÚMEROS ---")
    
    # 1. Entrada de datos como string para facilitar la manipulación
    numero = input("Introduce un número de más de una cifra: ")

    # Parte A: Imprimir componentes uno a uno
    print("\nComponentes del número:")
    for cifra in numero:
        print(cifra)

    # Parte B: Invertir el número
    # Verificamos si tiene 4 cifras para cumplir con el requisito específico
    if len(numero) == 4:
        # Usamos Slicing [::-1] que significa: "empieza desde el final hasta el principio, de uno en uno"
        numero_invertido = numero[::-1]
        print(f"\nNúmero invertido (4 cifras): {numero_invertido}")
    else:
        print(f"\nNúmero invertido: {numero[::-1]} (Nota: No tiene 4 cifras)")

if __name__ == "__main__":
    procesar_numero()
