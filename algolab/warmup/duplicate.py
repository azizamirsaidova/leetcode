"""
Contains Duplicate
Given an integer array nums, return true if any value appears at least 
twice in the array, and return false if every element is distinct.

Input: nums = [1,2,3,1]
Output: true

"""
def containsDuplicate(nums):
    for i in nums:
        if nums.count(i) == 2:
            return True
        else:
            return False

nums = [1,2,3,1]
for i in range(len(nums)):
    print(nums[i], nums[i-1])
