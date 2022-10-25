# Emphasize each point with marker

import matplotlib.pyplot as plt
import numpy as np

ypoint = np.array([3, 8, 1, 10])

# marking each point with bold point or star
plt.plot(ypoint, marker="H")    # H = hexagonal
plt.show()
