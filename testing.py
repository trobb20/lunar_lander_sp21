import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm

# Create a set of line segments so that we can color them individually
# This creates the points as a N x 1 x 2 array so that we can stack points
# together easily to get the segments. The segments array for line collection
# needs to be (numlines) x (points per line) x 2 (for x and y)

x1=np.linspace(0,1,100)
y1=np.sin(x1)
x2=np.linspace(1,2,100)
y2=np.sin(x2)

ln1=np.array([x1,y1]).T
ln2=np.array([x2,y2]).T

fig, axs = plt.subplots()

segments=[ln1,ln2]
print(segments)

# Use a boundary norm instead
lc = LineCollection(segments, colors=[(0,1,0),(1,0,0)])
lc.set_linewidth(2)
line = axs.add_collection(lc)

axs.set_xlim(x1.min(), x2.max())
axs.set_ylim(-1.1, 1.1)
plt.show()