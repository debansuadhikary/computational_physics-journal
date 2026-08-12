import pandas as pd

# Setup experimental run DataFrame
df = pd.DataFrame(
    {
        "Energy_eV": [13.6, 3.4, 1.51, 0.85],
        "Wavelength_nm": [91.2, 364.6, 820.6, 1458.8],
        "Observed": [True, True, False, True],
    },
    index=["n=1", "n=2", "n=3", "n=4"],  # Custom string index labels
)

print("Original DataFrame")
print(df)

# 1. Column Selection
print("\nSelecting Single and Multiple Columns")
energy_col = df["Energy_eV"]  # Returns a Series
sub_table = df[["Energy_eV", "Observed"]]  # Returns a DataFrame
print(sub_table)

# 2. Label-based selection using .loc[row_label, column_label]
print("\nSelection by Label (.loc)")
print("Energy for n=2 state :", df.loc["n=2", "Energy_eV"])
print("\nSubset for n=1 to n=3:")
print(df.loc["n=1":"n=3", ["Energy_eV", "Wavelength_nm"]])

# 3. Position-based selection using .iloc[row_index, column_index]
print("\nSelection by Position (.iloc)")
print("First row, second column :", df.iloc[0, 1])
print("\nFirst 2 rows, all columns:")
print(df.iloc[0:2, :])
