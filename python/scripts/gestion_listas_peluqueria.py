"""
PROYECTO: IA BarberFlow - Gestión de Turnos Avanzada
PROFESIÓN: Ingeniero / Peluquero
TEMA: Listas, Slicing y Estadística (Clase 2)
"""

# 1. Definición de datos (Listas Numéricas y Strings)
servicios = ["Corte", "Barba", "Color", "Tratamiento"]
precios = [15.0, 10.0, 30.0, 20.0]
clientes_espera = ["Carlos", "Marta", "Jorge", "Elena", "Andrés", "Lucía"]

def reporte_financiero():
    # --- Uso de Funciones Matemáticas ---
    total_potencial = sum(precios)
    servicio_top = max(precios)
    
    print("\n--- ANÁLISIS DE NEGOCIO (Estadística Rápida) ---")
    print(f"Ingreso total previsto: {total_potencial}€")
    print(f"Tarifa máxima actual: {servicio_top}€")

def mostrar_agenda_segmentada():
    # --- Uso de Slicing (Porciones de lista) ---
    # Dividimos la jornada: los 3 primeros son el "Turno Mañana"
    turno_manana = clientes_espera[:3]
    turno_tarde = clientes_espera[3:]
    
    print("\n--- ORGANIZACIÓN DE JORNADA (Slicing) ---")
    print(f"Mañana (Prioridad): {turno_manana}")
    print(f"Tarde (Pendientes): {turno_tarde}")

def procesar_jornada():
    print("\n--- INICIO DE ATENCIÓN (Bucle While + FIFO) ---")
    
    while clientes_espera:
        # Extraemos al primer cliente (Lógica de cola real)
        cliente_actual = clientes_espera.pop(0)
        print(f"Atendiendo a: {cliente_actual}...")
        
        # --- List Comprehension ---
        # Filtramos nombres cortos para una promoción rápida
        promo_rapida = [c for c in clientes_espera if len(c) <= 5]
        if promo_rapida:
            print(f"   > IA Sugerencia: Ofrecer promo rápida a {promo_rapida}")

if __name__ == "__main__":
    # Ejecutamos las funciones que demuestran el dominio de la Clase 2
    mostrar_agenda_segmentada()
    reporte_financiero()
    procesar_jornada()
    print("\n✅ Sistema actualizado y jornada cerrada.")
