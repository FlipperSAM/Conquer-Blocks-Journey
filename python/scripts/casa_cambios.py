"""
Módulo: casa_cambios.py
Descripción: Conversor de divisas con cálculo de tasas de gestión.
Objetivo: Práctica de operadores aritméticos y formateo de moneda.
"""

def calcular_cambio():
    # 1. Configuración de constantes (Tasas del día)
    TASA_CAMBIO = 1.2  # 1 EUR = 1.2 USD
    COMISION_PORCENTAJE = 0.10  # 10% de comisión

    print("--- 🏦 SISTEMA DE CASA DE CAMBIOS ---")
    
    # 2. Entrada de datos
    euros = float(input("Introduce la cantidad de Euros (€) a cambiar: "))

    # 3. Cálculos lógicos
    total_dolares_bruto = euros * TASA_CAMBIO
    comision_casa = total_dolares_bruto * COMISION_PORCENTAJE
    total_usuario = total_dolares_bruto - comision_casa

    # 4. Desglose formateado (usando .2f para mostrar solo 2 decimales)
    print("\n" + "="*30)
    print("      RESUMEN DE OPERACIÓN")
    print("="*30)
    print(f"Monto recibido:      {euros:>10.2f} €")
    print(f"Cambio (1.20):       {total_dolares_bruto:>10.2f} $")
    print(f"Tasa gestión (10%):  {comision_casa:>10.2f} $")
    print("-" * 30)
    print(f"TOTAL A RECIBIR:     {total_usuario:>10.2f} $")
    print("="*30)

if __name__ == "__main__":
    calcular_cambio()
