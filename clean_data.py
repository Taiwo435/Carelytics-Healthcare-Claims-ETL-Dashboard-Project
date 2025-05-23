import sqlite3
import pandas as pd

df = pd.read_csv("claims.csv")
df = df.drop(columns=["index"])


df["age"] = df["age"].fillna(df["age"].mean())
df["region"] = df["region"].fillna("Unknown")

df["gender"] = df["gender"].str.lower()
df["diabetic"] = df["diabetic"].str.title()
df["smoker"] = df["smoker"].str.title()

df = df[df["claim"] > 0]

conn = sqlite3.connect("claims_data.db")
df.to_sql("claims_cleaned", conn, if_exists='replace', index=False)
conn.close()

print("Cleaned data saved to table 'claims_cleaned' in claims_data.db")
