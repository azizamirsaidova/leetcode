"""
Given an array of positive numbers and a positive number ‘k,’ 
find the maximum sum of any contiguous subarray of size ‘k’.

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Calculate the sum of all ‘k’ sized subarrays of the given array to find the subarray with the highest sum.
"""
def max_sub_array_of_size_k(k, arr):

    """
    The above algorithm’s time complexity will be O(N∗K), where ‘N’ is the total number of elements in the given array.
    """
    max_sum = 0 
    window_sum = 0

    for i in range(len(arr)-k+1):
        window_sum = 0
        for j in range(i, i+k):
            window_sum += arr[j]
            # print("window sum", window_sum)
            # print("max sum", max_sum)
        max_sum =  max(max_sum, window_sum)
    return max_sum

def max_sub_array_of_size_k_2(k, arr):

    """ 
     Time complexity of the above algorithm will be O(N)
    """
    max_sum, window_sum = 0,0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        
        if window_end >= k-1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start] #subtract element going out
            window_start += 1 #slide the window ahead
            print(max_sum)
    return max_sum

def main():
 # print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k_2(2, [2, 3, 4, 1, 5])))


main()