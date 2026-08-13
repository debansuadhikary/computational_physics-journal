import numpy as np
import matplotlib.pyplot as plt

# Construct 2D Spatial Grid
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

# Scalar Potential Field: 2D Gaussian Quantum Well
Z = np.exp(-(X**2 + Y**2))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# 1. Heatmap / Pseudocolor Mesh (pcolormesh)
mesh = ax1.pcolormesh(X, Y, Z, cmap="viridis", shading="auto")
fig.colorbar(mesh, ax=ax1, label="Potential $V(x,y)$")
ax1.set_title("2D Field Heatmap (pcolormesh)")
ax1.set_xlabel("$x$")
ax1.set_ylabel("$y$")

# 2. Filled Contours with Overlay Lines (contourf + contour)
contour_filled = ax2.contourf(X, Y, Z, levels=12, cmap="magma")
contour_lines = ax2.contour(X, Y, Z, levels=6, colors="white", linewidths=0.8)
ax2.clabel(contour_lines, inline=True, fontsize=8, fmt="%.2f")  # Label contour values
fig.colorbar(contour_filled, ax=ax2, label="Potential $V(x,y)$")
ax2.set_title("2D Contour Lines (contourf)")
ax2.set_xlabel("$x$")
ax2.set_ylabel("$y$")

plt.tight_layout()
plt.show()
