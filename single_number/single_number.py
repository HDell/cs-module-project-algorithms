'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    dupes = []
    for i in range(0, len(arr)-1):
        sentinel = False
        for j in range (i+1, len(arr)):
            if arr[i] == arr[j]:
                dupes.append(arr[i])     
    for i in range(0, len(arr)):
        sentinel = False
        for j in range(0, len(dupes)):
            if arr[i] == dupes[j]:
                sentinel = True
        if sentinel == False:
            return arr[i]

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 8, 5, 5, 3, 8, 0, 1, 3, 0, 4]

    print(f"The odd-number-out is {single_number(arr)}")