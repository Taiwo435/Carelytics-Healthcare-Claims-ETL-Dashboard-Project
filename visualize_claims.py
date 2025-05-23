import pandas as pd
import matplotlib.pyplot as plt

# Plot 1: Average claim by region
df_avg = pd.read_csv("average_claim_by_region.csv")
df_avg.plot(kind='bar', x='region', y='avg_claim', legend=False)
plt.title("Average Claim Amount by Region")
plt.xlabel("Region")
plt.ylabel("Average Claim ($)")
plt.tight_layout()
plt.show()

# Plot 2: Diabetic vs Non-diabetic Count
df_diabetic = pd.read_csv("diabetic_counts.csv")
df_diabetic.plot(kind='bar', x='diabetic', y='patient_count',
                 legend=False, color='orange')
plt.title("Patient Count by Diabetic Status")
plt.xlabel("Diabetic")
plt.ylabel("Number of Patients")
plt.tight_layout()
plt.show()

# Plot 3: Average claim per gender (smokers only)
df_smokers = pd.read_csv("high_claim_smokers.csv")
df_gender_avg = df_smokers.groupby('gender')['claim'].mean().reset_index()
df_gender_avg.plot(kind='bar', x='gender', y='claim',
                   legend=False, color='skyblue')
plt.title("Average Claim Amount by Gender (High-Claim Smokers)")
plt.xlabel("Gender")
plt.ylabel("Avg Claim ($)")
plt.tight_layout()
plt.show()
