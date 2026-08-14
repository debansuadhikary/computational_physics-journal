import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Generate multi-variable dataset representing Monte Carlo phase space runs
np.random.seed(42)
n_samples = 300

# High-energy vs Low-energy phase classifications
phase_A_x = np.random.normal(1.0, 0.5, 150)
phase_A_y = np.random.normal(2.0, 0.8, 150)
phase_A_z = phase_A_x * 2.0 + np.random.normal(0, 0.3, 150)

phase_B_x = np.random.normal(3.0, 0.7, 150)
phase_B_y = np.random.normal(0.5, 0.4, 150)
phase_B_z = phase_B_x * 0.5 + np.random.normal(0, 0.2, 150)

df = pd.DataFrame({
    "Position_X": np.concatenate([phase_A_x, phase_B_x]),
    "Momentum_Y": np.concatenate([phase_A_y, phase_B_y]),
    "Energy_Z": np.concatenate([phase_A_z, phase_B_z]),
    "Phase": ["Phase Alpha"] * 150 + ["Phase Beta"] * 150
})

# 1. Automatic Pairwise Feature Matrix (pairplot)
# Diagonals show KDE distributions; off-diagonals show scatter relationships
pair_fig = sns.pairplot(
    df, 
    hue="Phase", 
    corner=True,              # Plot lower triangle only to eliminate redundant mirrored plots
    kind="scatter", 
    diag_kind="kde", 
    palette="Dark2", 
    plot_kws={"alpha": 0.6, "s": 25}
)

pair_fig.fig.suptitle("Phase Space Pairwise Feature Relationships", y=1.02, fontsize=14, fontweight="bold")
plt.show()
