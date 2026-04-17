# Investigación: Lógica de Control y Sentencias Condicionales

Resumen técnico basado en la investigación de estructuras de decisión en Python.

### 1. El Concepto de Flujo de Control
El flujo de ejecución de un programa es lineal por defecto. Las sentencias condicionales permiten **romper esa linealidad**, decidiendo qué bloques de código ejecutar según se cumplan o no ciertas premisas.

### 2. Estructura `if-elif-else`
*   **`if`**: La condición inicial. Si es `True`, se ejecuta su bloque.
*   **`elif` (Else If)**: Permite evaluar múltiples condiciones adicionales si la anterior fue falsa. Es más eficiente que usar muchos `if` independientes.
*   **`else`**: El bloque por defecto. Se ejecuta solo si **todas** las condiciones anteriores fueron falsas.

### 3. Operadores de Comparación y Lógica
*   **Comparación:** `==` (Igualdad), `!=` (Desigualdad), `>`, `<`, `>=`, `<=`.
*   **Lógicos:** 
    *   `and`: Requiere que ambos lados sean `True`.
    *   `or`: Requiere que al menos un lado sea `True`.
    *   `not`: Invierte el valor de verdad.

> **💡 Dato Pro:** En Python, la **indentación** (los 4 espacios) no es estética, es obligatoria para definir qué código pertenece a cada condicional.
