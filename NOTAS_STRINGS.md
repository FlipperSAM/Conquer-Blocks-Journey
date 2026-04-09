# 🐍 Manipulación de Strings en Python

En el desarrollo profesional, los datos que vienen del usuario suelen estar "sucios". Python ofrece herramientas potentes para estandarizarlos antes de procesarlos.

### Métodos de Formato Esenciales
- `.upper()`: Convierte todo el texto a **MAYÚSCULAS**. Útil para destacar mensajes importantes.
- `.lower()`: Convierte todo a **minúsculas**. Es la mejor práctica para comparar datos de forma segura.
- `.title()`: Pone la **primera letra en mayúscula** (ej. `sam` -> `Sam`). Ideal para nombres propios.
- `.replace(viejo, nuevo)`: Busca un carácter y lo reemplaza. Lo usamos para eliminar errores como puntos innecesarios (`"."`, `""`).

### ¿Por qué usamos f-strings?
Desde Python 3.6+, las **f-strings** (`f"Hola {nombre}"`) son el estándar de la industria en España y el mundo. Son más rápidas, legibles y fáciles de mantener que los métodos antiguos.
