import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Generate physical dataset: Ideal Gas Law V vs T at different pressures
np.random.seed(42)
temp_k = np.linspace(200, 500, 40)

# Volume responses for low and high pressure conditions with noise
vol_low_p = 0.08 * temp_k + np.random.normal(0, 1.5, 40)
vol_high_p = 0.04 * temp_k + np.random.normal(0, 1.0, 40)

df = pd.DataFrame({
    "Temperature_K": np.tile(temp_k, 2),
    "Volume_L": np.concatenate([vol_low_p, vol_high_p]),
    "Pressure": ["Low Pressure (1 atm)"] * 40 + ["High Pressure (2 atm)"] * 40
})

# 1. Linear Regression with Confidence Bands (lmplot)
# Automatically fits lines and computes 95% confidence intervals via bootstrapping
g = sns.lmplot(
    data=df, 
    x="Temperature_K", 
    y="Volume_L", 
    hue="Pressure", 
    markers=["o", "s"], 
    height=5, 
    aspect=1.4, 
    scatter_kws={"s": 30, "alpha": 0.7}
)

g.set_axis_labels("Temperature $T$ (K)", "Volume $V$ (L)")
g.fig.suptitle("Chasles/Gay-Lussac Law: $V$ vs $T$ Linear Fit", y=1.03, fontsize=13, fontweight="bold")
plt.show()

# 2. Polynomial Regression Fit (order=2)
x_poly = np.linspace(0, 5, 30)
y_poly = 2.5 * (x_poly ** 2) - 1.2 * x_poly + np.random.normal(0, 2.0, 30)

plt.figure(figsize=(7, 4.5))
sns.regplot(x=x_poly, y=y_poly, order=2, color="teal", scatter_kws={"s": 40})
plt.title("2nd-Order Polynomial Trend Fit", fontsize=12, fontweight="bold")
plt.xlabel("Input Parameter")
plt.ylabel("System Output Response")
plt.grid(True, alpha=0.5)
plt.tight_layout()
plt.show()
