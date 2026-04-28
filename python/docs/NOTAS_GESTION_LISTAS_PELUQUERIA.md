# Gestión de Colecciones e Iteración Automatizada (Peluquería)

En este bloque aplico el manejo de listas y bucles para resolver la problemática real de la organización de turnos y el flujo de trabajo en una barbería/peluquería.

### Puntos Clave:

*   **Lógica de Cola Real (FIFO):** Mediante el uso de `.pop(0)` en la lista de `clientes_espera`, el software replica el orden de llegada de la peluquería. Esto garantiza que el sistema sea justo y no pierda el hilo de quién es el siguiente.
*   **Automatización de Menús con `enumerate()`:** En lugar de escribir cada servicio a mano, el bucle `for` recorre la lista `servicios`. Esto permite que el negocio sea escalable: si mañana añades "Corte de Barba", el sistema lo numera y lo muestra automáticamente.
*   **Auditoría en Tiempo Real (List Comprehensions):** Implementé esta técnica para que, mientras el barbero trabaja, el sistema pueda filtrar información al instante (como identificar nombres largos o servicios específicos) sin detener el proceso principal.
*   **Estado Operativo con `while`:** El programa utiliza la propia lista de clientes como condición de parada. Mientras existan elementos en la cola, el "negocio" sigue funcionando, simulando una jornada laboral completa.

**Nota de Ingeniero:** He diseñado este script para que la estructura de datos sea el corazón de la lógica. La lista no es solo un contenedor, es el motor que decide quién sigue y cuándo termina la jornada.
