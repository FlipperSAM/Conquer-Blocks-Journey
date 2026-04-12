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
    
    # 2. Conversión total a segundos
    # 1 min = 60 seg | 1 seg = 100 centésimas
    tiempo_total_segundos = (minutos * 60) + segundos + (centesimas / 100)
    
    # 3. Cálculo de velocidad media (Velocidad = Distancia / Tiempo)
    DISTANCIA_PISTA = 100  # Metros
    velocidad_media = DISTANCIA_PISTA / tiempo_total_segundos

    return tiempo_total_segundos, velocidad_media

def iniciar_competicion():
    finalistas = ["Hannah Neise", "Jackie Narracott", "Kimberley Bos"]
    
    print("🏆 COMPETICIÓN DE SKELETON - OLIMPIADAS DE INVIERNO")
    
    for atleta in finalistas:
        tiempo, velocidad = calcular_velocidad_atleta(atleta)
        # 4. Impresión de resultados con formato profesional
        print(f"⏱️ Tiempo total: {tiempo:.2f} segundos")
        print(f"⚡ Velocidad media: {velocidad:.2f} m/s")

if __name__ == "__main__":
    iniciar_competicion()
