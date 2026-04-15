"""
Módulo: test_condicionales_pro.py
Descripción: Aplicación práctica de lógica condicional (if-elif-else) y operadores lógicos.
"""

def test_acceso():
    edad = 20
    tiene_entrada = True
    esta_en_lista = False

    # Ejemplo de lógica combinada (AND / OR)
    if (edad >= 18 and tiene_entrada) or esta_en_lista:
        print("✅ Acceso concedido.")
    else:
        print("🛑 Acceso denegado.")

if __name__ == "__main__":
    test_acceso()
