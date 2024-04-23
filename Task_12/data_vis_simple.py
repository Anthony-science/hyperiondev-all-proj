import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 20)
y = np.sin(x)

plt.plot(x, y, label="sine")

plt.title("My first MatPlotLib sine graph")

plt.show()