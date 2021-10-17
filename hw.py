import numpy as np
import matplotlib.pyplot as plt

# Create some mock data
v = np.arange(29.25, 100, 0.1)
thrust = ((1 / 2) * (0.905) * (v ** 2) * (16.17) * (0.005)) + (
    (2) * (0.045) * ((((900) * (9.81)) ** 2)) / ((0.905) * (v ** 2) * (16.17))
)
power = ((1 / 2) * (0.905) * (v ** 3) * (16.17) * (0.005)) + (
    (2) * (0.045) * ((900) * (9.81)) / ((0.905) * (v ** 2) * (16.17))
)

fig, ax1 = plt.subplots()

color = "tab:red"
ax1.set_xlabel("Velocity (m/s)")
ax1.set_ylabel("Thrust (N)", color=color)
ax1.plot(v, thrust, color=color)
ax1.tick_params(axis="y", labelcolor=color)


ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = "tab:blue"
ax2.set_ylabel("Power (J)", color=color)  # we already handled the x-label with ax1
ax2.plot(v, power, color=color)
ax2.tick_params(axis="y", labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()
