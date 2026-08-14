import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Experimental Conductivity Data across Material Samples
np.random.seed(7)
copper = np.random.normal(59.6, 2.1, 100)
aluminum = np.random.normal(37.7, 1.8, 100)
silicon = np.random.normal(0.1, 0.05, 100)

df = pd.DataFrame({
    "Conductivity": np.concatenate([copper, aluminum]),
    "Material": ["Copper"] * 100 + ["Aluminum"] * 100
})

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# 1. Box Plot overlaid with Individual Data Points (Stripplot)
sns.boxplot(data=df, x="Material", y="Conductivity", ax=ax1, palette="Set2", width=0.4, boxprops=dict(alpha=0.7))
sns.stripplot(data=df, x="Material", y="Conductivity", ax=ax1, color="black", alpha=0.4, jitter=0.2, size=5)
ax1.set_title("Electrical Conductivity Distribution (Boxplot)")
ax1.set_ylabel("Conductivity ($MS/m$)")

# 2. Violin Plot (Combines Boxplot metrics with Kernel Density shape)
sns.violinplot(data=df, x="Material", y="Conductivity", ax=ax2, palette="Set2", inner="quartile", cut=0)
ax2.set_title("Conductivity Density Profiles (Violinplot)")
ax2.set_ylabel("Conductivity ($MS/m$)")

plt.tight_layout()
plt.show()
