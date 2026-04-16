"""
Módulo: hamburgueseria_online.py
Descripción: Sistema de pedidos dinámico con selección de ingredientes según tipo de producto.
Conceptos: Menús anidados y validación de strings.
"""

def hacer_pedido():
    print("--- 🍔 RBM BURGER ONLINE ---")
    tipo = input("¿Deseas una hamburguesa Clásica o Vegana?: ").lower()

    if tipo == "clásica" or tipo == "clasica":
        print("Ingredientes extra: Queso Idiazabal, Bacon, Huevo")
        extra = input("Elige uno: ").title()
        print(f"\nHas elegido una Hamburguesa Clásica con {extra}. ¡Buen provecho!")
    elif tipo == "vegana":
        print("Ingredientes extra: Tofu, Cebolla caramelizada")
        extra = input("Elige uno: ").title()
        print(f"\nHas elegido una Hamburguesa Vegana con {extra}. ¡Disfruta tu opción healthy!")
    else:
        print("❌ Tipo de hamburguesa no disponible.")

if __name__ == "__main__":
    hacer_pedido()
