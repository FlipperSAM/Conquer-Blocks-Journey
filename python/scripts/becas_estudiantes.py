"""
Módulo: becas_estudiantes.py
Descripción: Sistema de validación para el otorgamiento de becas de excelencia.
Conceptos: Operadores lógicos (and), comparaciones numéricas y captura de datos.
"""

def evaluar_beca():
    print("--- 🎓 SISTEMA NACIONAL DE BECAS DE EXCELENCIA ---")
    
    # 1. Entrada de datos del estudiante
    nombre = input("Introduce el nombre del estudiante: ").title()
    try:
        edad = int(input(f"Introduce la edad de {nombre}: "))
        nota_media = float(input(f"Introduce la nota media de {nombre}: "))

        # 2. Lógica de validación con operadores lógicos
        # Requisitos: Nota mínima de 8 Y edad entre 17 y 21 años
        cumple_nota = nota_media >= 8
        cumple_edad = 17 <= edad <= 21

        print("\n" + "="*40)
        if cumple_nota and cumple_edad:
            print(f"✅ RESULTADO: {nombre} es APTO/A para la beca.")
        else:
            print(f"🛑 RESULTADO: {nombre} NO cumple los requisitos.")
            
            # Feedback específico para el usuario
            if not cumple_nota:
                print("- Motivo: La nota media debe ser igual o superior a 8.")
            if not cumple_edad:
                print("- Motivo: La edad debe estar comprendida entre 17 y 21 años.")
        print("="*40)

    except ValueError:
        print("❌ Error: Por favor, introduce valores numéricos válidos para edad y nota.")

if __name__ == "__main__":
    evaluar_beca()
