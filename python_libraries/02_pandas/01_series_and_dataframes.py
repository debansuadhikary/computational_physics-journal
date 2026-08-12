import numpy as np
import pandas as pd

# 1. Pandas Series (1D Labeled Array)
time_steps = pd.Series([0.0, 0.1, 0.2, 0.3, 0.4], name="Time (s)")
print("1D Pandas Series")
print(time_steps)
print(f"Values array : {time_steps.values}")
print(f"Index        : {time_steps.index}\n")

# 2. Pandas DataFrame (2D Tabular Data)
# Creating a DataFrame from a dictionary of physical simulation outputs
data = {
    "Time": [0.0, 0.5, 1.0, 1.5, 2.0],
    "Position": [0.00, 1.25, 5.00, 11.25, 20.00],
    "Velocity": [0.0, 5.0, 10.0, 15.0, 20.0],
    "Sensor_ID": ["A1", "A1", "A2", "A2", "A2"],
}

df = pd.DataFrame(data)

print("2D DataFrame")
print(df)

# 3. Inspecting DataFrame Properties
print("\nData Summary & Inspection")
print("\n--- df.head(3) ---")
print(df.head(3))  # First 3 rows

print("\n--- df.info() ---")
df.info()  # Data types and non-null counts

print("\n--- df.describe() ---")
print(df.describe())  # Summary statistics (mean, std, min, max, quartiles)
