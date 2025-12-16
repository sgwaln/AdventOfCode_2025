import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Read the polygon vertices
file_path = "day9_input.txt"
cords = [tuple(int(num) for num in line.split(',', 2)) for line in open(file_path, 'r')]
vertices = np.array(cords)

# Define the rectangles to plot
rectangles = [
    {
        'vert_0': np.array([94553, 48602]),
        'vert_2': np.array([4353, 34308]),
        'area': 1289423295,
        'color': 'red',
        'label': 'Rectangle 1'
    },
    {
        'vert_0': np.array([94553, 48602]),
        'vert_2': np.array([3053, 41413]),
        'area': 657892190,
        'color': 'green',
        'label': 'Rectangle 2'
    },
    {
        'vert_0': np.array([94553, 48602]),
        'vert_2': np.array([3253, 38948]),
        'area': 881511155,
        'color': 'yellow',
        'label': 'Rectangle 3'
    }, 
    {
        'vert_0': np.array([97553, 55037]),
        'vert_2': np.array([2446, 51055]),
        'area': 378815164,
        'color': 'purple',
        'label': 'Rectangle 4'
    }
]

# Create the plot
fig, ax = plt.subplots(figsize=(12, 10))

# Draw polygon
poly_patch = Polygon(vertices, fill=False, edgecolor='blue', linewidth=2, label='Polygon')
ax.add_patch(poly_patch)

# Draw each rectangle
for rect in rectangles:
    vert_0 = rect['vert_0']
    vert_2 = rect['vert_2']
    
    # Calculate all 4 corners
    rect_corners = np.array([
        vert_0,
        [vert_0[0], vert_2[1]],
        vert_2,
        [vert_2[0], vert_0[1]]
    ])
    
    # Draw rectangle
    rect_patch = Polygon(rect_corners, fill=True, facecolor=rect['color'], 
                        alpha=0.3, edgecolor=rect['color'], linewidth=2, 
                        label=f"{rect['label']} (Area={rect['area']:,})")
    ax.add_patch(rect_patch)

ax.autoscale()
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.legend()
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Polygon with Rectangles')
plt.tight_layout()
plt.show()