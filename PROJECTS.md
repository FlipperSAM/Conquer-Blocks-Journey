# Proyectos Prácticos de Aplicación

A continuación, se detallan los proyectos prácticos desarrollados para consolidar los conocimientos de estadística, visualización y muestreo utilizando entornos de desarrollo en Python.

---

## Proyecto 1: Análisis Exploratorio y Estimación Salarial (EDA)
**Conceptos aplicados:** Estadística Descriptiva, Medidas de Tendencia Central y Librería Seaborn.  
**Dataset:** `Anual Salary reports survey` (Kaggle).

### Objetivos del Proyecto
1. **Limpieza e Inspección:** Cargar el dataset de 100,000 registros y verificar la consistencia de las columnas (`income`, `age`, `education_level`).
2. **Análisis Estadístico:** Calcular de forma manual y automatizada la media, mediana y moda del ingreso anual (`income`). Identificar si existen valores atípicos (*outliers*) comparando la media con la mediana.
3. **Visualización Avanzada:** 
   * Construir un **Histograma** con una curva de densidad de kernel (KDE) para evaluar el sesgo de los salarios.
   * Diseñar un **Gráfico de Cajas (Box plot)** segmentado por `gender` y `education_level` para analizar la dispersión y las brechas salariales.

```python
# Código base para iniciar el proyecto
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("anual_salary_reports_survey.csv")
print(df.describe()) # Resumen estadístico inicial
```

---

## Proyecto 2: Clasificación Biométrica y Correlación Estructural
**Conceptos aplicados:** Correlación (Pearson y Spearman), Gráficos de Dispersión, Violín y Mapas de Calor.  
**Dataset:** `Iris Dataset`.

### Objetivos del Proyecto
1. **Análisis de Correlación Cruzada:** Generar una matriz de correlación de Pearson entre las dimensiones de los sépalos y pétalos. Visualizarla usando un **Mapa de Calor (Heatmap)** con una paleta divergente (`coolwarm`) para identificar qué variables están altamente correlacionadas.
2. **Patrones Geométricos:** Crear un **Gráfico de Dispersión (Scatter plot)** mapeando `Petal Length` vs `Petal Width`, utilizando el argumento `hue='Species'` para comprobar visualmente cómo la probabilidad de distribución de las clases se separa de forma natural en el espacio plano.
3. **Distribución de Densidad:** Construir **Gráficos de Violín** para la variable `Sepal Length` agrupada por especie, demostrando visualmente la multimodalidad y la concentración de los datos en comparación con un Box plot tradicional.

---

## Proyecto 3: Simulador de Muestreo Probabilístico y Regresión Lineal
**Conceptos aplicados:** Regresión Lineal Simple, Métodos de Muestreo (Simple vs. Estratificado) y Teorema Central del Límite.  
**Dataset:** Sintético / Modificación del Dataset de Salarios.

### Objetivos del Proyecto
1. **Modelado Predictivo:** Ajustar una línea de **Regresión Lineal** (\(y = a + bx\)) para predecir el salario (`income`) de un candidato utilizando únicamente su edad (`age`) como variable independiente.
2. **Experimento de Muestreo:**
   * Extraer una **Muestra Aleatoria Simple** del 5% del dataset.
   * Extraer una **Muestra Estratificada** del 5% manteniendo la proporción exacta del nivel educativo (`education_level`).
3. **Evaluación de Errores:** Calcular la media del salario en ambas muestras y compararla con la media real de la población (los 100,000 registros). Graficar el error de estimación para demostrar matemáticamente por qué el muestreo estratificado reduce la varianza del estimador cuando existen subgrupos marcados.

```python
# Demostración del impacto del muestreo en el cálculo de la media
media_poblacion = df['income'].mean()
media_simple = df.sample(frac=0.05, random_state=42)['income'].mean()
print(f"Error Muestreo Simple: {abs(media_poblacion - media_simple):.2f}")
```
