"""
Average Of All Subarrays
Given an array, find the average of all subarrays of ‘K’ contiguous elements in it.

Let’s understand this problem with real input:

Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
Output: [2.2, 2.8, 2.4, 3.6, 2.8]

"""

def findAverage(nums, k):
    n = len(nums)
    windowSum = sum(nums[:k])
    average = windowSum/k
    result = [average]
    
    for i in range(n-k):
        windowSum = windowSum - nums[i] + nums[i+k]
        average = windowSum/k
        result.append(average)
    return result

nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
findAverage(nums, k)