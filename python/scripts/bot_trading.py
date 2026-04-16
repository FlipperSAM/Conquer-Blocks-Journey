"""
Módulo: bot_trading.py
Descripción: Simulación de órdenes de compra, venta y espera (HOLD) para activos financieros.
Conceptos: Control de flujo, lógica de rangos y toma de decisiones automatizada.
"""

def ejecutar_bot():
    print("--- 📈 RBM TRADING BOT: MÓDULO DE EJECUCIÓN ---")
    
    try:
        precio = float(input("Introduce el precio actual del activo ($): "))

        # Lógica de Trading (Reglas de Negocio)
        if precio < 100:
            print("🚀 ACCIÓN: COMPRAR (Precio por debajo del valor objetivo)")
        elif 100 <= precio <= 150:
            print("⚖️ ACCIÓN: HOLD (Precio en rango de estabilidad)")
        else:
            print("💰 ACCIÓN: VENDER (Precio por encima del objetivo - Toma de ganancias)")

    except ValueError:
        print("❌ ERROR: El precio debe ser un valor numérico.")

if __name__ == "__main__":
    ejecutar_bot()
