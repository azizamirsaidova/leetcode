"""
Given an array of integers nums which is sorted in ascending order, and 
an integer target, write a function to search target in nums. If target exists, 
then return its index. Otherwise, return -1.

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
"""

def search(nums, target):
    start = 0 
    end = len(nums) - 1 
    
    while start <= end:
        mid = start + (end - start) // 2
        
        if nums[mid] == target:
            return mid
        
        if nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

nums = [-1,0,3,5,9,12]
target = 9
search(nums, target)