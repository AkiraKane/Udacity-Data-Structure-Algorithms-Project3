Firstly, heap sort was used to sort the digit array

Afterwards, traverse the sorted list and construct the 2 numbers respectively:

Firstly, check whether the number of elements is odd. If yes, then take the last element (which is the largest digit) as the first digit of the first number. Remove the element.
Then we traverse the array from last element to the beginning. Which should be in the order of largest digit to smallest digit.
For each element, we alternatively append the digit to first and second number respectively. This way will cause the max possible digit to the most significant digit of each number.
The sum of the result 2 numbers should be the largest possible value.

Time and Space complexity:

The run time complexity is the same as the Heap Sort algorithm, which is of O(nlog(n)) and the overall space complexity is of O(n).