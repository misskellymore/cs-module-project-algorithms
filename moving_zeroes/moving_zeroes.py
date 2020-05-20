'''
Input: a List of integers
Returns: a List of integers
'''

# # Moving Zeroes

# Write a function that takes an array of integers and 
# moves each non-zero integer to the left side of the 
# array, then returns the altered array. The order of 
# the non-zero integers does not matter in the mutated array.

# ## Examples
# ```
# Sample input: [0, 3, 1, 0, -2]
# Expected output: 3
# Expected output array state: [3, 1, -2, 0, 0]

def moving_zeroes(arr):
    # Your code here
    # starting count of of non 0 elems
    count = 0
    n = len(arr)

    for i in range(n):
        if arr[i] != 0:

            arr[count] = arr[i]
            count+=1

    while count < n:
        arr[count] = 0
        count+=1

    return arr


           

        
        
 

    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")