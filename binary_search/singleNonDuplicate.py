"""
    Single Element in a Sorted Array
    You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

    Return the single element that appears only once.

    Your solution must run in O(log n) time and O(1) space.

    Input: nums = [1,1,2,3,3,4,4,8,8]
    Output: 2

    Input: nums = [3,3,7,7,10,11,11]
    Output: 10

"""

def singleNonDuplicate(nums):
    numsMap = {}
    for i in range(len(nums)):
        numsMap[nums[i]] = numsMap.get(nums[i], 0)+1

    for i in range(len(nums)):
        if numsMap[nums[i]] == 1:
            return nums[i]

def singleNonDuplicate2(nums):
    start = 0
    end = len(nums) - 1

    while start < end:
        mid = start + (end - start) // 2
        
        # check the right side whether its even
        if nums[mid] == nums[mid+1]:
            if (mid - start) % 2 == 0:
                start = mid + 2
            else:
                end = mid - 1

        # check the left side whether its even
        elif nums[mid] == nums[mid-1]:
            if (end - mid) % 2 == 0:
                end = mid - 2
            else:
                start = mid + 1
        else:
            return nums[mid]
    return nums[start]



def main():
    nums = [1,1,2,3,3,4,4,8,8]
    print(singleNonDuplicate(nums))
    print(singleNonDuplicate2(nums))
    
if __name__ == "__main__":
    main()