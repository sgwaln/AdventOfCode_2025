import copy

file_path = "day4_input.txt"

total = 0
max_neigbors = 4
empty = 0

def count_neigbors(grid,pos_x,pos_y):
    y_max = len(grid)
    x_max = len(grid[0])
    count = 0

    for x in range(-1,1+1):

        x_cord = pos_x + x
        if x_cord < 0 or x_cord >= x_max:
            continue

        for y in range(-1,1+1):
            if x == 0 and y == 0: # Don't count yourself
                continue
            
            y_cord = pos_y + y
            if y_cord < 0 or y_cord >= y_max:
                continue

            if grid[y_cord][x_cord] != empty:
                count += 1
    return count

try:
    with open(file_path, 'r') as file:
        grid = list(file.read().replace('@','1').replace('.','0').split('\n'))
        grid_new = [[int(digit) for digit in row] for row in grid]

        grid_old = [[0 for _ in range(len(grid_new[0]))] for _ in range(len(grid_new))]

        y_max = len(grid)
        x_max = len(grid[0])

        interations = 0

        while grid_new != grid_old:
            grid_old = copy.deepcopy(grid_new)  # Create a true copy            print('-'*50)
            print(f"Interation: {interations}")            
            for y in range(0,y_max):
                for x in range(0,x_max):
                    if grid_old[y][x] != empty:
                        if count_neigbors(grid_old,x,y) < max_neigbors:
                            total += 1
                            grid_new[y][x] = 0
            interations += 1


except Exception as e:
    print(f"An error occurred: {e}")

print(f"Total = {total}\r\n")