"""
    268. Missing Number
    Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
   
    Example 1:
    Input: nums = [3,0,1]
    Output: 2
    Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

    Example 2:
    Input: nums = [0,1]
    Output: 2

    Time & Space Complexity = O(n)
"""

def missingNumber(nums):
    return list(set(range(0,len(nums)+1)).difference(set(nums)))[0]

def missingNumber2(nums):
    return sum(range(0, len(nums)+1)) - sum(nums)

if __name__ == "__main__":
    nums = [3,0,1]
    missingNumber(nums)