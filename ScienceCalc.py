from scipy.optimize import differential_evolution
from scipy.optimize import minimize
import numpy as np
from scipy.integrate import quad, dblquad, odeint


def pend(y, t, b, c):

    theta, omega = y
    e = lambda x: np.exp(-x)
    dydt = odeint(omega, -b*omega, - e(theta))
    return dydt

t0 = float(input())

dt = 0.001
t = np.arange(0, 10, dt)

b = 0.25
c = 5.0

y0 = [np.pi - 0.1, 0.0]

t = np.linspace(0, 10, 101)


sol = odeint(pend, y0, t, args=(b, c))


import matplotlib.pyplot as plt
plt.plot(t, sol[:, 0], 'b', label='theta(t)')
plt.plot(t, sol[:, 1], 'g', label='omega(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()

# result = differential_evolution(func, [(dx, xmax)])
# print(*result.x)
# result = minimize(func, 0)
# print(round(*result.x, 1))