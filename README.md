# Sales Data Cleaning — 100 Rows (Python & Pandas)

## Overview
A hands-on portfolio project cleaning a sample dataset of 100 sales records with missing values, duplicate order IDs, inconsistent text formatting, and invalid numeric values.

## Tools
Python, Pandas, CSV, Visual Studio Code.

## Workflow
1. Standardize city and product names (trim spaces and lowercase).
2. Convert quantities and prices to numeric types; parse dates.
3. Flag missing, invalid, and duplicate-order records for manual review.
4. Calculate `total_sales = quantity * unit_price`, extract `month`, and label `order_status`.
5. Export valid and review-needed records separately.

## Results
| Output | Rows |
| --- | ---: |
| Original dataset | 100 |
| Cleaned valid records | 81 |
| Records needing review | 19 |
| Total accounted for | 100 |

## Files
- `messy_sales_100_rows.csv` — Original input data.
- `code.py` — Pandas cleaning script.
- `cleaned_100_rows.csv` — Valid cleaned records.
- `need_review_100_rows.csv` — Flagged records for manual review.

## Run
Install Pandas (`pip install pandas`), then run `python code.py` in the directory containing the input CSV.

## Note
This is an independent practice/portfolio project, not commissioned client work.