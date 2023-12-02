"""
    Sort Colors

    Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

    We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

    You must solve this problem without using the library's sort function.

    Input: nums = [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]

    Input: nums = [2,0,1]
    Output: [0,1,2]

    0 -> red
    1 -> white
    2 -> blue 

"""

def sortColors(nums):
    low = 0
    high = len(nums) - 1 
    i = 0 

    while low <= high:
        if nums[low] == 0:
            nums[i],nums[low] = nums[low], nums[i]
            i += 1
            low += 1
        elif nums[low] == 2:
            nums[low], nums[high] = nums[high], nums[low]
            high -= 1
        else:
            low += 1
    return nums
        


if __name__ == "__main__":
    nums = [2,0,1]
    print(sortColors(nums))
