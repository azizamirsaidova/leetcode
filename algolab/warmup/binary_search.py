"""
Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

"""
def searchRange1(self, nums, target):
        res = []
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
            
            if target not in nums:
                return [-1,-1]
        return res
