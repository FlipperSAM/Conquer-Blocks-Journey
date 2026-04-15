"""
Módulo: restaurante_cuenta.py
Descripción: Sistema de cálculo de cuenta para restaurante.
Estructura: Uso de diccionarios para gestión de precios.
"""

def calcular_cuenta():
    # 1. Menú organizado en un Diccionario (Clave: Platillo, Valor: Precio)
    menu = {
    
        "Ensalada mixta": 12.0,
        "Sopa de pescado": 10.0,
        "Dorada al horno": 18.0,
        "Arroz al curry": 14.0,
        "Lasaña de carne": 15.0,
        "Brownie de chocolate": 8.0,
        "Helado": 6.0,
        "Refrescos": 5.5,
        "Café": 3.5
    }

    print("--- 🍽️ SISTEMA DE GESTIÓN DE PEDIDOS ---")
    total_cuenta = 0
    resumen_pedido = []

    # 2. Proceso de toma de pedido
    for plato, precio in menu.items():
        cantidad = int(input(f"¿Cuántas unidades de '{plato}' ({precio}€) se consumieron?: "))
        
        if cantidad > 0:
            subtotal = cantidad * precio
            total_cuenta += subtotal
            resumen_pedido.append(f"{plato} x{cantidad}: {subtotal:.2f}€")

    # 3. Impresión de Ticket Profesional
    print("\n" + "—"*30)
    print("       TICKET DE VENTA")
    print("—"*30)
    for linea in resumen_pedido:
        print(linea)
    print("—"*30)
    print(f"TOTAL A PAGAR: {total_cuenta:.2f}€")
    print("—"*30)
    print("¡Gracias por su visita!")

if __name__ == "__main__":
    calcular_cuenta()
