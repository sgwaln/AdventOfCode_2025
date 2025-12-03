file_path = "day2_input.txt"

total = 0

try:
    with open(file_path, 'r') as file:
        for line in file:
            full_id = line.split(',',-1)
            for double_id in full_id:
                ids = double_id.split('-',-1)
                for id in ids:
                    print(id)
                    length = len(id)

                    # Cant have a repeat if its only 1 number long, or starts with a zero
                    if length <= 1 or id[0] == 0:
                        next

                    for digiit in range(0,length):
                        pass


except Exception as e:
    print(f"An error occurred: {e}")
