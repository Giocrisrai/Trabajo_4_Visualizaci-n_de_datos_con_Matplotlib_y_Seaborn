# Trabajo 4: Visualización de datos con Matplotlib y Seaborn

## 📊 Descripción del Proyecto

Este proyecto implementa un análisis completo de visualización de datos utilizando las bibliotecas **Matplotlib** y **Seaborn** para analizar un conjunto de datos de ventas minoristas del Superstore 2012. El objetivo es crear visualizaciones univariantes, bivariantes y multivariantes que permitan extraer insights valiosos del dataset.

## 🎯 Objetivos

- Crear visualizaciones univariantes, bivariantes y multivariantes con Matplotlib
- Implementar gráficos avanzados con Seaborn
- Preparar y manejar datos con Pandas
- Organizar múltiples visualizaciones en subplots
- Personalizar gráficos con títulos, etiquetas y paletas de colores
- Guardar visualizaciones como archivos de imagen
- Documentar conclusiones obtenidas de cada visualización

## 📁 Estructura del Proyecto

```
Trabajo_4_Visualizaci-n_de_datos_con_Matplotlib_y_Seaborn/
├── README.md                              # Este archivo
├── trabajo4_visualizacion_superstore.py   # Script principal
├── superstore_dataset2012.csv             # Dataset de ventas
└── fig_superstore_overview.png            # Figura generada
```

## 🚀 Instalación y Configuración

### Requisitos del Sistema

- Python 3.7+
- pip (gestor de paquetes de Python)

### Dependencias

```bash
pip install pandas matplotlib seaborn numpy
```

### Instalación

1. Clona o descarga este repositorio
2. Navega al directorio del proyecto:
   ```bash
   cd Trabajo_4_Visualizaci-n_de_datos_con_Matplotlib_y_Seaborn
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## 📊 Dataset

**Archivo**: `superstore_dataset2012.csv`

El dataset contiene información de ventas minoristas con las siguientes columnas principales:
- `Order Date`: Fecha de pedido
- `Ship Date`: Fecha de envío
- `Sales`: Ventas
- `Profit`: Beneficio
- `Quantity`: Cantidad
- `Discount`: Descuento
- `Category`: Categoría del producto
- `Sub-Category`: Subcategoría
- `Segment`: Segmento de cliente
- `Region`: Región

## 🔧 Uso

### Ejecución del Script

```bash
python trabajo4_visualizacion_superstore.py
```

### Funcionalidades Principales

El script incluye las siguientes funcionalidades:

1. **Carga inteligente de datos**: Detecta automáticamente los nombres de columnas
2. **Preparación de datos**: Conversión de fechas y limpieza de datos
3. **Visualizaciones individuales**: Cada gráfico se muestra por separado
4. **Figura resumen**: Subplot con 4 visualizaciones organizadas
5. **Guardado automático**: La figura se guarda como `fig_superstore_overview.png`

## 📈 Visualizaciones Implementadas

### 1. Visualizaciones Univariantes

#### Matplotlib - Histograma de Ventas
- **Tipo**: Histograma
- **Variable**: Distribución de ventas
- **Insight**: Identifica patrones de distribución y valores atípicos

#### Seaborn - Boxplot de Beneficio por Categoría
- **Tipo**: Boxplot
- **Variables**: Beneficio agrupado por categoría
- **Insight**: Compara la variabilidad del beneficio entre categorías

### 2. Visualizaciones Bivariantes

#### Matplotlib - Dispersión Ventas vs Beneficio
- **Tipo**: Gráfico de dispersión
- **Variables**: Ventas (X) vs Beneficio (Y)
- **Insight**: Analiza la relación entre volumen de ventas y rentabilidad

#### Seaborn - Regresión Ventas vs Beneficio
- **Tipo**: Gráfico de dispersión con línea de regresión
- **Variables**: Ventas (X) vs Beneficio (Y)
- **Insight**: Muestra la tendencia y correlación entre variables

### 3. Visualizaciones Multivariantes

#### Seaborn - Heatmap de Correlación
- **Tipo**: Matriz de correlación
- **Variables**: Todas las variables numéricas
- **Insight**: Identifica relaciones lineales entre múltiples variables

### 4. Figura Resumen (Subplots)

La figura final incluye 4 visualizaciones organizadas en una cuadrícula 2x2:
1. Histograma de Ventas
2. Boxplot de Beneficio por Segmento
3. Dispersión Ventas vs Beneficio
4. Línea de Ventas por Mes

## 🎨 Características Técnicas

### Personalización
- **Títulos descriptivos**: Cada gráfico incluye títulos claros
- **Etiquetas de ejes**: Nombres descriptivos para X e Y
- **Paletas de colores**: Colores consistentes y profesionales
- **Estilos**: Uso de estilos Seaborn para mejor apariencia

### Robustez
- **Detección automática de columnas**: Maneja diferentes formatos de nombres
- **Manejo de errores**: Verificación de existencia de archivos y columnas
- **Limpieza de datos**: Eliminación de duplicados y manejo de valores nulos

## 📋 Conclusiones Principales

### Distribución de Ventas
- La distribución muestra colas largas típicas en ventas
- Existen ventas pequeñas muy frecuentes y transacciones grandes menos comunes

### Beneficio por Categoría
- Permite comparar la mediana y dispersión del beneficio por categoría
- Identifica categorías con valores negativos o pérdidas

### Relación Ventas-Beneficio
- El patrón muestra la relación entre volumen de ventas y beneficio
- Puntos con alta venta y beneficio negativo pueden indicar descuentos excesivos

### Correlaciones
- La matriz de correlación resume relaciones lineales entre variables
- Ventas y cantidad suelen estar correlacionadas
- Los descuentos pueden afectar negativamente al beneficio

## 🛠️ Estructura del Código

### Funciones Principales

- `load_superstore()`: Carga el dataset con manejo de errores
- `smart_find()`: Detecta automáticamente nombres de columnas
- `prepare_data()`: Prepara y limpia los datos

### Flujo de Ejecución

1. **Configuración**: Importación de librerías y configuración de estilos
2. **Carga de datos**: Lectura y preparación del dataset
3. **Visualizaciones individuales**: Creación de cada gráfico por separado
4. **Figura resumen**: Organización en subplots
5. **Guardado**: Exportación de la figura final

## 📊 Resultados

El script genera:
- **5 visualizaciones individuales** mostradas en pantalla
- **1 figura resumen** con 4 subplots organizados
- **1 archivo PNG** guardado como `fig_superstore_overview.png`
- **Conclusiones detalladas** impresas en consola

## 🔍 Análisis de Datos

### Métricas Clave
- **Distribución de ventas**: Identificación de patrones y outliers
- **Rentabilidad por segmento**: Comparación de beneficios
- **Correlaciones**: Relaciones entre variables numéricas
- **Tendencias temporales**: Evolución de ventas por mes

### Insights de Negocio
- Identificación de segmentos con pérdidas
- Análisis de la efectividad de descuentos
- Patrones estacionales en las ventas
- Optimización de estrategias de pricing

## 📚 Bibliotecas Utilizadas

- **pandas**: Manipulación y análisis de datos
- **matplotlib**: Visualizaciones básicas y personalización
- **seaborn**: Visualizaciones estadísticas avanzadas
- **numpy**: Operaciones numéricas

## 🎓 Aprendizajes

Este proyecto demuestra:
- Uso efectivo de Matplotlib para visualizaciones personalizadas
- Aprovechamiento de Seaborn para análisis estadístico
- Preparación robusta de datos con Pandas
- Organización profesional de código y documentación
- Extracción de insights valiosos de datos reales

## 📝 Notas Adicionales

- El código es robusto y maneja diferentes formatos de dataset
- Las visualizaciones están optimizadas para presentación
- Se incluyen comentarios detallados para facilitar el mantenimiento
- El diseño es escalable para futuras mejoras

---

**Autor**: Giocrisrai Godoy
**Fecha**: 2025
**Curso**: Visualización de Datos con Python  
**Institución**: UNIR
