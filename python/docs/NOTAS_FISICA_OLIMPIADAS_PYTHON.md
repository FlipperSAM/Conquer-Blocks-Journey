# Física con Python: Cálculo de Velocidad Media

En el desarrollo de software para deportes de alto rendimiento (como el **Skeleton**), la precisión en la conversión de unidades es crítica.

### Lógica de Conversión
Para obtener la velocidad en **m/s**, es necesario llevar todas las medidas de tiempo a una unidad común (segundos):
- **Minutos a segundos:** Multiplicamos por 60.
- **Centésimas a segundos:** Dividimos por 100.

### Aplicación de Fórmulas
Utilizamos la fórmula clásica de la física:  
`Velocidad = Distancia (m) / Tiempo (s)`

### Buenas Prácticas Implementadas
- **Modularidad:** Uso de funciones para evitar repetir código por cada atleta.
- **Formateo de Salida:** Uso de `: .2f` para asegurar que los resultados de velocidad tengan una precisión de dos decimales, evitando strings infinitos de números.
