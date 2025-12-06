file_path = "day5_input.txt"

total = 0

check = 1
ranges = 0
state = ranges

id_ranges= []

def checkId(id,id_ranges):
    for id_range in id_ranges:
        if id >= id_range[0] and id <= id_range[1]:
            return 1
    return 0

try:
    with open(file_path, 'r') as file:

        for line in file:

            if line == "\n":
                state = check
                continue

            if state == ranges:
                temp_range = line.strip().split('-')
                temp_range = [int(num) for num in temp_range]
                id_ranges.append(temp_range)

            if state == check:
                id = int(line.strip())
                total += checkId(id,id_ranges)

except Exception as e:
    print(f"An error occurred: {e}")

print(f"Total = {total}\r\n")
total = 0

try:
    with open(file_path, 'r') as file:

        for line in file:

            if line == "\n":
                state = check
                break

    
        sorted_id_ranges = sorted(id_ranges,key=lambda x : x[0]) # Sorted ranges by starting point, having it sorted makes it much easier to detect overlap
        merged_id_ranges = [] # will be the compress arrays, removing all overlap
        for start, end in sorted_id_ranges:
            if merged_id_ranges and start <= merged_id_ranges[-1][1] + 1:
                # Overlaps or adjacent - extend the last range
                merged_id_ranges[-1] = (merged_id_ranges[-1][0], max(merged_id_ranges[-1][1], end))
            else:
                # No overlap - add new range
                merged_id_ranges.append((start, end))
        
        total = sum(end - start + 1 for start, end in merged_id_ranges)
    
except Exception as e:
    print(f"An error occurred: {e}")

print(f"Total = {total}\r\n")