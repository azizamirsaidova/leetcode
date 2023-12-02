"""

    Squares of a Sorted Array
    Given an integer array nums sorted in non-decreasing order, return an array of 
    the squares of each number sorted in non-decreasing order.

    Input: nums = [-4,-1,0,3,10]
    Output: [0,1,9,16,100]
    Explanation: After squaring, the array becomes [16,1,0,9,100].
    After sorting, it becomes [0,1,9,16,100].

    Input: nums = [-7,-3,2,3,11]
    Output: [4,9,9,49,121]


"""

def sortedSquares(nums):
    """
        Time Complexity 

        For loop: O(n)
        Sorting: O(nlog(n))
        Total: O(nlog(n))
    """
    for i in range(len(nums)): 
        nums[i] = nums[i] * nums[i] 
    nums.sort() 
    return nums

def sortedSquares2(nums):
    """
        Time Complexity: 0 (n)
    """

    left = 0
    right = len(nums) - 1 

    while left <= right:
        if nums[left]**2 > nums[right]**2:
            nums[left], nums[right] = nums[right], nums[left]
        nums[right] = nums[right]**2
        right -= 1
    return nums

def sortedSquares3(nums):
    """
        Time Complexity: O (n)
    """
    left = 0
    right = len(nums) - 1 
    squares = [None] * len(nums)
    highestSquareVal = len(squares) -1 

    while left <= right:
        leftSquares = nums[left] * nums[left]
        rightSquares = nums[right] * nums[right]

        if leftSquares > rightSquares:
            squares[highestSquareVal] = leftSquares
            left += 1
        else:
            squares[highestSquareVal] = rightSquares
            right -= 1 
        highestSquareVal -= 1 
    return squares

    


if __name__ == "__main__":
    nums = [-7,-3,2,3,11]
    print(sortedSquares3(nums))