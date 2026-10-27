
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "outputs" / "cleaned_superstore.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
CHART_DIR = OUTPUT_DIR / "charts"

CHART_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA_FILE, encoding="utf-8-sig")
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="raise")

sns.set_theme(style="whitegrid")

# 1. Sales by category
category_sales = df.groupby("Category")["Sales"].sum().sort_values()

plt.figure(figsize=(9, 5))
category_sales.plot(kind="barh")
plt.title("Total Sales by Product Category")
plt.xlabel("Sales")
plt.ylabel("Category")
plt.tight_layout()
plt.savefig(CHART_DIR / "sales_by_category.png", dpi=300)
plt.close()

# 2. Profit by category
category_profit = df.groupby("Category")["Profit"].sum().sort_values()

plt.figure(figsize=(9, 5))
category_profit.plot(kind="barh")
plt.title("Total Profit by Product Category")
plt.xlabel("Profit")
plt.ylabel("Category")
plt.tight_layout()
plt.savefig(CHART_DIR / "profit_by_category.png", dpi=300)
plt.close()

# 3. Monthly sales trend
monthly_sales = (
    df.set_index("Order Date")["Sales"]
    .resample("MS")
    .sum()
)

plt.figure(figsize=(12, 5))
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Order Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig(CHART_DIR / "monthly_sales_trend.png", dpi=300)
plt.close()

# 4. Profit versus discount
plt.figure(figsize=(9, 5))
sns.scatterplot(
    data=df,
    x="Discount",
    y="Profit",
    hue="Category",
    alpha=0.6
)
plt.title("Profit versus Discount by Category")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig(CHART_DIR / "profit_vs_discount.png", dpi=300)
plt.close()

# 5. Profit by region
regional_profit = df.groupby("Region")["Profit"].sum().sort_values()

plt.figure(figsize=(9, 5))
regional_profit.plot(kind="barh")
plt.title("Total Profit by Region")
plt.xlabel("Profit")
plt.ylabel("Region")
plt.tight_layout()
plt.savefig(CHART_DIR / "profit_by_region.png", dpi=300)
plt.close()

print("All five charts were created successfully.")
print("Chart folder:", CHART_DIR)

print("\nMonthly sales summary:")
print(monthly_sales.describe().round(2).to_string())

print("\nCharts created:")
for chart in sorted(CHART_DIR.glob("*.png")):
    print(chart.name)
