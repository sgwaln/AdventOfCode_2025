file_path = "day9_test.txt"
coords = [tuple(int(num) for num in line.split(',', 2)) for line in open(file_path, 'r') ]

max_area = 0
for x_1,y_1 in coords:
    for x_2,y_2 in coords:
        area = abs(x_2 - x_1 + 1) * abs(y_2 - y_1 + 1)
        if area > max_area:
            max_area = area
print(max_area)

max_area = 0
for x_1,y_1 in coords:
    for x_2,y_2 in coords:

        # Check if rectagle is in alowable area
        # I think I can do this by checking if a point of the polygon is concave, but how do I do that.
        # I could find all the allowable points and check if rectangle is in the allowable space    

        area = abs(x_2 - x_1 + 1) * abs(y_2 - y_1 + 1)
        if area > max_area:
            max_area = area
print(max_area)