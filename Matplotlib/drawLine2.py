# NOTE: 2nd version of drawLine.py code file
# NOTE: matplotlib.use("agg") is non-GUI file to show draw line
# NOTE: This code might give some error
# First three line to make compiler able to draw

import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib
matplotlib.use("agg")


xpoint = np.array([0, 6])
ypoint = np.array([0, 250])

plt.plot(xpoint, ypoint)
plt.show()

# Two lines to make compiler able to draw
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
