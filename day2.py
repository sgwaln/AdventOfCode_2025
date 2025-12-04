file_path = "day2_input.txt"

total = 0
total_2 = 0

def strip_leading_zeros(poly):
    """Remove leading zeros from polynomial"""
    while len(poly) > 1 and poly[0] == 0:
        poly = poly[1:]
    return poly if poly else [0]

def degree(poly):
    """
    Docstring for degree
        Poly must be in DESCENDING ORDER
    :param poly: Description
    """
    for i in range(0, len(poly)):
        if poly[i] != 0:
            break
    return len(poly) - 1 - i

def lead(poly):
    """
        Poly must be in DESCENDING order
    """
    for i in range(0, len(poly)):
        if poly[i] != 0:
            break
    return poly[i]

def poly_mult_scalar(poly, scalar):
    """Multiply polynomial by a scalar"""
    return [coef * scalar for coef in poly]

def poly_mult(poly1, poly2):
    """Multiply two polynomials in descending order"""
    if not poly1 or not poly2:
        return [0]
    
    m = len(poly1)
    n = len(poly2)
    
    # Result degree = deg(poly1) + deg(poly2)
    prod = [0] * (m + n - 1)
    
    # For descending order arrays
    for i in range(m):
        for j in range(n):
            prod[i + j] += poly1[i] * poly2[j]
    
    return prod

def poly_sub(poly1, poly2):
    """Subtract poly2 from poly1 (both in descending order)"""
    length = max(len(poly1), len(poly2))
    sub = [0] * length
    
    for i in range(1, length + 1):
        if i > len(poly1):
            sub[-i] = 0 - poly2[-i]
        elif i > len(poly2):
            sub[-i] = poly1[-i] - 0
        else:        
            sub[-i] = poly1[-i] - poly2[-i]
    return sub

def poly_divide(dividend, divisor):
    """"
    Divisor and dividend are in DESCENDING order
    Returns (quotient, remainder)
    """
    # This funciton was mostly from claude.ai

    # Check for zero divisor
    if all(coef == 0 for coef in divisor):
        return "ERROR: Division by zero polynomial"
    
    # If dividend degree < divisor degree
    if degree(dividend) < degree(divisor):
        return [0], dividend
    
    quotient = []
    remainder = dividend.copy()
    
    divisor_degree = degree(divisor)
    divisor_lead = lead(divisor)
    
    # Track expected quotient degree for proper padding
    expected_quotient_degree = degree(dividend) - divisor_degree
    current_quotient_degree = expected_quotient_degree
    
    while degree(remainder) >= divisor_degree:
        # Check if remainder is zero
        if all(coef == 0 for coef in remainder):
            break
            
        # Calculate next quotient term
        remainder_lead = lead(remainder)
        quotient_term = remainder_lead / divisor_lead
        
        # Calculate what degree this quotient term represents
        term_degree = degree(remainder) - divisor_degree
        
        # If we skipped degrees (shouldn't happen in normal division), pad with zeros
        while current_quotient_degree > term_degree:
            quotient.append(0)
            current_quotient_degree -= 1
        
        quotient.append(quotient_term)
        current_quotient_degree -= 1
        
        # Multiply divisor by quotient term
        deg_diff = degree(remainder) - degree(divisor)
        subtrahend = poly_mult_scalar(divisor, quotient_term)
        
        # Pad subtrahend with zeros at the end (lower degree terms)
        subtrahend = subtrahend + [0] * deg_diff
        
        # Subtract from remainder
        remainder = poly_sub(remainder, subtrahend)
        
        # Remove leading term (should be zero or very close to zero)
        remainder = remainder[1:]
        
        # Strip leading zeros from remainder
        while len(remainder) > 1 and abs(remainder[0]) < 1e-9:
            remainder = remainder[1:]
        
        if not remainder:
            remainder = [0]
            break
    
    # Pad quotient with trailing zeros if needed
    while current_quotient_degree >= 0:
        quotient.append(0)
        current_quotient_degree -= 1
    
    # Clean up quotient and remainder
    if not quotient:
        quotient = [0]
    
    if not remainder or all(coef == 0 for coef in remainder):
        remainder = [0]
    
    return quotient, remainder


def test_poly_divide():
    """Test cases for polynomial division"""
    
    print("=" * 60)
    print("POLYNOMIAL DIVISION TEST CASES")
    print("=" * 60)
    
    # Test 1: Simple division with no remainder
    print("\nTest 1: (x^2 - 1) / (x - 1)")
    print("Expected: Quotient = [1, 1] (x + 1), Remainder = [0]")
    dividend = [1, 0, -1]  # x^2 - 1
    divisor = [1, -1]       # x - 1
    q, r = poly_divide(dividend, divisor)
    print(f"Result:   Quotient = {q}, Remainder = {r}")
    print("PASS" if (close_enough(q, [1, 1]) and close_enough(r, [0])) else "FAIL")
    
    # Test 2: Division with remainder
    print("\nTest 2: (x^2 + 3x + 5) / (x + 1)")
    print("Expected: Quotient = [1, 2] (x + 2), Remainder = [3]")
    dividend = [1, 3, 5]   # x^2 + 3x + 5
    divisor = [1, 1]       # x + 1
    q, r = poly_divide(dividend, divisor)
    print(f"Result:   Quotient = {q}, Remainder = {r}")
    print("PASS" if (close_enough(q, [1, 2]) and close_enough(r, [3])) else "FAIL")
    
    # Test 3: Dividend degree < divisor degree
    print("\nTest 3: (x + 1) / (x^2 + 1)")
    print("Expected: Quotient = [0], Remainder = [1, 1]")
    dividend = [1, 1]      # x + 1
    divisor = [1, 0, 1]    # x^2 + 1
    q, r = poly_divide(dividend, divisor)
    print(f"Result:   Quotient = {q}, Remainder = {r}")
    print("PASS" if (close_enough(q, [0]) and close_enough(r, [1, 1])) else "FAIL")
    
    # Test 4: Division by constant
    print("\nTest 4: (2x^2 + 4x + 6) / (2)")
    print("Expected: Quotient = [1, 2, 3] (x^2 + 2x + 3), Remainder = [0]")
    dividend = [2, 4, 6]   # 2x^2 + 4x + 6
    divisor = [2]          # 2
    q, r = poly_divide(dividend, divisor)
    print(f"Result:   Quotient = {q}, Remainder = {r}")
    print("PASS" if (close_enough(q, [1, 2, 3]) and close_enough(r, [0])) else "FAIL")
    
    # Test 5: Division resulting in constant quotient
    print("\nTest 5: (3x + 6) / (x + 2)")
    print("Expected: Quotient = [3], Remainder = [0]")
    dividend = [3, 6]      # 3x + 6
    divisor = [1, 2]       # x + 2
    q, r = poly_divide(dividend, divisor)
    print(f"Result:   Quotient = {q}, Remainder = {r}")
    print("PASS" if (close_enough(q, [3]) and close_enough(r, [0])) else "FAIL")
    
    # Test 6: Higher degree polynomial
    print("\nTest 6: (x^3 + 2x^2 - 5x - 6) / (x + 1)")
    print("Expected: Quotient = [1, 1, -6] (x^2 + x - 6), Remainder = [0]")
    dividend = [1, 2, -5, -6]  # x^3 + 2x^2 - 5x - 6
    divisor = [1, 1]           # x + 1
    q, r = poly_divide(dividend, divisor)
    print(f"Result:   Quotient = {q}, Remainder = {r}")
    print("PASS" if (close_enough(q, [1, 1, -6]) and close_enough(r, [0])) else "FAIL")
    
    # Test 7: Division with fractional coefficients
    print("\nTest 7: (x^2 + x + 1) / (2x + 2)")
    print("Expected: Quotient = [0.5, 0] (0.5x), Remainder = [1]")
    dividend = [1, 1, 1]   # x^2 + x + 1
    divisor = [2, 2]       # 2x + 2
    q, r = poly_divide(dividend, divisor)
    print(f"Result:   Quotient = {q}, Remainder = {r}")
    print("PASS" if (close_enough(q, [0.5, 0]) and close_enough(r, [1])) else "FAIL")

    # Test 8: Both same degree
    print("\nTest 8: (2x^2 + 3x + 1) / (x^2 + 1)")
    print("Expected: Quotient = [2], Remainder = [3, -1]")
    dividend = [2, 3, 1]   # 2x^2 + 3x + 1
    divisor = [1, 0, 1]    # x^2 + 1
    q, r = poly_divide(dividend, divisor)
    print(f"Result:   Quotient = {q}, Remainder = {r}")
    print("PASS" if (close_enough(q, [2]) and close_enough(r, [3, -1])) else "FAIL")
    
    # Test 9: Dividing by itself
    print("\nTest 9: (x^2 + 2x + 1) / (x^2 + 2x + 1)")
    print("Expected: Quotient = [1], Remainder = [0]")
    dividend = [1, 2, 1]   # x^2 + 2x + 1
    divisor = [1, 2, 1]    # x^2 + 2x + 1
    q, r = poly_divide(dividend, divisor)
    print(f"Result:   Quotient = {q}, Remainder = {r}")
    print("PASS" if (close_enough(q, [1]) and close_enough(r, [0])) else "FAIL")
    
    # Test 10: Long division
    print("\nTest 10: (x^4 - 1) / (x - 1)")
    print("Expected: Quotient = [1, 1, 1, 1] (x^3 + x^2 + x + 1), Remainder = [0]")
    dividend = [1, 0, 0, 0, -1]  # x^4 - 1
    divisor = [1, -1]            # x - 1
    q, r = poly_divide(dividend, divisor)
    print(f"Result:   Quotient = {q}, Remainder = {r}")
    print("PASS" if (close_enough(q, [1, 1, 1, 1]) and close_enough(r, [0])) else "FAIL")
    
    # Test 11: Negative coefficients
    print("\nTest 11: (-x^2 + 4) / (x + 2)")
    print("Expected: Quotient = [-1, 2] (-x + 2), Remainder = [0]")
    dividend = [-1, 0, 4]  # -x^2 + 4
    divisor = [1, 2]       # x + 2
    q, r = poly_divide(dividend, divisor)
    print(f"Result:   Quotient = {q}, Remainder = {r}")
    print("PASS" if (close_enough(q, [-1, 2]) and close_enough(r, [0])) else "FAIL")
    
    # Test 12: Zero dividend
    print("\nTest 12: (0) / (x + 1)")
    print("Expected: Quotient = [0], Remainder = [0]")
    dividend = [0]         # 0
    divisor = [1, 1]       # x + 1
    q, r = poly_divide(dividend, divisor)
    print(f"Result:   Quotient = {q}, Remainder = {r}")
    print("PASS" if (close_enough(q, [0]) and close_enough(r, [0])) else "FAIL")
    
    print("\n" + "=" * 60)

def close_enough(list1, list2, tolerance=1e-9):
    """Check if two lists are close enough (for floating point comparison)"""
    if len(list1) != len(list2):
        return False
    return all(abs(a - b) < tolerance for a, b in zip(list1, list2))

# Run all tests
#test_poly_divide()

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

                    num_str = str(num)
                    N = len(num_str)

 #                   if N % 2 == 0: # The even case is really easy to handle
 #                       str_L = num_str[0:N//2]
 #                       str_R = num_str[N//2:]
 #                       if str_L == str_R:
 #                           total += int(str_L)
 #                       continue

                    for n in range(2,N):
                        k = N/n
                        
                        if k < 0: # I would be testing for code shorter then a digit
                            break
                        elif k != int(k): # I would be testing for a code that isn't a whole digit
                            continue
                        
                        k = int(k)
                        S = [int(digit) for digit in num_str]

                        # C = 1 + x^k + x^(2k) + ... + x^((n-1)k)
                        max_deg = (n - 1) * k
                        C = [1 if (max_deg - i) % k == 0 else 0 for i in range(max_deg + 1)]
                        
                        Q, R = poly_divide(S,C)

                        if R == [0]:
                            print(f"N:{N}\t n: {n}\t k: {k}\t C: {C}\t\t S: {S}\t\t Q: {Q}\t\t R: {R}")
                            total += num

except Exception as e:
    print(f"An error occurred: {e}")

print(total)