"""
Módulo: control_aeropuerto.py
Descripción: Sistema lógico de seguridad y acceso de pasajeros.
Conceptos: Operadores lógicos (and, or), comparaciones numéricas y condicionales.
"""

def control_seguridad():
    print("--- ✈️ SISTEMA DE SEGURIDAD AEROPORTUARIO ---")

    # 1. Datos del pasajero
    edad = int(input("Introduce tu edad: "))
    tiene_pasaporte = input("¿Tienes pasaporte vigente? (si/no): ").lower() == "si"
    bolsos_sospechosos = input("¿Llevas objetos prohibidos? (si/no): ").lower() == "si"
    es_menor_acompanado = False

    if edad < 18:
        es_menor_acompanado = input("¿Vas acompañado de un adulto? (si/no): ").lower() == "si"

    # 2. Lógica de Control con Operadores Lógicos
    # REGLA 1: Debe tener pasaporte Y NO llevar objetos prohibidos
    # REGLA 2: Si es menor, DEBE ir acompañado
    
    puede_viajar = tiene_pasaporte and not bolsos_sospechosos
    
    if edad < 18 and not es_menor_acompanado:
        puede_viajar = False

    # 3. Toma de decisiones (IF-ELIF-ELSE)
    print("\n" + "="*30)
    if bolsos_sospechosos:
        print("🛑 ALERTA: Acceso denegado por seguridad.")
    elif not tiene_pasaporte:
        print("🛂 TRÁMITE: Acceso denegado. Sin pasaporte.")
    elif puede_viajar:
        print("✅ BIENVENIDO: Puede pasar a la zona de embarque.")
    else:
        print("⚠️ AVISO: Menores de edad requieren acompañante.")
    print("="*30)

if __name__ == "__main__":
    control_seguridad()
