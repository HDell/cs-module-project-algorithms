'''
Input: a List of integers
Returns: a List of integers
'''

def moving_zeroes(arr):
    # Your code here
    arr
    left = 0
    right = len(arr)-1
    while left < right:
        if arr[left] == 0:
            if arr[right] == 0:
                right -= 1
            else:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        else:
            left += 1        
    return arr

"""
def moving_zeroes(arr):
    # Your code here
    new_arr = []
    zeros = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            new_arr.append(arr[i])
        else:
            zeros += 1
    for i in range(zeros):
        new_arr.append(0)
    return new_arr
"""    
if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")