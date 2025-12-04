file_path = "day2_input.txt"

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

total = 0

try:
    with open(file_path, 'r') as file:
        for line in file:
            id_ranges = line.split(',',-1)
            id_ranges = [id.split('-',-1) for id in id_ranges]
            id_ranges = [[int(x) for x in str] for str in id_ranges]

            for id_range in id_ranges:
                print(f"Range: {id_range}")
                for num in range(id_range[0],id_range[1]+1):
                    
                    # Can't have repeated digits if only one digit
                    if num < 10:
                        continue

                    num_str = str(num)
                    N = len(num_str)

                    for n in range(2,N+1):
                        k = N/n
                        
                        if k < 0: # I would be testing for code shorter then a digit, time to test the next number
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
                            print(f"\t{num}")
                            total += num
                            break

except Exception as e:
    print(f"An error occurred: {e}")

print("-"*60)
print(f"{" "*10} TOTAL: {total}")
print("-"*60)