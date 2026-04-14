"""
Módulo: calculadora_ahorros.py
Descripción: Sistema de cálculo de finanzas personales (ingresos vs gastos).
Objetivo: Determinar la capacidad de ahorro anual y análisis de escenarios.
"""

def calcular_finanzas():
    print("--- 💰 CALCULADORA DE AHORROS ANUALES ---")

    # 1. Saludo personalizado
    nombre = input("¿Cómo te llamas?: ").title()
    print(f"Hola {nombre}\n")

    # 2 y 3. Cálculo de ingresos semanales
    ingreso_hora = float(input("¿Cuánto ganas por hora (€)?: "))
    horas_semana = float(input("¿Cuántas horas trabajas a la semana?: "))
    salario_semanal = ingreso_hora * horas_semana

    # 4 y 5. Ganancias anuales (52 semanas tiene un año)
    ganancias_anuales = salario_semanal * 52
    print(f"\n{nombre} tiene unas ganancias anuales de: {ganancias_anuales:,.2f} euros")

    # 6 y 7. Gastos
    gasto_semanal = float(input("¿Cuáles son tus gastos semanales (€)?: "))
    gasto_anual = gasto_semanal * 52

    # 8 y 9. Cálculo de ahorros (Ingresos - Gastos)
    ahorro_anual = ganancias_anuales - gasto_anual

    # 10. Resultados generales
    print("-" * 35)
    print(f"RESULTADOS PARA {nombre.upper()}")
    print(f"Gasto anual total: {gasto_anual:,.2f} €")
    print(f"Ahorro anual neto: {ahorro_anual:,.2f} €")
    print("-" * 35)

    # ESCENARIO EXTRA: Tiempo parcial (25h) y reducción de gastos (3/4)
    print("\n--- 📉 ANÁLISIS ESCENARIO TIEMPO PARCIAL ---")
    nuevas_horas = 25
    nuevos_gastos_sem = gasto_semanal * (3/4)
    
    nuevo_salario_anual = (ingreso_hora * nuevas_horas) * 52
    nuevo_gasto_anual = nuevos_gastos_sem * 52
    nuevo_balance = nuevo_salario_anual - nuevo_gasto_anual

    if nuevo_balance >= 0:
        print(f"Resultado: ¡SÍ! Tendrías un ahorro de {nuevo_balance:,.2f} € anuales.")
    else:
        print(f"Resultado: NO. Tendrías un déficit de {abs(nuevo_balance):,.2f} € anuales.")

if __name__ == "__main__":
    calcular_finanzas()
