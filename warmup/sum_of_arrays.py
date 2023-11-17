"""
Sum Of All Subarrays - Example Question
Given an array, find the sum of all subarrays of ‘K’ contiguous elements in it.

Let’s understand this problem with real input:

Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
Here is the final output containing the averages of all subarrays of size '5':

Output: [2.2, 2.8, 2.4, 3.6, 2.8]

"""

def sumOfArrays(nums, k):
    n = len(nums)
    windowSum = sum(nums[:k])
    maximumSum = windowSum

    for i in range(n-k):
        windowSum = windowSum - nums[i]+nums[i+k]
        maximumSum = max(maximumSum,windowSum)
    return maximumSum

nums = [2,1,5,1,3,2]
k = 5