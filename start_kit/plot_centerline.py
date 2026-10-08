import matplotlib.pyplot as plt
import numpy as np

x, y, left, right = np.loadtxt("centerline.csv", delimiter=",", skiprows=1, unpack=True)
tx, ty = np.gradient(x), np.gradient(y)
norm = np.hypot(tx, ty)
nx, ny = -ty / norm, tx / norm  # unit normal pointing left

plt.plot(x, y, "k--", lw=0.8, label="centerline")
plt.plot(x + nx * left, y + ny * left, label="left wall")
plt.plot(x - nx * right, y - ny * right, label="right wall")
plt.plot(x[0], y[0], "go", label="start")
plt.axis("equal")
plt.legend()
plt.show()
