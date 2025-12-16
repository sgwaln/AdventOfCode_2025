import numpy as np
import matplotlib.path as mpath

file_path = "day9_input.txt"
cords = [tuple(int(num) for num in line.split(',', 2)) for line in open(file_path, 'r')]
vertices = np.array(cords)
poly = mpath.Path(vertices)

# Precompute set for O(1) lookup
vertices_set = set(map(tuple, vertices))

def vertex_check(vert):
    vert_tuple = tuple(vert)
    if vert_tuple in vertices_set:
        return True
    return poly.contains_point(vert)

def check_edges(verts):
    verts = np.array(verts)

    # The degenerte case where rect is 1xN or Nx1
    if (np.array_equal(verts[0], verts[1]) and np.array_equal(verts[2], verts[3]) or 
        np.array_equal(verts[0], verts[3]) and np.array_equal(verts[1], verts[2])):
        return poly.contains_points(verts).all()
    
    x_L = max(verts[[0,2], 0]) - 0.1 # X cord just left of right edge
    x_R = min(verts[[0,2], 0]) + 0.1 # X cord just right of left edge
    y_U = min(verts[[0,2], 1]) + 0.1 # Y cord just up of bottom edge
    y_D = max(verts[[0,2], 1]) - 0.1 # Y cord just down of top edge
    
    # Build all points at once for batch checking
    points = []
    x = np.arange(x_R, x_L, 1)
    y = np.arange(y_U, y_D, 1)
    
    for xi in x:
        points.append([xi, y_U])
        points.append([xi, y_D])
    for yi in y:
        points.append([x_L, yi])
        points.append([x_R, yi])
    
    if len(points) == 0:
        return True
    
    # Batch check all points at once - MUCH faster then poly.contains_point or so I was told
    return poly.contains_points(points).all()

max_area = 0
best_verts = None

# An output from an antempt, but was not the awnser, but look valid
# Max Area: 1289423295
# Vertices: [94553 48602] - [ 4353 34308]
max_area = 1289423295
best_verts = [[94553,48602],[ 4353,34308]]

# Sort vertices to skip symmetric checks
for i, vert_0 in enumerate(vertices):
    for vert_2 in vertices[i+1:]:  # Only check upper triangle
        # Skip if same point
        if np.array_equal(vert_0, vert_2):
            continue
        
        # Early area check - skip if can't beat current max
        potential_area = (abs(vert_2[0] - vert_0[0]) + 1) * (abs(vert_2[1] - vert_0[1]) + 1)
        if potential_area <= max_area:
            continue
        
        vert_1 = np.array([vert_0[0], vert_2[1]])
        vert_3 = np.array([vert_2[0], vert_0[1]])
        
        # Check vertices
        if not vertex_check(vert_1):
            continue
        if not vertex_check(vert_3):
            continue
        
        # Check edges
        if not check_edges([vert_0, vert_1, vert_2, vert_3]):
            continue
        
        # Found valid rectangle
        max_area = potential_area
        best_verts = (vert_0, vert_2)
        print(f"Max Area: {max_area}")
        print(f"Vertices: {vert_0} - {vert_2}")

print(f"\t\t MAX AREA IS {max_area}")

# This was not the awnser, but if it's valid, is a good spot to start from

# Max Area: 1220
# Vertices: [97633 50169] - [97633 51388]
# Max Area: 293463
# Vertices: [97633 50169] - [97553 53791]
# Max Area: 197419912
# Vertices: [97633 50169] - [ 2446 52242]
# Max Area: 314003880
# Vertices: [97553 53791] - [ 2574 57096]
# Max Area: 314096448
# Vertices: [97553 53791] - [ 2546 57096]
# Max Area: 378815164
# Vertices: [97553 55037] - [ 2446 51055]
# Max Area: 657892190
# Vertices: [94553 48602] - [ 3053 41413]
# Max Area: 767144384
# Vertices: [94553 48602] - [ 3053 40219]
# Max Area: 881511155
# Vertices: [94553 48602] - [ 3253 38948]
# Max Area: 985462142
# Vertices: [94553 48602] - [ 3493 37781]
# Max Area: 1086995157
# Vertices: [94553 48602] - [ 3493 36666]
# Max Area: 1186344432
# Vertices: [94553 48602] - [ 4021 35499]
# Max Area: 1289423295
# Vertices: [94553 48602] - [ 4353 34308]
#                  MAX AREA IS 1289423295