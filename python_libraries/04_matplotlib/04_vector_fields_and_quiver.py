import numpy as np
import matplotlib.pyplot as plt

# Define 2D Grid
x = np.linspace(-3, 3, 20)
y = np.linspace(-3, 3, 20)
X, Y = np.meshgrid(x, y)

# Vector Field Components (e.g., Dipole Electric Field or Rigid Body Rotation)
# Rotating fluid field: U = -Y, V = X
U = -Y
V = X
speed = np.sqrt(U**2 + V**2)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# 1. Quiver Plot (Arrows at discrete grid nodes)
q = ax1.quiver(X, Y, U, V, speed, cmap="autumn", pivot="middle")
fig.colorbar(q, ax=ax1, label="Field Magnitude")
ax1.set_title("Vector Field Arrows (quiver)")
ax1.set_xlabel("$x$")
ax1.set_ylabel("$y$")

# 2. Streamline Plot (Continuous field line paths)
# Requires denser mesh for smooth lines
x_dense = np.linspace(-3, 3, 50)
y_dense = np.linspace(-3, 3, 50)
Xd, Yd = np.meshgrid(x_dense, y_dense)
Ud, Vd = -Yd, Xd
speed_d = np.sqrt(Ud**2 + Vd**2)

strm = ax2.streamplot(Xd, Yd, Ud, Vd, color=speed_d, cmap="winter", density=1.2)
fig.colorbar(strm.lines, ax=ax2, label="Field Magnitude")
ax2.set_title("Field Streamlines (streamplot)")
ax2.set_xlabel("$x$")
ax2.set_ylabel("$y$")

plt.tight_layout()
plt.show()
