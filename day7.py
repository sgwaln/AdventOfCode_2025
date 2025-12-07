file_path = "day7_input.txt"

total_splits = 0
time_line_splits = 0

with open(file_path, 'r') as file:

    # grid = file.read().split('\n') 
    # grid = [list(row) for row in grid]

    # for row_index in range(0,len(grid)):
    #     for spot_index in range(0,len(grid[row_index])):
    #         if (grid[row_index][spot_index] == '|' or
    #             grid[row_index][spot_index] == 'S'): # Need to propagate beam

    #             if row_index + 1 >= len(grid):
    #                 break

    #             spot_below = grid[row_index+1][spot_index]

    #             if  spot_below == '^':
    #                 total_splits += 1
    #                 if spot_index - 1 >= 0:
    #                     if grid[row_index+1][spot_index-1] == '.':
    #                         grid[row_index+1][spot_index-1] = '|'

    #                 if spot_index + 1 < len(grid[row_index+1]):
    #                     if grid[row_index+1][spot_index+1] =='.':
    #                         grid[row_index+1][spot_index+1] = '|'

    #             elif spot_below == '.':
    #                     grid[row_index+1][spot_index] = '|'

    #for row in grid:
    #    print("".join(row))


    # Now dealint with part two, where their is one particle but multiple timelines
    # I think this is tree data structure?
    # My plan is start going left at every split,
    # Then hit the bottom and go back a split, and go right insted, 
    # then keep going left until the bottom and go back again, and again and again until I know all paths
    # 
    # 
    # Is their a better way? This seems really slow, 
    # Can I leverage the previous solution somehow?
    # Each split splits the beam into atleast two time lines,
    # so each "|^|" would add a time line?
    # No, if a beam got split earlier, and two timelins endup at the same splitter would add more time time lines
    # Could I go though the splitters row by row, but keep track of how many timelines are in a given spot, instead of just progating the beam

    grid = file.read().split('\n') 
    grid = [list(row) for row in grid]
    
    for y_index in range(len(grid)):
        for x_index in range(len(grid[y_index])):
            if grid[y_index][x_index] == '.':
                grid[y_index][x_index] = '0'
            elif grid[y_index][x_index] == 'S':
                grid[y_index][x_index] = '1'

    for row_index in range(0,len(grid)):
        for spot_index in range(0,len(grid[row_index])):

            current_slot = grid[row_index][spot_index]

            if row_index + 1 >= len(grid):
                break
            elif current_slot == '0': # No need to propagate this
                continue
            elif current_slot == '^':
                continue

            if  grid[row_index+1][spot_index] == '^': # Checking spot below to see if its a splitter
                if spot_index - 1 >= 0: # Got to propagate left
                    grid[row_index+1][spot_index-1] = str(int(grid[row_index+1][spot_index-1]) + int(current_slot))

                if spot_index + 1 < len(grid[row_index+1]): # got to propagate right
                    grid[row_index+1][spot_index+1] = str(int(grid[row_index+1][spot_index+1]) + int(current_slot))

            else: # Spot below is empty, propgate down
                grid[row_index+1][spot_index] = str(int(current_slot) + int(grid[row_index+1][spot_index]))

time_line_splits = sum([int(index) for index in grid[-1]])

print('='*30)
print(f"Total Splits = {total_splits}")
print(f"Total Time Lines = {time_line_splits}")
