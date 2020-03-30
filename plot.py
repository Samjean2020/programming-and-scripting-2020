# Jean Bonsenge
# This program displays a plot of the functions f(x) = x, g(x) = x2 and h(x) = x3 in the range [0, 4] on the one set of axes.
# numpy and matplotlib.pyplot deal respectively with numbers and plots.

import numpy as np
import matplotlib.pyplot as plt

# description of functions for plotting.

# list of values in floating-point precision type, and in one time on x-axis.
f = np.arange (0.0, 4.0, 1.0) 
# values on y-axis squared. 
g = f**2
# values on y-axis on third power or cube.
h = f**3

#  display the title.
plt.title("A Plot of Functions")
#  display label of the functions. 
plt.xlabel("values of f(x) function)")
plt.ylabel("outputs of functions g(x), h(x)")

# use the plot() command
plt.plot( f, g, h )
#  display the plot.
plt.show()
