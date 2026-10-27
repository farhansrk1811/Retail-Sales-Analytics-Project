
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "outputs" / "cleaned_superstore.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_FILE, encoding="utf-8-sig")

# Overall business KPIs
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()
total_units = df["Quantity"].sum()

# Overall profit margin: profit divided by sales
profit_margin = (
    total_profit / total_sales * 100
    if total_sales != 0 else 0
)

kpis = pd.DataFrame({
    "KPI": [
        "Total Sales",
        "Total Profit",
        "Profit Margin (%)",
        "Unique Orders",
        "Unique Customers",
        "Units Sold"
    ],
    "Value": [
        total_sales,
        total_profit,
        profit_margin,
        total_orders,
        total_customers,
        total_units
    ]
})

print("\n===== OVERALL BUSINESS KPIs =====")
print(kpis.to_string(index=False, formatters={"Value": "{:,.2f}".format}))

# Category performance
category_performance = (
    df.groupby("Category", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Units_Sold=("Quantity", "sum"),
        Orders=("Order ID", "nunique")
    )
)

category_performance["Profit_Margin_Pct"] = (
    category_performance["Profit"]
    / category_performance["Sales"] * 100
)

category_performance = category_performance.sort_values(
    "Sales", ascending=False
)

print("\n===== CATEGORY PERFORMANCE =====")
print(category_performance.to_string(
    index=False,
    formatters={
        "Sales": "{:,.2f}".format,
        "Profit": "{:,.2f}".format,
        "Profit_Margin_Pct": "{:.2f}%".format
    }
))

# Regional performance
regional_performance = (
    df.groupby("Region", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order ID", "nunique")
    )
)

regional_performance = regional_performance.sort_values(
    "Sales", ascending=False
)

print("\n===== REGIONAL PERFORMANCE =====")
print(regional_performance.to_string(
    index=False,
    formatters={
        "Sales": "{:,.2f}".format,
        "Profit": "{:,.2f}".format
    }
))

# Save results for Power BI and the project report
kpis.to_csv(
    OUTPUT_DIR / "overall_kpis.csv",
    index=False,
    encoding="utf-8-sig"
)

category_performance.to_csv(
    OUTPUT_DIR / "category_performance.csv",
    index=False,
    encoding="utf-8-sig"
)

regional_performance.to_csv(
    OUTPUT_DIR / "regional_performance.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nKPI analysis complete.")
print("Results saved in:", OUTPUT_DIR)
