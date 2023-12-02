"""
    Move Zeros

    Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

    Note that you must do this in-place without making a copy of the array.

    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]    

    Input: nums = [0]
    Output: [0]

"""

def moveZeroes(nums):
    left = 0
    right = len(nums) - 1 

    while left <= right:
        if nums[left] == 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
        left += 1
    return nums


if __name__ == "__main__":
    nums = [0,1,0,3,12]
    print(moveZeroes(nums))
