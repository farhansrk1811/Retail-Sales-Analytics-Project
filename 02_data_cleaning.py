
from pathlib import Path
import pandas as pd

# Project paths
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "Sample - Superstore.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

# Load original dataset
df = pd.read_csv(DATA_FILE, encoding="cp1252")

print("Original dataset shape:", df.shape)

# Remove surrounding spaces from column names and text values
df.columns = df.columns.str.strip()

text_columns = df.select_dtypes(include=["object", "str"]).columns
for col in text_columns:
    df[col] = df[col].str.strip()

# Convert dates into datetime values
for col in ["Order Date", "Ship Date"]:
    df[col] = pd.to_datetime(df[col], errors="coerce")

# Convert numerical fields safely
numeric_columns = [
    "Row ID", "Postal Code", "Sales",
    "Quantity", "Discount", "Profit"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Validate required fields and record invalid values
required_columns = [
    "Order ID", "Order Date", "Ship Date",
    "Sales", "Quantity", "Discount", "Profit"
]

invalid_report = {}

for col in required_columns:
    invalid_report[col] = int(df[col].isna().sum())

print("\nInvalid or missing values after type conversion:")
print(pd.Series(invalid_report, name="Count").to_string())

# Report duplicate rows before removing any
duplicate_count = int(df.duplicated().sum())
print("\nExact duplicate rows found:", duplicate_count)

# Remove exact duplicate rows only
df = df.drop_duplicates().copy()

# Check logical date and numerical validity
invalid_date_order = df["Ship Date"] < df["Order Date"]
invalid_sales = df["Sales"] < 0
invalid_quantity = df["Quantity"] <= 0
invalid_discount = ~df["Discount"].between(0, 1)

print("\nValidation checks:")
print("Ship date before order date:", int(invalid_date_order.sum()))
print("Negative sales:", int(invalid_sales.sum()))
print("Zero or negative quantity:", int(invalid_quantity.sum()))
print("Discount outside 0-1:", int(invalid_discount.sum()))

# Create useful date features
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Month Name"] = df["Order Date"].dt.strftime("%B")
df["Quarter"] = "Q" + df["Order Date"].dt.quarter.astype("Int64").astype(str)

# Create profit margin only where sales are nonzero
df["Profit Margin"] = df["Profit"].div(df["Sales"].where(df["Sales"] != 0))

# Save a cleaning report before making any decisions about invalid records
report = pd.DataFrame({
    "Check": [
        "Original rows",
        "Original columns",
        "Exact duplicate rows",
        "Missing or invalid Order ID",
        "Missing or invalid Order Date",
        "Missing or invalid Ship Date",
        "Missing or invalid Sales",
        "Missing or invalid Quantity",
        "Missing or invalid Discount",
        "Missing or invalid Profit",
        "Ship date before order date",
        "Negative sales",
        "Zero or negative quantity",
        "Discount outside 0-1",
        "Rows after exact duplicate removal"
    ],
    "Count": [
        9994,
        21,
        duplicate_count,
        int(df["Order ID"].isna().sum()),
        int(df["Order Date"].isna().sum()),
        int(df["Ship Date"].isna().sum()),
        int(df["Sales"].isna().sum()),
        int(df["Quantity"].isna().sum()),
        int(df["Discount"].isna().sum()),
        int(df["Profit"].isna().sum()),
        int(invalid_date_order.sum()),
        int(invalid_sales.sum()),
        int(invalid_quantity.sum()),
        int(invalid_discount.sum()),
        len(df)
    ]
})

report.to_csv(
    OUTPUT_DIR / "data_cleaning_report.csv",
    index=False,
    encoding="utf-8-sig"
)

# Stop if required data needs review rather than silently discarding records
critical_issues = (
    df[required_columns].isna().any().any()
    or invalid_date_order.any()
    or invalid_sales.any()
    or invalid_quantity.any()
    or invalid_discount.any()
)

if critical_issues:
    print("\nReview the cleaning report before finalizing the cleaned dataset.")
    print("No records were removed for validation issues.")
else:
    clean_path = OUTPUT_DIR / "cleaned_superstore.csv"
    df.to_csv(clean_path, index=False, encoding="utf-8-sig")
    print("\nCleaned dataset saved to:", clean_path)

print("\nCleaning report saved to:", OUTPUT_DIR / "data_cleaning_report.csv")
print("Rows currently retained:", len(df))
