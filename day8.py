import numpy as np
file_path = "day8_test.txt"

circuits = 0

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
        
    print(nearest_neigboors)

    clusters = []
    visted = set()
    
    # I did this wrong, I needed to find the 10 shorts connection and cluster them into circuits, not find the clusters that minimize total distance
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
    print(clusters)
    sizes = [len(cluster) for cluster in clusters]

    print(len(clusters)) # Should be 6
    print(sizes) # Three largest should multiply to 40, that being 5, 4, and 2
    

print('='*30)
print(f"Circuits = {circuits}")
