
from pathlib import Path
import pandas as pd
import numpy as np
import json

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.dummy import DummyRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "outputs" / "cleaned_superstore.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
MODEL_DIR = BASE_DIR / "models"

OUTPUT_DIR.mkdir(exist_ok=True)
MODEL_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_FILE, encoding="utf-8-sig")
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="raise")

# Create useful date features
df["Order Year"] = df["Order Date"].dt.year
df["Order Month"] = df["Order Date"].dt.month

# Predict Profit using information available for each transaction.
# Exclude identifiers and direct target-derived fields.
target = "Profit"

features = [
    "Sales",
    "Quantity",
    "Discount",
    "Ship Mode",
    "Segment",
    "Region",
    "Category",
    "Sub-Category",
    "Order Year",
    "Order Month"
]

X = df[features].copy()
y = df[target].copy()

numeric_features = [
    "Sales", "Quantity", "Discount", "Order Year", "Order Month"
]
categorical_features = [
    "Ship Mode", "Segment", "Region", "Category", "Sub-Category"
]

# Split before fitting any preprocessing or model
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

numeric_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="median"))
])

categorical_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("numeric", numeric_transformer, numeric_features),
    ("categorical", categorical_transformer, categorical_features)
])

# Baseline: always predict the training-set mean
baseline = DummyRegressor(strategy="mean")
baseline.fit(X_train, y_train)
baseline_predictions = baseline.predict(X_test)

# Random Forest regression model
model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(
        n_estimators=150,
        random_state=42,
        min_samples_leaf=2,
        n_jobs=-1
    ))
])

model.fit(X_train, y_train)
predictions = model.predict(X_test)

def evaluate(actual, predicted):
    return {
        "MAE": float(mean_absolute_error(actual, predicted)),
        "RMSE": float(np.sqrt(mean_squared_error(actual, predicted))),
        "R2": float(r2_score(actual, predicted))
    }

results = {
    "target": target,
    "test_size": len(y_test),
    "training_size": len(y_train),
    "baseline": evaluate(y_test, baseline_predictions),
    "random_forest": evaluate(y_test, predictions)
}

print("\n===== PROFIT PREDICTION RESULTS =====")
print("Training records:", len(X_train))
print("Test records:", len(X_test))

for name in ["baseline", "random_forest"]:
    print(f"\n{name.upper()}")
    for metric, value in results[name].items():
        print(f"{metric}: {value:.4f}")

# Save evaluation results and test predictions
with open(OUTPUT_DIR / "model_evaluation.json", "w") as f:
    json.dump(results, f, indent=4)

pd.DataFrame({
    "Actual Profit": y_test.to_numpy(),
    "Baseline Predicted Profit": baseline_predictions,
    "Predicted Profit": predictions
}).to_csv(
    OUTPUT_DIR / "profit_predictions.csv",
    index=False,
    encoding="utf-8-sig"
)

# Save the fitted pipeline for reproducibility
import joblib
joblib.dump(model, MODEL_DIR / "profit_prediction_model.joblib")

print("\nEvaluation and predictions saved in outputs.")
print("Fitted model saved in models.")
