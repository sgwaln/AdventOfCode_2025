import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np
import matplotlib.path as mpath

file_path = "day9_input.txt"
cords = [tuple(int(num) for num in line.split(',', 2)) for line in open(file_path, 'r')]
vertices = np.array(cords)
poly = mpath.Path(vertices)

fig, ax = plt.subplots(figsize=(10, 10))

# Draw polygon
poly_patch = Polygon(vertices, fill=False, edgecolor='blue', linewidth=2, label='Polygon')
ax.add_patch(poly_patch)

# Draw best rectangle

best_verts = [[94553,48602],[4353,34308]]
max_area = 1289423295

if best_verts is not None:
    vert_0, vert_2 = best_verts
    rect_corners = np.array([
        vert_0,
        [vert_0[0], vert_2[1]],
        vert_2,
        [vert_2[0], vert_0[1]]
    ])
    rect_patch = Polygon(rect_corners, fill=True, facecolor='red', 
                        alpha=0.3, edgecolor='red', linewidth=2, 
                        label=f'Max Rectangle (Area={max_area})')
    ax.add_patch(rect_patch)

ax.autoscale()
ax.set_aspect('equal')
ax.grid(True)
ax.legend()
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Polygon with Maximum Rectangle')
plt.show()