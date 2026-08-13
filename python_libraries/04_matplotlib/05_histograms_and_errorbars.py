import numpy as np
import matplotlib.pyplot as plt

# 1. Histogram of Random Gaussian Measurement Noise
np.random.seed(10)
measurements = np.random.normal(loc=5.0, scale=1.2, size=1000)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))

# Plot normalized probability density histogram
n, bins, patches = ax1.hist(measurements, bins=30, density=True, color="skyblue", edgecolor="black", alpha=0.7)
ax1.set_title("Measurement Noise Distribution")
ax1.set_xlabel("Measured Value")
ax1.set_ylabel("Probability Density")
ax1.grid(True, linestyle="--", alpha=0.5)

# 2. Plotting Physical Points with Symmetric/Asymmetric Error Bars
x_exp = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
y_exp = np.array([2.1, 3.9, 8.8, 16.2, 24.8])
y_err = np.array([0.3, 0.4, 0.5, 0.8, 1.1])  # Uncertainty limits

ax2.errorbar(
    x_exp, y_exp, yerr=y_err, fmt="o", color="darkred",
    ecolor="black", elinewidth=1.5, capsize=4, label="Sensor Data ± $\sigma$"
)
ax2.set_title("Experimental Data with Error Bars")
ax2.set_xlabel("Input Parameter")
ax2.set_ylabel("Measured Signal")
ax2.grid(True, linestyle="--", alpha=0.5)
ax2.legend()

plt.tight_layout()
plt.show()
