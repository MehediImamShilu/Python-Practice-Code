# Line graph

import matplotlib.pyplot as plt
import numpy as np

ypoint1 = np.array([3, 8, 1, 10])
ypoint2 = np.array([6, 9, 3, 8])

plt.plot(ypoint1, linestyle="--", linewidth=10, color="red")
plt.plot(ypoint2, linestyle=":", color="green")
plt.show()
