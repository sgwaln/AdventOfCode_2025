file_path = "day6_input.txt"

total = 0

operations = ['+','*']

with open(file_path, 'r') as file:
    grid = file.read().split('\n')
    grid = [row.strip() for row in grid]
    grid = [row.split() for row in grid]
    grid = list(zip(*grid))
    for row in grid:
        if row[len(row)-1] == '+':
            def math_op(list):
                sum = 0
                for number in list:
                    sum += int(number)
                return sum
        else:
            def math_op(list):
                product = 1
                for number in list:
                    product *= int(number)
                return product
        total += math_op(row[0:-1])
print(f"total = {total}")

total = 0
with open(file_path, 'r') as file:
    grid = file.read().split('\n')
    grid = [[char for char in word] for word in grid]
    
    row_len = max([len(row) for row in grid])
    for row in grid: # Now grid is an actual grid that preserved text jutify
        while len(row) < row_len:
            row.append('')

    product = 1
    op = ''

    for row in  range(row_len):

        operand = grid[-1][row]
        if operand in operations:
            
            if op == '*':
                total += product

            op = operand
            print(f"Next operation {op}, Current Total {total}")
            product = 1

        number = [int(digit) for digit in [grid[x][row] for x in range(0,len(grid)-1)] if digit != '' and digit != ' ']

        if number == []:
            continue

        num = 0
        for i in range(0,len(number)):
            num += number[-(i+1)] * 10**i

        if op == '+':
            total += num
        elif op == '*':
            product *= num

    if op == '*':
        total += product
    elif op == '+':
        total += num

print(f"total = {total}")