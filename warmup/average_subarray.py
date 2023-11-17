"""
Average Of All Subarrays - Example Question
Given an array, find the average of all subarrays of ‘K’ contiguous elements in it.

Let’s understand this problem with real input:

Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
Here is the final output containing the averages of all subarrays of size '5':

Output: [2.2, 2.8, 2.4, 3.6, 2.8]

"""
nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5 #can be greater than the length of array, then return empty list 

def averageSubArrays(nums, k):
    n = len(nums)
    
    if k > n:
        return []

    windowSum = sum(nums[:k])
    averageArr = windowSum/k
    
    for i in range(n-k):
        windowSum = windowSum - nums[i]+nums[i+k]
        averageArr = windowSum/k
    return averageArr


