import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba_array

colors = []
with open("pi.txt") as f:
    for i in range(10000):
      color = "#{:06x}".format(int(f.read(7)))
      colors.append(color)

plt.imshow(to_rgba_array(colors).reshape(100,100,4))
plt.show()
