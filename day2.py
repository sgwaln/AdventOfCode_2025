file_path = "day2_input.txt"

total = 0
total_2 = 0

try:
    with open(file_path, 'r') as file:
        for line in file:
            id_ranges = line.split(',',-1)
            id_ranges = [id.split('-',-1) for id in id_ranges]
            id_ranges = [[int(x) for x in str] for str in id_ranges]

            for id_range in id_ranges:
                for num in range(id_range[0],id_range[1]+1):
                    
                    # Can't have repeated digits if only one digit
                    if num < 10:
                        continue
                    
                    # For the number to be repeated, it has to have total even number of digits
                    num_digits = len(str(num))
                    if num_digits % 2 != 0:
                        continue

                    # repeated number are always divisable by the number and result in a leading one, zeros and a one
                    # i.e. 1188511885 / 11885 = 100001, where the resultant is one digit longer then the repition
                    # therefor, if the number is remainder 0 of 10^x+1 then its a repeated digits
                    # I think this is related to polynomial division?
                    # I belive the pattern is the number of zeros in the 1s sandwidch 
                    # Never mind, I don't think this will work
                    # i.e. 8008/1001 = 8
                    # Well its less then 10, so it can't be

                    # could also split the number directly in half and compare strings, which I think is simpler
                    num_str = str(num)
                    num_left = num_str[0:((num_digits//2))]
                    num_right = num_str[(num_digits//2):]
                    if num_left == num_right:
                        total += int(num)

                    max_zeros = num_digits//2 - 1
                    div = int("1" + ("0"*max_zeros) + "1")
                    if num % div == 0 :
                        total_2 += num

                    # So, I think I have a way to the general case of x*n where x is repeated n times
                    # i.e. 10101 tests for n = 3, and len(n) = 2 (number of zeros between ones + 1)
                    # i.e. 1001001 test for n = 3, len(n) = 3
                    # 1010101 test for n = 4, and len(n) = 2

                    

except Exception as e:
    print(f"An error occurred: {e}")

print(total)
print(total_2)