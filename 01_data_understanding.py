
from pathlib import Path
import pandas as pd

# Locate the project and dataset
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "Sample - Superstore.csv"

# Check whether the dataset exists
if not DATA_FILE.exists():
    raise FileNotFoundError(f"Dataset not found: {DATA_FILE}")

# Load the dataset
df = pd.read_csv(DATA_FILE, encoding="cp1252")

print("\n===== DATASET OVERVIEW =====")
print("Dataset name:", DATA_FILE.name)
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

print("\n===== FIRST FIVE ROWS =====")
print(df.head().to_string(index=False))

print("\n===== DATA TYPES =====")
print(df.dtypes.to_string())

print("\n===== MISSING VALUES =====")
print(df.isnull().sum().to_string())

print("\n===== DUPLICATE ROWS =====")
print("Duplicate rows:", df.duplicated().sum())

print("\n===== NUMERICAL SUMMARY =====")
print(df.describe().to_string())

print("\nDataset inspection completed.")

# Save dataset inspection results
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df.head(20).to_csv(
    OUTPUT_DIR / "data_preview.csv",
    index=False,
    encoding="utf-8-sig"
)

df.isnull().sum().to_csv(
    OUTPUT_DIR / "missing_values_report.csv",
    header=["Missing_Count"]
)

print("\nInspection files saved successfully in the outputs folder.")