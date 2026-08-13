import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Enables 3D projection

# 1. 3D Helix Trajectory (e.g., Charged Particle in a Magnetic Field)
t = np.linspace(0, 10 * np.pi, 500)
x_traj = np.cos(t)
y_traj = np.sin(t)
z_traj = 0.2 * t

fig = plt.figure(figsize=(12, 5))

# Subplot 1: 3D Trajectory Curve
ax1 = fig.add_subplot(1, 2, 1, projection="3d")
ax1.plot(x_traj, y_traj, z_traj, label="Particle Helical Path", color="crimson", linewidth=2)
ax1.set_title("3D Particle Trajectory")
ax1.set_xlabel("X (m)")
ax1.set_ylabel("Y (m)")
ax1.set_zlabel("Z (m)")
ax1.legend()

# 2. 3D Potential Surface Plot
x_grid = np.linspace(-2, 2, 50)
y_grid = np.linspace(-2, 2, 50)
X, Y = np.meshgrid(x_grid, y_grid)
Z = X**2 - Y**2  # Saddle point / Quadrupole Potential

ax2 = fig.add_subplot(1, 2, 2, projection="3d")
surf = ax2.plot_surface(X, Y, Z, cmap="coolwarm", edgecolor="none", alpha=0.9)
fig.colorbar(surf, ax=ax2, shrink=0.5, aspect=10, label="Potential $V(x,y)$")
ax2.set_title("3D Quadrupole Potential Surface")
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_zlabel("V")

plt.tight_layout()
plt.show()
