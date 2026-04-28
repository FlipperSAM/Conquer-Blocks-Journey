"""
PROYECTO: Gestión de Turnos con IA
PROFESIÓN: Ingeniero / Peluquero
TEMA: Listas y Bucles (Práctica de Clase)
"""

# Definición de datos maestros
servicios = ["Corte", "Barba", "Color", "Tratamiento Capilar"]
clientes_espera = ["Carlos", "Marta", "Jorge", "Elena", "Andrés"]

def mostrar_menu():
    print("\n--- SERVICIOS DISPONIBLES (Uso de for + enumerate) ---")
    for i, servicio in enumerate(servicios, 1):
        print(f"{i}. {servicio}")

def procesar_cola():
    print(f"\n--- INICIO DE JORNADA (Uso de while) ---")
    print(f"Clientes iniciales: {len(clientes_espera)}")
    
    while clientes_espera:
        # Extraemos al primer cliente de la lista
        cliente_actual = clientes_espera.pop(0)
        print(f">> Atendiendo a: {cliente_actual}")
        
        # Ejemplo de List Comprehension: Filtrar nombres con más de 5 letras
        # mientras procesamos el resto
        pendientes_largos = [c for c in clientes_espera if len(c) > 5]
        if pendientes_largos:
            print(f"   (Nota: En cola quedan nombres largos: {pendientes_largos})")

    print("\n✅ Jornada finalizada: No quedan clientes en la lista.")

if __name__ == "__main__":
    mostrar_menu()
    procesar_cola()
