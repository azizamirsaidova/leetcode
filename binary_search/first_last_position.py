"""
    Find First and Last Position of Element in Sorted Array
    Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

    If target is not found in the array, return [-1, -1].

    You must write an algorithm with O(log n) runtime complexity.

    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]

"""

nums = [5,7,7,8,8,10]
target = 8

class Solution:
    def searchRanage(self, nums, target):
        start = self.binarySearch(nums, target, True)
        end = self.binarySearch(nums, target, False)
        return [start, end]

    def binarySearch(self, nums, target, leftBiased):
        start = 0 
        end = len(nums) - 1 
        i = -1

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                i = mid

                if leftBiased:
                    end = mid - 1
                else:
                    start = mid + 1
        return i

def main():
    nums = [5,7,7,8,8,10]
    target = 8

    Solution.searchRanage(nums, target)

if __name__ == "__main__":
    main()

