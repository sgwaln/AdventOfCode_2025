file_path = "day6_test.txt"

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
    print(grid)
    print()
    print([row.split(' ') for row in grid])
    print()
    grid = [row.strip() for row in grid]
    grid = [row.split() for row in grid]
    print(grid)


print(f"total = {total}")