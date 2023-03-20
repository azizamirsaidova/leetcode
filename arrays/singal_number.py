"""
Single Number

Given a non-empty array of integers nums, 
every element appears twice except for one. Find that single one.

As an extra challenge, can you find a solution with a linear runtime complexity and use only constant extra space?

Input: nums = [2,2,1]
Output: 1

"""

nums = [2, 2, 1]

def singleNumber(nums):
    res = 0
    for i in nums:
        res = i ^ res
    return res 

print(singleNumber(nums))


