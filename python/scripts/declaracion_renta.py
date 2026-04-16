"""
Módulo: declaracion_renta.py
Descripción: Cálculo automatizado de tipos impositivos según requisitos legales.
Conceptos: IF anidados, operadores lógicos y validación de mayoría de edad.
"""

def calcular_renta():
    print("--- ⚖️ AGENCIA TRIBUTARIA: MÓDULO DE RENTA ---")
    
    try:
        edad = int(input("Introduce tu edad: "))
        ingresos_mes = float(input("Introduce tus ingresos mensuales (€): "))

        # Filtro de seguridad inicial: Requisitos para tributar
        if edad >= 18 and ingresos_mes > 1000:
            print("✅ Perfil apto para tributación. Evaluando tramo...")
            renta_anual = ingresos_mes * 12
            
            # Estructura de decisión por tramos impositivos
            if renta_anual < 15000:
                tipo = "5%"
            elif 15000 <= renta_anual < 25000:
                tipo = "15%"
            elif 25000 <= renta_anual < 35000:
                tipo = "20%"
            elif 35000 <= renta_anual < 60000:
                tipo = "30%"
            else:
                tipo = "45%"
            
            print(f"\nResultado: Renta anual de {renta_anual:,.2f}€. \nTipo impositivo: {tipo}")
        else:
            print("🛑 Resultado: No cumples los requisitos mínimos para aplicar el tipo impositivo.")

    except ValueError:
        print("❌ Error: Por favor, introduce valores numéricos válidos.")

if __name__ == "__main__":
    calcular_renta()
