import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("🏥 Healthcare Claims Dashboard")

# Loading datasets
df_avg = pd.read_csv("average_claim_by_region.csv")
df_smokers = pd.read_csv("high_claim_smokers.csv")
df_diabetic = pd.read_csv("diabetic_counts.csv")

# Section 1: Average Claim by Region
st.subheader("📊 Average Claim by Region")

fig1, ax1 = plt.subplots()
df_avg.plot(kind='bar', x='region', y='avg_claim', legend=False, ax=ax1)
ax1.set_title("Average Claim Amount by Region")
ax1.set_xlabel("Region")
ax1.set_ylabel("Average Claim ($)")
st.pyplot(fig1)

# Section 2: Gender-based Claim Analysis for Smokers
st.subheader("🚬 Gender-based Claim Analysis (High-Claim Smokers)")
df_gender = df_smokers.groupby('gender')['claim'].mean().reset_index()

fig2, ax2 = plt.subplots()
df_gender.plot(kind='bar', x='gender', y='claim',
               legend=False, ax=ax2, color='orange')
ax2.set_title("Avg Claim by Gender (Smokers)")
ax2.set_xlabel("Gender")
ax2.set_ylabel("Average Claim ($)")
st.pyplot(fig2)

# Section 3: Diabetic vs Non-Diabetic Counts
st.subheader("🩺 Diabetic vs Non-Diabetic Patients")

fig3, ax3 = plt.subplots()
df_diabetic.plot(kind='bar', x='diabetic', y='patient_count',
                 legend=False, ax=ax3, color='teal')
ax3.set_title("Patient Count by Diabetic Status")
ax3.set_xlabel("Diabetic")
ax3.set_ylabel("Number of Patients")
st.pyplot(fig3)

# Raw Data Preview
st.subheader("📄 Preview Raw High-Claim Smokers Data")
st.dataframe(df_smokers)
