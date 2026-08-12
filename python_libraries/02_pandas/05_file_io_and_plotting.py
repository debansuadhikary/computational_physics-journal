import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1. Generate synthetic damped harmonic oscillator simulation data
t = np.linspace(0, 10, 100)
gamma = 0.5
omega = 2.0
x = np.exp(-gamma * t) * np.cos(omega * t)

df = pd.DataFrame({"Time_s": t, "Displacement_m": x})

# 2. Exporting DataFrame to CSV File
output_dir = "data_output"
os.makedirs(output_dir, exist_ok=True)
csv_filepath = os.path.join(output_dir, "damped_oscillator.csv")

df.to_csv(csv_filepath, index=False)
print(f"Data successfully saved to '{csv_filepath}'")

# 3. Reading Data Back from CSV
imported_df = pd.read_csv(csv_filepath)
print("\n=== First 5 rows of imported CSV ===")
print(imported_df.head())

# 4. Quick Plotting directly using Pandas / Matplotlib
plt.figure(figsize=(8, 4))
plt.plot(
    imported_df["Time_s"],
    imported_df["Displacement_m"],
    label="Damped Harmonic Motion",
    color="navy",
)
plt.title("Pandas Data Plotting: Position vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.grid(True)
plt.legend()
plt.tight_layout()

# Save plot image
plt.savefig(os.path.join(output_dir, "oscillator_plot.png"))
print(f"Plot saved to '{output_dir}/oscillator_plot.png'")
plt.show()
