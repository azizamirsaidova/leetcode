"""
Maximum Sum Subarray of Size K (easy)

Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Time complexity: O(N*K), where 'N' is the total number of elements in the given array


"""

arr = [2, 1, 5, 1, 3, 2]
k = 3

def max_sub_array_of_size_k(k, arr):
    max_sum = 0
    window_sum = 0
    for i in range(len(arr)-k+1):
        window_sum = 0
        for j in range(i, i+k):
            #print("Window: ", window_sum)
            window_sum += arr[j]
        # print("After incrementing: ", window_sum)
        max_sum = max(max_sum, window_sum)
    return max_sum

"""
1. Subtract the element going out of the sliding window, i.e., subtract the first element of the window.
2. Add the new element getting included in the sliding window, i.e., the element coming right after the end of the window.
This approach will save us from re-calculating the sum of the overlapping part of the sliding window. Here is what our algorithm will look like:
Time complexity: 0(n)
"""      
def max_sub_array_of_size_k_2(k, arr):
    max_sum = 0
    window_sum = 0
    window_start = 0
    
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= k-1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]  # subtract the element going out
            window_start += 1  # slide the window ahead
    return max_sum

print(max_sub_array_of_size_k_2(k, arr))