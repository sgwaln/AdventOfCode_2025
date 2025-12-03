file_path = "day1_input.txt"

position = 50 # Intial position is 50
zero_count = 0
circle_size = 100

try:
    with open(file_path, 'r') as file:
        for line in file:
            move = int(line[1:])

            print(f"Pos: {position} Zeros: {zero_count} \r\n\t Move: {line[0]} {move}")

            num_rotations = move // circle_size
            if num_rotations > 0:
                zero_count += num_rotations
                move %= circle_size
                
            print(f"\t Rotations: {num_rotations}")

            if line[0] == 'L':
                move = -move
            elif line[0] != 'R':
                print("ERROR")
                break

            # I didn't start on zero, and my move would move me past zero, add a count
            if position != 0 and ((position + move) < 0 or (position + move) > 100):
                    zero_count += 1

            position = (position + move) % circle_size
            
            # I ended on zero, add a count
            if position == 0:
                 zero_count += 1

            print(f"\t Final Zeros: {zero_count}")
            print(f"\t Final Pos: {position}")

except Exception as e:
    print(f"An error occurred: {e}")

print(f"Count = {zero_count}")