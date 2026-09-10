import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel(
    "../data/Italy_Inflation_Unemployment_Data_2015_2026.xlsx"
)

# Display basic information
print("Dataset shape:", df.shape)
print("\nColumn data types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isna().sum())

print("\nSummary statistics:")
print(df.describe())

# Calculate averages
average_inflation = df["Inflation_HICP_Annual_%"].mean()
average_unemployment = df["Unemployment_Rate_%"].mean()

print("\nAverage inflation:", round(average_inflation, 2), "%")
print("Average unemployment:", round(average_unemployment, 2), "%")

# Find highest and lowest inflation
highest_inflation = df.loc[
    df["Inflation_HICP_Annual_%"].idxmax()
]

lowest_inflation = df.loc[
    df["Inflation_HICP_Annual_%"].idxmin()
]

print("\nHighest inflation:")
print(highest_inflation)

print("\nLowest inflation:")
print(lowest_inflation)

# Calculate correlation
correlation = df[
    "Inflation_HICP_Annual_%"
].corr(
    df["Unemployment_Rate_%"]
)

print(
    "\nCorrelation between inflation and unemployment:",
    round(correlation, 2)
)

# Inflation chart
plt.figure(figsize=(12, 6))
plt.plot(
    df["Date"],
    df["Inflation_HICP_Annual_%"],
    label="Inflation"
)

plt.title("Italy Inflation (2015–2026)")
plt.xlabel("Date")
plt.ylabel("Inflation (%)")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(
    "../figures/Italy_Inflation_2015_2026.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# Unemployment chart
plt.figure(figsize=(12, 6))
plt.plot(
    df["Date"],
    df["Unemployment_Rate_%"],
    label="Unemployment"
)

plt.title("Italy Unemployment Rate (2015–2026)")
plt.xlabel("Date")
plt.ylabel("Unemployment (%)")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(
    "../figures/Italy_Unemployment_2015_2026.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# Inflation vs unemployment scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(
    df["Inflation_HICP_Annual_%"],
    df["Unemployment_Rate_%"]
)

plt.title("Inflation vs Unemployment in Italy (2015–2026)")
plt.xlabel("Inflation (%)")
plt.ylabel("Unemployment (%)")
plt.grid(True)
plt.tight_layout()

plt.savefig(
    "../figures/Italy_Inflation_vs_Unemployment_2015_2026.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nAnalysis completed successfully.")