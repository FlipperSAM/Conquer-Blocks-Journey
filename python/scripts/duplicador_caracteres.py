"""
Módulo: duplicador_caracteres.py
Descripción: Script para duplicar cada carácter de una cadena de texto.
Conceptos: Bucles for, iteración de strings y concatenación.
"""

def duplicar_entrada():
    print("--- 🔄 TRANSFORMADOR: DUPLICADOR DE CARACTERES ---")

    # 1. Captura de datos
    entrada = input("Introduce un texto de 5 caracteres: ")

    # 2. Validación de longitud (Garantiza que el input sea de 5)
    if len(entrada) != 5:
        print("❌ Error: Debes introducir exactamente 5 caracteres.")
    else:
        # 3. Lógica de duplicación mediante iteración
        resultado = ""
        for caracter in entrada:
            # Multiplicamos el carácter por 2 y lo acumulamos
            resultado += caracter * 2
        
        # 4. Salida de datos
        print(f"Entrada: {entrada}")
        print(f"Salida:  {resultado}")

if __name__ == "__main__":
    duplicar_entrada()
