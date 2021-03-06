def heapsort(arr):
    arr_len = len(arr)

    for i in range(arr_len - 1, -1, -1):
        heapify(arr, len(arr), i)

        # Swap the top element in heap with last element in array
        arr[0], arr[i] = arr[i], arr[0]


def heapify(arr, n, i):
    """
    :param: arr - array to heapify
    n -- number of elements in the array
    i -- index of the current node
    TODO: Converts an array (in place) into a maxheap, a complete binary tree with the largest values at the top
    """
    for i in range(1, i + 1):
        # Perform heapify processing
        data_index = i
        while data_index > 0:
            parent_index = (data_index - 1) // 2
            if arr[data_index] > arr[parent_index]:
                arr[data_index], arr[parent_index] = arr[parent_index], arr[data_index]
                data_index = parent_index
            else:
                break


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.
    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    # Handle empty input list
    if len(input_list) == 0:
        return []

    # Step 1 - perform heap sort on the input list
    heapsort(input_list)

    # Step 2 - base on the sorted list, construct the 2 numbers so their sum is maximum
    number_1_list = list()
    number_2_list = list()

    input_list_len = len(input_list)
    # If the no. of digits is odd, then set the first digit of the first number as
    if input_list_len % 2 == 1:
        digit = input_list.pop()
        number_1_list.append(digit)

    # Append the digits in input list to the 2 numbers in an interleave manner
    input_list_len = len(input_list)
    for i in range(input_list_len, 0, -1):
        digit = input_list.pop()
        if i % 2 == 0:
            number_1_list.append(digit)
        else:
            number_2_list.append(digit)
    
    number_1_str = ''.join(str(n) for n in number_1_list)
    number_1 = int(number_1_str)
    
    if len(number_2_list) != 0: 
        # Convert the 2 list of digits into a string     
        number_2_str = ''.join(str(n) for n in number_2_list)
        # Convert the number string to int      
        number_2 = int(number_2_str)
        return [number_1, number_2] 

    else: 
        return [number_1] 

####################### Test ##########################################################

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])      # Pass
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])  # Pass
test_function([[1, 1, 1, 1], [11, 11]])          # Pass
test_function([[1], [1]])                        # Pass
test_function([[], []])                          # Pass