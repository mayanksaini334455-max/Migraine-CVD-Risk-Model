import pandas as pd
import matplotlib.pyplot as plt

# Sample Biomedical Dataset
data = {
    "Migraine": [1,0,1,0,1,0,1,0,1,0],
    "Age": [45,50,38,60,42,55,48,52,40,58],
    "BP": [140,120,150,110,135,115,145,118,138,125],
    "Smoking": [1,0,1,0,0,0,1,0,1,0],
    "CVD_Risk": [1,0,1,0,1,0,1,0,1,0]
}

df = pd.DataFrame(data)

print("Dataset Preview:")
print(df.head())

print("\nStatistical Summary:")
print(df.describe())

# Visualization
plt.scatter(df["BP"], df["CVD_Risk"])
plt.xlabel("Blood Pressure")
plt.ylabel("CVD Risk (0=No, 1=Yes)")
plt.title("Blood Pressure vs Cardiovascular Risk")
plt.show()