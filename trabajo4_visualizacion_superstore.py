"""
Trabajo 4: Visualización de datos con Matplotlib y Seaborn
Dataset: superstore_dataset2012.csv

Este script:
- Carga y prepara datos de ventas minoristas
- Genera visualizaciones (univariantes, bivariantes, multivariantes)
- Organiza subplots
- Guarda una figura de salida
- Incluye comentarios con conclusiones
"""

# =========================
# 1. Imports y configuración
# =========================
import warnings
warnings.filterwarnings("ignore")

import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-whitegrid")
sns.set_theme(context="notebook", style="whitegrid", palette="deep")

# =========================
# 2. Carga y preparación
# =========================
DATA_PATH = "superstore_dataset2012.csv"  # ajusta si lo necesitas

def load_superstore(path: str) -> pd.DataFrame:
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"No se encontró el archivo '{path}'. "
            "Asegúrate de que está en el directorio de trabajo o ajusta DATA_PATH."
        )
    df = pd.read_csv(path, encoding="utf-8", low_memory=False)
    return df

def smart_find(df: pd.DataFrame, candidates):
    """Devuelve la primera columna existente de la lista candidates (ignora mayúsculas/minúsculas y espacios)."""
    normalized = {c.lower().strip(): c for c in df.columns}
    for cand in candidates:
        key = cand.lower().strip()
        if key in normalized:
            return normalized[key]
    # prueba aproximada quitando espacios y guiones
    normalized2 = {c.lower().replace(" ", "").replace("-", ""): c for c in df.columns}
    for cand in candidates:
        key = cand.lower().replace(" ", "").replace("-", "")
        if key in normalized2:
            return normalized2[key]
    return None

def prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    # Columnas candidatas frecuentes en distintos Superstore
    col_order_date = smart_find(df, ["Order Date", "OrderDate", "Date"])
    col_ship_date  = smart_find(df, ["Ship Date", "ShipDate"])
    col_sales      = smart_find(df, ["Sales", "Venta", "Ventas"])
    col_profit     = smart_find(df, ["Profit", "Beneficio", "Profit/Loss"])
    col_quantity   = smart_find(df, ["Quantity", "Qty", "Unidades"])
    col_discount   = smart_find(df, ["Discount", "Descuento"])
    col_category   = smart_find(df, ["Category", "Categoría"])
    col_subcat     = smart_find(df, ["Sub-Category", "SubCategory", "Subcategoría"])
    col_segment    = smart_find(df, ["Segment", "Segmento"])
    col_region     = smart_find(df, ["Region", "Región"])

    # Conversión de fechas
    if col_order_date:
        df[col_order_date] = pd.to_datetime(df[col_order_date], errors="coerce")
        df["OrderMonth"] = df[col_order_date].dt.to_period("M").dt.to_timestamp()
    if col_ship_date and col_ship_date != col_order_date:
        df[col_ship_date] = pd.to_datetime(df[col_ship_date], errors="coerce")

    # Mantener solo columnas útiles si existen
    keep_cols = [c for c in [col_order_date, col_ship_date, col_sales, col_profit,
                             col_quantity, col_discount, col_category, col_subcat,
                             col_segment, col_region, "OrderMonth"] if c is not None]
    df = df[keep_cols].copy()

    # Eliminación de duplicados y nulos obvios
    df.drop_duplicates(inplace=True)

    # Rellenos simples o eliminación si fuera crítico
    if col_sales and df[col_sales].isna().any():
        df[col_sales] = df[col_sales].fillna(0)
    if col_profit and df[col_profit].isna().any():
        df[col_profit] = df[col_profit].fillna(0)

    return df, {
        "order_date": col_order_date, "ship_date": col_ship_date,
        "sales": col_sales, "profit": col_profit, "quantity": col_quantity,
        "discount": col_discount, "category": col_category, "subcat": col_subcat,
        "segment": col_segment, "region": col_region
    }

# Carga
df_raw = load_superstore(DATA_PATH)
df, cols = prepare_data(df_raw)

print("Columnas identificadas:", cols)
print("Muestra de datos preparados:\n", df.head(), "\n")

# =========================
# 3. Visualizaciones
# =========================

# ---------- Univariante con Matplotlib: Histograma de Ventas ----------
if cols["sales"]:
    fig1, ax1 = plt.subplots(figsize=(7, 4))
    ax1.hist(df[cols["sales"]], bins=40, color="#2E86C1", alpha=0.8, edgecolor="white")
    ax1.set_title("Distribución de Ventas (Matplotlib)", fontsize=12, weight="bold")
    ax1.set_xlabel("Ventas")
    ax1.set_ylabel("Frecuencia")
    plt.tight_layout()
    plt.show()

    # Conclusión:
    print("Conclusión (Histograma de Ventas):")
    print("- La distribución permite observar colas largas típicas en ventas; "
          "existen ventas pequeñas muy frecuentes y algunas transacciones grandes menos comunes.\n")

# ---------- Univariante con Seaborn: Boxplot de Beneficio por Categoría ----------
if cols["profit"] and cols["category"]:
    fig2, ax2 = plt.subplots(figsize=(7, 4))
    sns.boxplot(data=df, x=cols["category"], y=cols["profit"], ax=ax2, palette="pastel")
    ax2.set_title("Beneficio por Categoría (Seaborn - Boxplot)", fontsize=12, weight="bold")
    ax2.set_xlabel("Categoría")
    ax2.set_ylabel("Beneficio")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

    print("Conclusión (Boxplot Beneficio por Categoría):")
    print("- Podemos comparar la mediana y la dispersión del beneficio por categoría; "
          "categorías con muchos valores negativos/pérdidas pueden aparecer claramente.\n")

# ---------- Bivariante con Matplotlib: Dispersión Ventas vs Beneficio ----------
if cols["sales"] and cols["profit"]:
    fig3, ax3 = plt.subplots(figsize=(7, 4))
    ax3.scatter(df[cols["sales"]], df[cols["profit"]], s=15, alpha=0.6, c="#8E44AD")
    ax3.set_title("Relación Ventas vs Beneficio (Matplotlib)", fontsize=12, weight="bold")
    ax3.set_xlabel("Ventas")
    ax3.set_ylabel("Beneficio")
    plt.tight_layout()
    plt.show()

    print("Conclusión (Dispersión Ventas vs Beneficio):")
    print("- El patrón muestra la relación entre el volumen de ventas y el beneficio. "
          "Si hay puntos con alta venta y beneficio negativo, podrían indicar descuentos excesivos o costes elevados.\n")

# ---------- Bivariante con Seaborn: Regresión Ventas vs Beneficio ----------
if cols["sales"] and cols["profit"]:
    fig4, ax4 = plt.subplots(figsize=(7, 4))
    sns.regplot(
        data=df, x=cols["sales"], y=cols["profit"], scatter_kws={"alpha":0.4, "s":15}, ax=ax4, color="#27AE60"
    )
    ax4.set_title("Relación Ventas vs Beneficio con Regresión (Seaborn)", fontsize=12, weight="bold")
    ax4.set_xlabel("Ventas")
    ax4.set_ylabel("Beneficio")
    plt.tight_layout()
    plt.show()

    print("Conclusión (Regresión Ventas vs Beneficio):")
    print("- La recta de regresión permite observar si el beneficio tiende a aumentar con las ventas. "
          "Si la pendiente es baja o negativa, hay oportunidades de optimización.\n")

# ---------- Multivariante con Seaborn: Heatmap de correlación ----------
numeric_cols = df.select_dtypes(include=[np.number]).columns
if len(numeric_cols) >= 2:
    corr = df[numeric_cols].corr(method="pearson")
    fig5, ax5 = plt.subplots(figsize=(6, 5))
    sns.heatmap(corr, cmap="vlag", annot=True, fmt=".2f", linewidths=.5, ax=ax5, cbar_kws={"shrink": .8})
    ax5.set_title("Matriz de Correlación (Seaborn - Heatmap)", fontsize=12, weight="bold")
    plt.tight_layout()
    plt.show()

    print("Conclusión (Heatmap de correlación):")
    print("- La matriz de correlación resume relaciones lineales entre variables numéricas. "
          "Por ejemplo, ventas y cantidad suelen estar correlacionadas; descuentos pueden afectar negativamente al beneficio.\n")

# ---------- Subplots: figura resumen con 4 visualizaciones ----------
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Resumen de Visualizaciones Superstore 2012", fontsize=14, weight="bold")

# (1) Histograma de Ventas
if cols["sales"]:
    axes[0, 0].hist(df[cols["sales"]], bins=35, color="#1F77B4", alpha=0.85, edgecolor="white")
    axes[0, 0].set_title("Ventas (Histograma)")
    axes[0, 0].set_xlabel("Ventas")
    axes[0, 0].set_ylabel("Frecuencia")
else:
    axes[0, 0].text(0.5, 0.5, "Ventas no disponibles", ha="center", va="center")

# (2) Boxplot Beneficio por Segmento
if cols["profit"] and cols["segment"]:
    sns.boxplot(data=df, x=cols["segment"], y=cols["profit"], ax=axes[0, 1], palette="pastel")
    axes[0, 1].set_title("Beneficio por Segmento")
    axes[0, 1].set_xlabel("Segmento")
    axes[0, 1].set_ylabel("Beneficio")
else:
    axes[0, 1].text(0.5, 0.5, "Segmento/Beneficio no disponible", ha="center", va="center")

# (3) Dispersión Ventas vs Beneficio
if cols["sales"] and cols["profit"]:
    axes[1, 0].scatter(df[cols["sales"]], df[cols["profit"]], s=12, alpha=0.45, c="#D35400")
    axes[1, 0].set_title("Ventas vs Beneficio")
    axes[1, 0].set_xlabel("Ventas")
    axes[1, 0].set_ylabel("Beneficio")
else:
    axes[1, 0].text(0.5, 0.5, "Ventas/Beneficio no disponible", ha="center", va="center")

# (4) Línea de Ventas por Mes (si hay OrderMonth)
if "OrderMonth" in df.columns and cols["sales"]:
    monthly = df.groupby("OrderMonth")[cols["sales"]].sum().sort_index()
    axes[1, 1].plot(monthly.index, monthly.values, marker="o", color="#2ECC71", linewidth=2)
    axes[1, 1].set_title("Ventas por Mes")
    axes[1, 1].set_xlabel("Mes")
    axes[1, 1].set_ylabel("Ventas")
else:
    axes[1, 1].text(0.5, 0.5, "OrderMonth/Ventas no disponible", ha="center", va="center")

plt.tight_layout(rect=[0, 0, 1, 0.96])

# Guardar la figura
OUTPUT_FIG = "fig_superstore_overview.png"
plt.savefig(OUTPUT_FIG, dpi=120)
plt.show()

print(f"Figura guardada como: {OUTPUT_FIG}\n")

# Comentario final
print("Conclusiones generales:")
print("- Las visualizaciones permiten identificar patrones clave: distribución de ventas, "
      "variabilidad del beneficio por grupos, relaciones y correlaciones entre métricas.")
print("- Úsalo como base para identificar segmentos con pérdidas o meses con caídas y plantear acciones.\n")