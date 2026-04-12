"""
Módulo: comisiones_carros.py
Descripción: Cálculo de comisiones mensuales para vendedores de automóviles.
Modelos: RBM Serie 1, RMB Serie Plus, RBM Todoterreno.
"""

def calcular_comisiones():
    # 1. Configuración de Precios y Comisiones (Constantes)
    # Serie 1: 20k € al 3%
    # Serie Plus: 35k € al 5%
    # Todoterreno: 60k € al 7%
    
    PRECIOS = [20000, 35000, 60000]
    COMISIONES = [0.03, 0.05, 0.07]
    NOMBRES = ["RBM Serie 1", "RMB Serie Plus", "RBM Todoterreno"]

    print("--- 🚗 CÁLCULO DE COMISIONES - CONCESIONARIO RBM ---")
    
    total_comision_mes = 0

    # 2. Entrada de datos y cálculo iterativo
    for i in range(len(NOMBRES)):
        cantidad = int(input(f"¿Cuántos coches del modelo {NOMBRES[i]} has vendido?: "))
        
        # Cálculo: (Cantidad * Precio) * Porcentaje de comisión
        comision_modelo = (cantidad * PRECIOS[i]) * COMISIONES[i]
        total_comision_mes += comision_modelo
        
        print(f"-> Comisión por {NOMBRES[i]}: {comision_modelo:,.2f} €")

    # 3. Resultado final
    print("\n" + "="*35)
    print(f"TOTAL COMISIONES DEL MES: {total_comision_mes:,.2f} €")
    print("="*35)

if __name__ == "__main__":
    calcular_comisiones()
