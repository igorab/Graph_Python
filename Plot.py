import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

t = np.linspace(0, 2*np.pi, 100)
a = np.cos(t)
b = np.sin(t)

ax.plot(a, b)
plt.show()
