# Toronto 311 Service Analytics

Exploratory analysis of Toronto's 311 Service Request data, examining request volume, timing patterns, and category/ward-level trends.

## Data Source
Toronto 311 Service Requests dataset (sr2025.csv) — City of Toronto Open Data.

## Scripts
1. scripts/01_load_inspect.py — loads the raw CSV, parses creation dates, and inspects data quality.
2. scripts/02_clean_standardize.py — removes duplicates and sparse columns, groups service divisions into categories, and saves a cleaned CSV.
3. scripts/03_Insights.py — analyzes the cleaned data for top categories, peak hours/days, seasonality, top wards, division workload, and status breakdown.

## Requirements
- Python 3.x
- pandas

## How to Run
cd scripts
python 01_load_inspect.py
python 02_clean_standardize.py
python 03_Insights.py

## Project Structure
toronto-311-service-analytics/
├── data/
│   ├── raw/
│   │   └── sr2025.csv
│   └── processed/
│       └── sr2025_cleaned.csv
├── scripts/
│   ├── 01_load_inspect.py
│   ├── 02_clean_standardize.py
│   └── 03_Insights.py
└── README.md