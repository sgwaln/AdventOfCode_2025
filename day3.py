file_path = "day3_input.txt"

total = 0
number_of_batteries = 12
batteries  = [0]*number_of_batteries

def find_max(list):
    index = 0
    max = list[0]
    for i in range(1,len(list)):
        if list[i] > max:
            max = list[i]
            index = i
    return max, index

try:
    with open(file_path, 'r') as file:

        line_count = 0
        for line in file:
            line = line.strip()
            bank = [int(char) for char in line]
            bank_size = len(bank)

            batteries = bank[:number_of_batteries]
            print(f"Bank: {line}")

            start_range = 0
            end_range = bank_size - number_of_batteries + 1
            avalible_range = bank[start_range:end_range]
            batteries[0], bank_index = find_max(avalible_range)
            print(f"Start: {start_range}, End: {end_range}, Bank: {bank_index}")
            print(f"Range = {avalible_range}, Battery: {batteries[0]}")


            for battery_index in range(1,len(batteries)):
                start_range = bank_index + 1 
                end_range = bank_size - number_of_batteries + 1 + battery_index
                avalible_range = bank[start_range:end_range]
                batteries[battery_index], bank_index = find_max(avalible_range)
                print(f"Start: {start_range}, End: {end_range}, Bank: {bank_index}")
                print(f"Range = {avalible_range}, Battery: {batteries[battery_index]}")
                bank_index = start_range + bank_index

            print(f"Batteries: {batteries}")
            jolt = 0
            for battery_index in range(0,len(batteries)):
                jolt += int(batteries[battery_index] * (10**(number_of_batteries - 1 - battery_index)))
            print(f"Joltage Total: {jolt}")
            total += jolt
            print("\r\n"*2)

except Exception as e:
    print(f"An error occurred: {e}")

print(f"Total = {total}\r\n")