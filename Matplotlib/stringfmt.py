# String format in marker
# shor form "fmt"

import matplotlib.pyplot as plt
import numpy as np

ypoint = np.array([3, 8, 1, 10])

# "o": bold point ":": dotted line, "r": red color line
# "ms" or markersize: set the size of the markers
# "mec" or markeredgecolor: set the color of the edge of the markers
# "mfc" or markerfacecolor: set the color inside the edge of the markers

plt.plot(ypoint, "o:r", ms=20, mec="g", mfc="b")
plt.show()
