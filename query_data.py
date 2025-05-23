import sqlite3
import pandas as pd

conn = sqlite3.connect("claims_data.db")

# Query 1: Show average claim amount per region
query1 = """
SELECT region, AVG(claim) as avg_claim
FROM claims_cleaned
GROUP BY region
"""
df1 = pd.read_sql(query1, conn)
print("Average claim by region:\n", df1)

# Query 2: Show all smokers who filed claims over $3000
query2 = """
SELECT * FROM claims_cleaned
WHERE smoker = 'Yes'AND claim > 3000
"""
df2 = pd.read_sql(query2, conn)
print("\n High-claim smokers:\n", df2)


# Query 3: Count diabetic vs non-diabetic patients
query3 = """
SELECT diabetic, COUNT(*) as patient_count
FROM claims_cleaned
GROUP BY diabetic
"""
df3 = pd.read_sql(query3, conn)
print("\n Diabetic vs Non-diabetic counts:\n", df3)

conn.close()

# Save DataFrames to CSV files
df1.to_csv("average_claim_by_region.csv", index=False)
df2.to_csv("high_claim_smokers.csv", index=False)
df3.to_csv("diabetic_counts.csv", index=False)


# Reconnect to database for table creation
conn = sqlite3.connect("claims_data.db")
cursor = conn.cursor()

# Create a new table for high-claim smokers
query_create = """
CREATE TABLE IF NOT EXISTS high_claim_smokers AS
SELECT * FROM claims_cleaned
WHERE smoker = 'Yes' AND claim > 3000
"""
cursor.execute(query_create)
conn.commit()
conn.close()
