"""
    
    Search in Rotated Sorted Array
    There is an integer array nums sorted in ascending order (with distinct values).

    Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

    Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

    You must write an algorithm with O(log n) runtime complexity.

    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1
    
    Input: nums = [1], target = 0
    Output: -1

"""

def search(nums, target):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if nums[mid] == target:
            return mid

        # split into 2 boundaries -> start -> mid - mid -> end
        # when start is less than the middle [0,1,2] -> not rotated
        if nums[start] <= nums[mid]:
            if nums[start] <= target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
        # when mid is less than the target 
            if nums[mid] < target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1 
    return -1

def main():
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(search(nums, target))

if __name__ == "__main__":
    main()