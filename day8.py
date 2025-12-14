import numpy as np
import math
file_path = "day8_test.txt"

number_of_connections = 10
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

with open(file_path, 'r') as file:

    coords = [tuple(int(num) for num in line.split(',', 3)) for line in file]

    nearest_neigboors = []
    for i in range(0,len(coords)):
        i_vec = coords[i]
        distance_vec = []
        
        for j in range(0,len(coords)):
            
            if i == j:
                continue

            j_vec = coords[j]
            range_vec = [i_vec[k] - j_vec[k] for k in range(3)]
            distance_sqr = sum([dim**2 for dim in range_vec])
            distance_vec.append(distance_sqr)

        min_index = distance_vec.index(min(distance_vec))
        if min_index >= i: # Means it was appending after I skipped repeat case, so I have to correct for that
            min_index += 1
        
        nearest_neigboors.append(min_index)
        
    # finding the 10 nearest connections and clustering those
    visted = set()
    connections = []

    for i in range(number_of_circuits):
        # Check if any unvisited remain
        unvisited_vals = [val for j, val in enumerate(distance_vec) if j not in visted]
        if not unvisited_vals:
            break
        
        min_val = min(unvisited_vals)
        min_index = distance_vec.index(min_val)
        neighbor_index = nearest_neigboors[min_index]
        visted.add(min_index)
        connections.append([min_index, neighbor_index])

    circuits = find_clusters_from_connections(connections)
    lengths = [len(circuit) for circuit in circuits]
    lengths.sort(reverse=True)
    print(lengths)
    print(lengths[0:number_of_connections])
    print(math.prod(lengths[-1:-4:-1]))
    
