file_path = "day3_input.txt"

total = 0
try:
    with open(file_path, 'r') as file:

        line_count = 0
        for line in file:
            line = line.strip()

            pressident = int(line[0])
            vp = int(line[1])

            for index in range(1,len(line)-1):
                candidate = int(line[index])

                if candidate > pressident: # Tens is bigger, so number bigger, assume index after as vp
                    pressident = candidate
                    vp = int(line[index + 1])
                elif candidate > vp: # While the pressident didn't get beat, the VP still can
                    vp = candidate

            # Didn't catch the edge case of last number in line being larger then vp
            last = int(line[-1])
            if last > vp:
                vp = last

            total += pressident*10 + vp
            line_count += 1
            print(f"P:{pressident} VP:{vp}\t Total: {total} \t Line Number: {line_count-1}")
        
except Exception as e:
    print(f"An error occurred: {e}")

print(f"Total = {total}\r\n")