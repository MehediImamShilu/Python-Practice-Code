# First three line to make compiler able to draw

import matplotlib.pyplot as plt
import numpy as np

xpoint = np.array([1, 8])
ypoint = np.array([3, 10])

plt.plot(xpoint, ypoint)
# for plotting without line
# plt.plot(xpoint, ypoint, "o")
plt.show()
