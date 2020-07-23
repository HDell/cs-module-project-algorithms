'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    window = [None]*k
    sub = []
    start = 0
    end = k
    max = None
    while window != nums[len(nums)-k:]:
        window = nums[start:end]
        max = window[0]
        for i in range(1, len(window)):
            if window[i] > max:
                max = window[i]
        sub.append(max)
        start += 1
        end += 1
    return sub

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
