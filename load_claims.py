import sqlite3
import pandas as pd

df = pd.read_csv("claims.csv")
df = df.drop(columns=["index"])
conn = sqlite3.connect("claims_data.db")

df.to_sql("claims", conn, if_exists='replace', index=False)
conn.close()

print("dATA LOADED INTO CLAIMS_DATA.DB")
