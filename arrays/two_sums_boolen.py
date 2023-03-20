"""

Given an array of integers nums and an integer target, 
return true if integers add up to target.

Two pointer approach: O N log n

Sorted: Two pointers O(N)
Not sorted: Hash map O(N)

"""
nums = [6, 4, 7, 6]  
nums_map = {6:0, 4:1, 7:2, 6:3}

target = 13

def twoSums(nums, target):
    nums.sort()
    left = 0
    right = len(nums) - 1 
    curr = 0

    while left < right:
        curr = nums[left] + nums[right]
         
        if curr == target:
            return True
        elif curr < target:
            left += 1
        else:
            right -= 1
    return False
        
def twoSumsMap(nums, target):
    nums_map = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in nums_map:
            return True

        nums_map[nums[i]] = i
    return False

nums = [6, 4, 7, 5, 3, 2, 1]  
# nums_map = {6:0, 4:1, 7:2, 6:3}
target = 13
print(twoSumsMap(nums, target))

