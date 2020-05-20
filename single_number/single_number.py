'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # A Simple Solution is to use two loops. 
    # The outer loop picks elements one by one and 
    # inner loop checks if the element is present 
    # more than once or not.
    # Resource: https://www.geeksforgeeks.org/non-repeating-element/


    # picks elems 1 by 1
    # for (i = 0; i < arr.length; i++)
    for i in range(len(arr)): 
        # index 0  
        # starting point of next comparision
        j = 0        
        while(j < len(arr)):
            # checks if the elem is present more than once
            # if they're different indexes
            # in the same array AND they carry the same
            # value, stop looping
            # [0,0,2,2,4,5,5]
            if(i != j and arr[i] == arr[j]):
                break
            # Move right 
            j += 1
        # find single value here 
        if(j == len(arr)):
            return arr[i]

    return -1
        

    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")