import math

file_path = "day8_input.txt"

number_of_connections = 1000
number_of_circuits = 3

def find_clusters_from_neigbhoors(nearest_neigboors):
    clusters = []
    visted = set()
    
    for i in range(len(nearest_neigboors)):
        if i in visted:
            continue # skip if already in a cluster

        current_cluster = set() # Starting a cluster at i
        to_vist = [i]           # Queue of points to explore

        while to_vist:
            current = to_vist.pop() # Get the next point to explore and remove it form to-do list
            if current in current_cluster:
                continue # Already added this point

            current_cluster.add(current)
            visted.add(current)

            neighbor = nearest_neigboors[current]
            if neighbor not in current_cluster:
                to_vist.append(neighbor) # Got to look at this one next

            for j, nn in enumerate(nearest_neigboors): # Find all points that point to current point and add them
                if nn == current and j not in current_cluster:
                    to_vist.append(j)

        clusters.append(current_cluster)
    return clusters

def find_clusters_from_connections(connections):
    clusters = []
    visited = set()
    
    # Build adjacency list (who's connected to whom)
    graph = {}
    for a, b in connections:
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    
    # Find connected components
    for node in graph:
        if node in visited:
            continue
        
        # Start new cluster
        cluster = set()
        to_visit = [node]
        
        while to_visit:
            current = to_visit.pop()
            if current in cluster:
                continue
            
            cluster.add(current)
            visited.add(current)
            
            # Add all neighbors to explore
            for neighbor in graph[current]:
                if neighbor not in cluster:
                    to_visit.append(neighbor)
        
        clusters.append(cluster)
    
    return clusters

def find_distance_sqrd(vec_1, vec_2):
    if len(vec_1) != len(vec_2):
        print("ERROR, vectors not same size")
        return "ERROR"
    distance_sqr = sum((a - b)**2 for a, b in zip(vec_1, vec_2))
    return distance_sqr

def find_min(list_of_lists, exclude=None,skip_rows=None):
    min_value, min_row, min_col = min(
        (value, i, j)
        for i, sublist in enumerate(list_of_lists)
        if i not in skip_rows
        for j, value in enumerate(sublist)
        if value != exclude
    )
    return min_value, min_row, min_col

coords = [tuple(int(num) for num in line.split(',', 3)) for line in open(file_path, 'r') ]
number_of_breakers = len(coords)
distance_matrix = [[0] * number_of_breakers for _ in range(number_of_breakers)]

print("Step 1: Calculating distance matrix")
for i in range(number_of_breakers):
    for j in range(number_of_breakers):
        distance_matrix[i][j] = find_distance_sqrd(coords[i],coords[j])

print(f"Step 2: Finding {number_of_connections} shortest connections") # This is incredibly slow
visited = set()
connections = [[0]*2 for _ in range(number_of_connections)]
visited_pairs = set() # The matrix is symetrical, the distance to 1 from 2 is the same as 2 to 1, so I need to not include both

for i in range(number_of_connections):
    min_val, breaker_index, neighbor_index = min(
        (value, row_idx, col_idx)
        for row_idx, row in enumerate(distance_matrix)
        if row_idx not in visited
        for col_idx, value in enumerate(row)
        if value != 0
        and (row_idx, col_idx) not in visited_pairs
        and (col_idx, row_idx) not in visited_pairs  # Check reverse too
    )
    
    visited.add(breaker_index)
    visited_pairs.add((breaker_index, neighbor_index))
    visited_pairs.add((neighbor_index, breaker_index))  # Add both directions
    connections[i] = [breaker_index, neighbor_index]

print("Step 3: Form connections into circuits")
circuits = find_clusters_from_connections(connections)
lengths = [len(circuit) for circuit in circuits]
lengths.sort(reverse=True)

print(f"Step 4: Product of the number of breakers in {number_of_circuits} largest circuits")
print(f"\tOutput: {math.prod(lengths[0:number_of_circuits])}") # Not 14196
    
