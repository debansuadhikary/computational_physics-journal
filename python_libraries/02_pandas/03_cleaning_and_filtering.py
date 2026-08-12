import numpy as np
import pandas as pd

# Experimental sensor dataset with missing values (NaN)
raw_data = {
    "Temperature_K": [300.0, 310.5, np.nan, 295.2, 350.0, np.nan],
    "Pressure_kPa": [101.3, 105.2, 98.4, np.nan, 120.1, 100.0],
    "Status": ["OK", "OK", "ERROR", "OK", "WARNING", "ERROR"],
}

df = pd.DataFrame(raw_data)

print("Raw Experimental Data")
print(df)

# 1. Detecting missing values
print("\nMissing values per column:")
print(df.isna().sum())

# 2. Cleaning missing data
# Fill missing temperatures with the column mean, drop remaining bad rows
df["Temperature_K"] = df["Temperature_K"].fillna(df["Temperature_K"].mean())
df_clean = df.dropna().copy()

print("\nCleaned Data")
print(df_clean)

# 3. Boolean Filtering (Conditional Queries)
# Filter for Temperature > 300 K AND Status == "OK"
filter_condition = (df_clean["Temperature_K"] > 300.0) & (
    df_clean["Status"] == "OK"
)
filtered_df = df_clean[filter_condition]

print("\nHigh Temperature Valid Runs")
print(filtered_df)

# 4. Adding Derived Physics Columns
# Convert Temperature from Kelvin to Celsius: C = K - 273.15
df_clean["Temperature_C"] = df_clean["Temperature_K"] - 273.15
print("\nFinal Data with Computed Column")
print(df_clean)
