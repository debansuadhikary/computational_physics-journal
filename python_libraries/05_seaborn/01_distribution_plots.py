import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set cohesive Seaborn theme for scientific publication plots
sns.set_theme(style="whitegrid", palette="muted")

# Generate synthetic experimental particle energy measurements (3 different detector runs)
np.random.seed(42)
detector_A = np.random.normal(loc=10.0, scale=1.5, size=500)
detector_B = np.random.normal(loc=12.0, scale=2.0, size=500)

df = pd.DataFrame({
    "Energy_MeV": np.concatenate([detector_A, detector_B]),
    "Detector": ["Detector A"] * 500 + ["Detector B"] * 500
})

# 1. Overlayed Histograms with Kernel Density Estimation (KDE)
plt.figure(figsize=(8, 5))
sns.histplot(
    data=df, 
    x="Energy_MeV", 
    hue="Detector", 
    kde=True,               # Overlay smooth probability density estimate
    element="step",         # Step-style histogram
    stat="density",         # Normalize to density
    common_norm=False, 
    alpha=0.4
)

plt.title("Particle Energy Spectrum Across Detectors", fontsize=14, fontweight="bold")
plt.xlabel("Energy (MeV)")
plt.ylabel("Probability Density")
plt.tight_layout()
plt.show()

# 2. Standalone Smooth 2D Density Contour Plot
x_data = np.random.normal(0, 1, 1000)
y_data = x_data * 0.8 + np.random.normal(0, 0.5, 1000)

plt.figure(figsize=(6, 5))
sns.kdeplot(x=x_data, y=y_data, cmap="Blues", fill=True, thresh=0.05)
plt.title("2D Probability Density Contours (KDE)")
plt.xlabel("Parameter X")
plt.ylabel("Parameter Y")
plt.tight_layout()
plt.show()
