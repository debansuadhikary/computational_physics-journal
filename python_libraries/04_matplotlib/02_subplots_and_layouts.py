import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 5, 200)
position = np.cos(3.0 * t)
velocity = -3.0 * np.sin(3.0 * t)

# 1. Standard 2x1 Vertical Subplot Layout
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

# Top Panel: Position
ax1.plot(t, position, color="royalblue", linewidth=2)
ax1.set_ylabel("Position $x$ (m)", fontsize=11)
ax1.set_title("Harmonic Motion Kinematics", fontsize=13, fontweight="bold")
ax1.grid(True, alpha=0.5)

# Bottom Panel: Velocity
ax2.plot(t, velocity, color="darkorange", linewidth=2)
ax2.set_xlabel("Time $t$ (s)", fontsize=11)
ax2.set_ylabel("Velocity $v$ (m/s)", fontsize=11)
ax2.grid(True, alpha=0.5)

plt.tight_layout()  # Adjust spacing automatically
plt.show()

# 2. Advanced Layout: Phase Space Plot alongside Time Series (GridSpec)
fig = plt.figure(figsize=(10, 4))
gs = fig.add_gridspec(1, 2, width_ratios=[2, 1])

ax_time = fig.add_subplot(gs[0])
ax_phase = fig.add_subplot(gs[1])

# Left: Time series
ax_time.plot(t, position, label="x(t)", color="royalblue")
ax_time.plot(t, velocity, label="v(t)", color="darkorange")
ax_time.set_xlabel("Time (s)")
ax_time.set_ylabel("State Variables")
ax_time.set_title("Time Evolution")
ax_time.legend()
ax_time.grid(True, alpha=0.5)

# Right: Phase space trajectory (v vs x)
ax_phase.plot(position, velocity, color="purple", linewidth=1.5)
ax_phase.set_xlabel("Position $x$")
ax_phase.set_ylabel("Velocity $v$")
ax_phase.set_title("Phase Space Portrait")
ax_phase.grid(True, alpha=0.5)

plt.tight_layout()
plt.show()
