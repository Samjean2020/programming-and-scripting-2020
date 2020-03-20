# Jean Bonsenge
# This program displays a plot of the functions f(x) = x, g(x) = x2 and h(x) = x3.

import numpy as np
import matplotlib.pyplot as plt

f = np.arange (0.0, 4.0, 1.0)
g = f**2
h = f**3

plt.title ("A Plot of Functions")

plt.plot ( f, g, h )

plt.show()
