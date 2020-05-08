def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    return binary_search_rotation(input_list, number, 0, len(input_list)-1)

def binary_search_rotation(arr, num, start_index, end_index):
    if start_index > end_index:
        return -1
    
    mid_index = (start_index + end_index) // 2
    mid_value = arr[mid_index]

    if mid_value == num:
        return mid_index

    left_index = binary_search_rotation(arr, num, start_index, mid_index-1)
    right_index = binary_search_rotation(arr, num, mid_index+1, end_index)

    return max(left_index, right_index)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

######################################### Test ################################
def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6]) # Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1]) # Pass 
test_function([[6, 7, 8, 1, 2, 3, 4], 8])        # Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1])        # Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10])       # Pass

test_function([[], 0])                           # Pass
test_function([[1,2,3],-1])                      # Pass

