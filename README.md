# 🏥 Carelytics: Healthcare Claims ETL & Dashboard Project

This project simulates a real-world healthcare data pipeline and interactive dashboard. It demonstrates the end-to-end workflow of loading, cleaning, analyzing, and visualizing healthcare claims data using **Python**, **pandas**, **SQLite**, **matplotlib**, and **Streamlit**.

---

## 🚀 Features

- **Data Loading & Cleaning**
  - Loaded raw claims data from CSV
  - Filled missing values, removed invalid rows, and normalized columns
  - Saved cleaned data into a SQLite database

- **Data Analysis**
  - Calculated average claim by region
  - Filtered high-claim smokers
  - Counted diabetic vs non-diabetic patients
  - Created a new table for high-claim smokers

- **Visualization**
  - Used `matplotlib` to generate bar charts for:
    - Average claims per region
    - Diabetic distribution
    - Gender-based claim averages for smokers

- **Interactive Dashboard**
  - Built with Streamlit
  - Displays insights using interactive plots
  - Allows data preview and real-time exploration

---

## 🗂 Project Structure

| File                  | Description                                      |
|-----------------------|--------------------------------------------------|
| `claims.csv`          | Raw healthcare claims data (local only)          |
| `load_claims.py`      | Loads the raw CSV data into SQLite               |
| `clean_data.py`       | Cleans, normalizes, and stores data in a new table |
| `query_data.py`       | Runs SQL queries and exports CSV summaries       |
| `visualize_claims.py` | Static plots using matplotlib                    |
| `dashboard.py`        | Interactive dashboard using Streamlit            |
| `claims_data.db`      | Local SQLite database                            |

---

## 🛠 Tools Used

- **Python 3.11**
- **pandas** for data manipulation
- **SQLite3** for SQL and storage
- **matplotlib** for data visualization
- **Streamlit** for building dashboards

---


## 📦 How to Run This Project

Run the scripts in the following order to ensure the data flows through all steps correctly:

```bash
python load_claims.py        # Step 1: Load raw CSV into database
python clean_data.py         # Step 2: Clean and store in new table
python query_data.py         # Step 3: Run SQL and export summaries
python visualize_claims.py   # Step 4: (optional) Static charts
streamlit run dashboard.py   # Step 5: Interactive dashboard

