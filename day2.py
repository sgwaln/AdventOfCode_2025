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
                    # 001001 test for n = 2, and len(n) = 3 in len(m) = 6

                    # This still has issues with len(m) is odd? say 999? Is that an invalid code?

                    for n in range(2,num_digits,2):
                        # This is checking for "0"*n + 1 + "0"*n + 1
                    
                    # I've read a little coding theory and I think I understand how to solve the general case
                    # I have a polynomical S where S = R + R*x^k where it repeats n times and R is degree k (k long - 1)
                    # i.e. n = 2, S = R+R*x^k = R(x^k + 1)
                    # i.e. n = 3, S = R+R*x^k+R*x^2k = R(x^2k + x^k + 1)
                    # i = 4, S = R + R*x^k + R*x^2k + R*x^3k = R * (x^3k + x^2k + x^k + 1)
                    # Therefor S is divisible by the n (n>=1) summed terms of x^2i where i = 0,1,2,...,k then S repeats n times, not sure if that made sense.
                    # basicly S % (x^k + 1) == 0 then repeats twice,
                    # if S % (x^2k + x^k + 1) == 0, then repeates treece
                    # note k would be N (len(S), or degree of S) / n, k = N/n => n = N/k
                    # so for a second degree S, N = 2, k = 2, then n = 1 (trivial), k = 1, then n = 2
                    # no, the values of k I have to test are floor((N+1)/2) and k is a divsor of N (N % k == 0)

                    # TODO
                        # Turn input into polynomial
                        # Find degree, and values of k and n
                        # For each k and n, see if polynomial is divisible with zero remainder by the sum of n terms of x^2i, where i = 0,1,2..,k
                        # If divisiable, add R to the total

                        pass

except Exception as e:
    print(f"An error occurred: {e}")

print(total)
print(total_2)