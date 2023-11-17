"""
Single Number

Given a non-empty array of integers nums, 
every element appears twice except for one. Find that single one.

As an extra challenge, can you find a solution with a linear runtime 
complexity and use only constant extra space?

Input: nums = [2,2,1, 2, 4]
Output: 1

"""

class Solution:
    def singleNumber(self, nums):
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    count += 1
            if count == 1:
                return nums[i]

    def singleNumber2(self, nums):
    # Approach 1
        
        # Time Complexity O(N^2)
        # Space Complexity O(1)
        
        for i in nums:
            if nums.count(i) == 1:
                return i
                
    def singleNumber3(self, nums):          
        # Approach 2
        
        # Time Complexity O(N)
        # Space Complexity O(1)
        # XOR cancels the effect of two same numbers for example  1 XOR 1 = 0, 0 XOR 1 = 1, 0 XOR 0 = 0
        
        ans = 0
        for i in nums:
            ans = ans^i
        
        return ans

nums = [4]
print(singleNumber(nums))




