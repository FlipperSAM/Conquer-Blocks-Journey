"""
Módulo: olimpiadas_skeleton.py
Descripción: Cálculo de velocidad media en Skeleton (Olimpiadas de Invierno).
Conceptos: Conversión de tiempo, operadores aritméticos y precisión float.
"""
def calcular_velocidad_atleta(nombre):
    print(f"\n--- Datos de {nombre} ---")
    # 1. Entrada de datos por pantalla
    minutos = int(input(f"Introduce los minutos de {nombre}: "))
    segundos = int(input(f"Introduce los segundos de {nombre}: "))
    centesimas = int(input(f"Introduce las centésimas de {nombre}: "))
