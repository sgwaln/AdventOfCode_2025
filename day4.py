file_path = "day4_input.txt"

total = 0

try:
    with open(file_path, 'r') as file:
        grid = file.read().replace('@','1').replace('.','0')

except Exception as e:
    print(f"An error occurred: {e}")

print(f"Total = {total}\r\n")