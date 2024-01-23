import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize


def fnc(x, y):
    f = 0.25 * np.sin(0.5 * x ** 2 - y) - np.exp(-((x - 5) ** 2 + (y - 2) ** 2))
    return f  # x**4 - y**4

def func(x):
    f = 0.25 * np.sin(0.5 * x[0] ** 2 - x[1]) - np.exp(-((x[0] - 5) ** 2 + (x[1] - 2) ** 2))
    return f  # x**4 - y**4



# x = np.linspace(2, 8, 100)
# y = np.linspace(0, 5, 100)

# X, Y = np.meshgrid(x, y)

# Z = fnc(X, Y)

# fig, ax = plt.subplots(1, 1, figsize=(5, 5), subplot_kw={'projection': '3d'})

# ax.plot_surface(X, Y, Z/Z.max(), cmap=plt.cm.ocean_r)
# ax.view_init(30, 60)
# plt.show()


#f = optimize.rosen

f = func


def plot_surface():
    n_points = 100
    x = np.linspace(2, 8, n_points)
    y = np.linspace(0, 5, n_points)
    xx, yy = np.meshgrid(x, y)
    X = np.vstack([xx.flatten(), yy.flatten()])
    zz = f(X).reshape(n_points, n_points)

    levels = np.hstack([np.linspace(0, 200, 25), np.linspace(250, 2000, 25)])

    fig, ax = plt.subplots(figsize=(11, 10), layout="tight")
    cf = ax.contourf(xx, yy, zz, levels=levels, cmap="coolwarm")
    cbar = fig.colorbar(cf)
    ax.set_xlabel("$x$")
    ax.set_ylabel("$y$")
    cbar.set_label("$z$")
    ax.scatter([1], [1], marker="*", s=200, color="violet", label="глобальный минимум")
    return ax


plot_surface()

solution = optimize.minimize(f, x0=[5, 2])
print(solution)

ax = plot_surface()
ax.scatter(solution.x[0], solution.x[1], color="red", label="найденный минимум")
ax.legend()

plt.show()
