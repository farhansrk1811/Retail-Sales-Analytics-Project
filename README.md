# Retail Sales Analysis and Profitability Prediction

## Project Overview

This project analyzes retail sales data to identify sales trends, evaluate profitability, compare regional and product-category performance, and explore machine learning techniques for profit prediction.

The project uses Python for data cleaning, exploratory data analysis, KPI calculations, visualization, and predictive modeling, along with Power BI to develop an interactive business intelligence dashboard.

## Objectives

- Clean and prepare retail sales data for analysis.
- Calculate key performance indicators (KPIs).
- Analyze sales and profit by category, region, and time.
- Visualize sales trends and the relationship between discounts and profit.
- Develop a machine learning model to explore profit prediction.
- Present actionable business insights through a Power BI dashboard.

## Tools and Technologies

- **Python** — Data processing and analysis
- **Pandas and NumPy** — Data cleaning and manipulation
- **Matplotlib and Seaborn** — Data visualization
- **Scikit-learn** — Machine learning and model evaluation
- **Power BI Desktop** — Interactive dashboard development
- **VS Code** — Development environment
- **Git and GitHub** — Version control and project hosting

## Dataset

The project uses the Sample Superstore retail dataset, containing order-level information about sales, profit, discounts, product categories, customers, regions, and shipping.

The original dataset contains **9,994 records and 21 columns**.

## Project Workflow

1. **Data Understanding:** Examine the dataset structure, column types, summary statistics, and data quality.
2. **Data Cleaning:** Check for missing values and duplicate records, validate data types, and prepare the cleaned dataset.
3. **KPI Analysis:** Calculate total sales, total profit, profit margin, order count, customer count, and units sold.
4. **Exploratory Data Analysis:** Compare category and regional performance and examine monthly sales trends.
5. **Data Visualization:** Generate charts for sales, profit, and discount analysis.
6. **Profit Prediction:** Train and evaluate a Random Forest regression model against a baseline model.
7. **Power BI Dashboard:** Present key metrics, trends, comparisons, and filters in an interactive dashboard.

## Key Performance Indicators

| KPI | Result |
|---|---:|
| Total Sales | $2,297,200.86 |
| Total Profit | $286,397.02 |
| Profit Margin | 12.47% |
| Unique Orders | 5,009 |
| Unique Customers | 793 |
| Units Sold | 37,873 |

## Key Findings

- **Technology** generated the highest category profit, approximately $145,454.95, with a profit margin of 17.40%.
- **Office Supplies** generated approximately $122,490.80 in profit and accounted for the largest unit volume.
- **Furniture** generated approximately $18,451.27 in profit, with a comparatively low profit margin of 2.49%.
- The **West** region recorded the highest sales and profit among the four regions.
- Discount levels and profitability were examined to help identify potential areas for improving pricing and discount strategies.

## Machine Learning Model

A Random Forest regression model was developed to explore profit prediction using available order, product, discount, and shipping-related features.

The model was compared with a baseline prediction model using Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and the coefficient of determination (R²).

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Baseline | 67.55 | 220.43 | -0.0021 |
| Random Forest | 27.49 | 216.22 | 0.0358 |

The Random Forest model improved on the baseline error metrics, but its R² of approximately 0.036 indicates **limited predictive power**. The model should therefore be treated as an exploratory prototype, not a reliable production forecasting system.

## Project Structure

```text
Retail_Sales_Analytics_Project/
├── data/
│   └── Sample - Superstore.csv
├── outputs/
│   ├── cleaned_superstore.csv
│   ├── charts/
│   ├── cleaning_report.json
│   ├── model_evaluation.json
│   └── profit_predictions.csv
├── models/
│   └── profit_prediction_model.joblib
├── 01_data_understanding.py
├── 02_data_cleaning.py
├── 03_kpi_analysis.py
├── 04_visualizations.py
├── 05_profit_prediction.py
├── requirements.txt
└── README.md
```

*The structure above describes the expected project files. Adjust it if your actual folder or output filenames differ.*

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/farhansrk1811/Retail-Sales-Analytics-Project.git
cd Retail-Sales-Analytics-Project
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the analysis scripts

Execute the scripts in order:

```bash
python 01_data_understanding.py
python 02_data_cleaning.py
python 03_kpi_analysis.py
python 04_visualizations.py
python 05_profit_prediction.py
```

Ensure the dataset is located at the path expected by the scripts. Run these commands from the project root directory.

## Power BI Dashboard

The Power BI dashboard provides an interactive view of sales, profit, profit margin, order count, customer count, and units sold, with visual analysis by product category, region, and time.

Open `Retail_Sales_Profitability_Analysis.pbix` in Power BI Desktop if the file is included in the repository.

## Business Recommendations

- Review Furniture pricing, product costs, and discount policies to improve profitability.
- Use category and regional performance to guide inventory planning and sales strategies.
- Monitor profit margin alongside revenue rather than evaluating performance on sales alone.
- Investigate the relationship between discounts and profit before changing discount policies.
- Improve predictive modeling through feature engineering, stronger validation, and additional explanatory variables.

## Limitations

- The analysis is based on the available sample dataset and may not represent all retail businesses.
- The profit prediction model currently has low explanatory power.
- Findings describe historical data and do not establish causation.
- Business decisions should consider additional operational and market information.

## Author

**Farhan Sirkhot**

GitHub: [farhansrk1811](https://github.com/farhansrk1811)

## License

This project is intended for educational and academic purposes. Check the dataset's applicable usage terms before redistributing the original data.
