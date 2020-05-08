def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # number cannot be negative
    if number < 0:
        return None
    
    # sqrt is the same as number
    if (number == 0) or (number == 1):
        return number
    
    # use binary search
    start_value = 0
    end_value = number // 2

    while start_value <= end_value:
        middle_value = (start_value + end_value) // 2
        middle_value_squared = middle_value ** 2

        if middle_value_squared == number:
            return middle_value
        
        elif middle_value_squared < number:
            start_value = middle_value + 1
            result = middle_value
        
        else:
            end_value = middle_value - 1 
    
    return result

#################################### Test #################################

print("Pass" if (3 == sqrt(9)) else "Fail")         # Pass
print("Pass" if (4 == sqrt(16)) else "Fail")        # Pass
print("Pass" if (5 == sqrt(27)) else "Fail")        # Pass
print("Pass" if (0 == sqrt(0)) else "Fail")         # Pass
print("Pass" if (1 == sqrt(1)) else "Fail")         # Pass
print("Pass" if (None == sqrt(-1)) else "Fail")     # Pass
print("Pass" if (1000 == sqrt(1000001)) else "Fail")# Pass
