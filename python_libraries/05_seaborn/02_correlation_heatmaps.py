import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Generate synthetic simulation parameters dataset
np.random.seed(101)
n_samples = 200

mass = np.random.uniform(1.0, 10.0, n_samples)
velocity = np.random.uniform(5.0, 50.0, n_samples)
momentum = mass * velocity
kinetic_energy = 0.5 * mass * (velocity ** 2)
temperature = 0.05 * kinetic_energy + np.random.normal(0, 2, n_samples)

df = pd.DataFrame({
    "Mass": mass,
    "Velocity": velocity,
    "Momentum": momentum,
    "Kinetic Energy": kinetic_energy,
    "Temperature": temperature
})

# Compute Pearson correlation matrix
corr_matrix = df.corr()

# 1. Annotated Correlation Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(
    corr_matrix, 
    annot=True,            # Print numerical correlation coefficients in cells
    fmt=".2f", 
    cmap="coolwarm",       # Diverging colormap (Red = positive, Blue = negative)
    vmin=-1.0, vmax=1.0, 
    linewidths=1.0, 
    cbar_kws={"label": "Pearson Correlation Coefficient"}
)

plt.title("Physical Parameters Correlation Matrix", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.show()

# 2. Hierarchical Clustering Heatmap (Groups strongly related physical parameters)
sns.clustermap(corr_matrix, cmap="mako", annot=True, figsize=(7, 7))
plt.suptitle("Hierarchical Parameter Clustering", y=1.02, fontsize=14, fontweight="bold")
plt.show()
