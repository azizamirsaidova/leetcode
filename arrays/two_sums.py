"""
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

Two pointer approach:

"""

def twoSums(nums, target):
    nums.sort()
    left = 0
    right = len(nums)-1
    curr = 0

    while left < right:
        curr = nums[left] + nums[right]
        if curr < target:
            left += 1
        elif curr == target:
            return nums[left] + nums[right]
        else:
            right -= 1
    
    return []

nums = [2,7,11,15]
target = 9

print(twoSums(nums, target))