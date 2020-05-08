def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None, None

    max_val = None
    min_val = None

    for i, int in enumerate(ints):
        if i == 0:
            max_val, min_val = int, int 

        if int > max_val:
            max_val = int
            
        elif int < min_val:
            min_val = int
        
    return min_val, max_val

############################################ Test ###################################

##Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")        # Pass

## Test case for None
print ("Pass" if ((None, None) == get_min_max([])) else "Fail") # Pass

# Test case for single number
print ("Pass" if ((1, 1) == get_min_max([1])) else "Fail")      # Pass

# Test case for same number
print ("Pass" if ((1, 1) == get_min_max([1, 1])) else "Fail")   # Pass

