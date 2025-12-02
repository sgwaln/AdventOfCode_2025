file_path = "day1_input.txt"

position = 50 # Intial position is 50
zero_count = 0
circle_size = 100

try:
    with open(file_path, 'r') as file:
        for line in file:
            move = int(line[1:])
            if line[0] == 'R':
                position = (position - move) % circle_size

            elif line[0] == 'L':
                position = (position + move) % circle_size
            else:
                break
            
            if position == 0:
                zero_count += 1
                print(zero_count)

    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")