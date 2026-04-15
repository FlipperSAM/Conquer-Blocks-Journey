# 👥 Caso de Estudio: Gestión de Usuarios con IF-ELIF-ELSE

En este ejercicio se aplica la lógica de **Control de Flujo** para gestionar el acceso a un sistema basado en nombres de usuario específicos.

### Conceptos Aplicados:
*   **Normalización Pre-Comparación:** Antes de entrar al `if`, el dato se limpia de caracteres como `#` o `.` y se pasa a `.lower()`. Esto garantiza que `Se#rgio`, `SERGIO` y `sergio` sean tratados igual.
*   **Estructura ELIF:** Se utiliza `elif` en lugar de múltiples `if` independientes. Esto es más eficiente ya que, una vez que Python encuentra una coincidencia, deja de evaluar las demás condiciones.
*   **Cláusula ELSE (Default):** Funciona como un "atrapalotodo" para el usuario invitado, asegurando que el programa siempre dé una respuesta.

> **Importancia:** Esta es la base de los sistemas de autenticación y autorización en cualquier aplicación Backend en España.
