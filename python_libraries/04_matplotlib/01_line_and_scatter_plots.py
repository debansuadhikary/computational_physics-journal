import os
import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic experimental data
t = np.linspace(0, 10, 100)
x_exact = np.exp(-0.2 * t) * np.cos(2.0 * t)

# Noisy data points representing physical measurements
t_measured = np.linspace(0, 10, 25)
x_measured = np.exp(-0.2 * t_measured) * np.cos(2.0 * t_measured) + np.random.normal(0, 0.05, size=25)

# Create Figure and Axes objects (Object-Oriented API)
fig, ax = plt.subplots(figsize=(8, 5), dpi=100)

# Plot continuous theoretical curve
ax.plot(t, x_exact, label="Theoretical Model", color="navy", linestyle="-", linewidth=2)

# Scatter plot for discrete experimental measurements
ax.scatter(t_measured, x_measured, label="Experimental Data", color="crimson", marker="o", s=30, zorder=3)

# Formatting labels, grid, and title
ax.set_title("Damped Harmonic Oscillator: Theory vs Experiment", fontsize=14, fontweight="bold")
ax.set_xlabel("Time $t$ (s)", fontsize=12)
ax.set_ylabel("Displacement $x(t)$ (m)", fontsize=12)
ax.axhline(0, color="gray", linestyle="--", linewidth=0.8)  # Zero reference line
ax.grid(True, linestyle=":", alpha=0.6)
ax.legend(loc="upper right", frameon=True)

# Save high-resolution figure for paper/report
output_dir = "plots_output"
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, "line_scatter_plot.png"), dpi=300, bbox_inches="tight")

print(f"Plot saved successfully to '{output_dir}/line_scatter_plot.png'")
plt.show()
