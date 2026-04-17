"""
Módulo: gestion_inventario_bySam.py
Descripción: Sistema básico de gestión de stock utilizando listas.
Conceptos: Mutabilidad, indexación y métodos de lista (.append, .insert, .remove).
"""

def administrar_inventario():
    # 1. Creación de la lista inicial (Colección de datos)
    inventario = ["Laptop", "Mouse", "Teclado"]
    print(f"📦 Inventario inicial: {inventario}")

    # 2. .append() - Añadir un producto al final
    inventario.append("Monitor")
    print(f"➕ Tras append (Monitor): {inventario}")

    # 3. .insert() - Añadir en una posición específica (ej. posición 1)
    inventario.insert(1, "Webcam")
    print(f"📍 Tras insert en pos 1 (Webcam): {inventario}")

    # 4. Modificación por índice
    inventario[0] = "MacBook Pro"
    print(f"📝 Tras modificar índice 0: {inventario}")

    # 5. .remove() - Eliminar por nombre
    inventario.remove("Mouse")
    print(f"🗑️  Tras remove (Mouse): {inventario}")

    # 6. len() - Consultar tamaño del inventario
    print(f"\n✅ Total de productos en stock: {len(inventario)}")
    print(f"📋 Lista final optimizada: {inventario}")

if __name__ == "__main__":
    administrar_inventario()
