""" 
    Find in Mountain Array
    (This problem is an interactive problem.)

    You may recall that an array arr is a mountain array if and only if:

    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
    arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
    Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.

    You cannot access the mountain array directly. You may only access the array using a MountainArray interface:

    MountainArray.get(k) returns the element of the array at index k (0-indexed).
    MountainArray.length() returns the length of the array.
    Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

    Input: array = [1,2,3,4,5,3,1], target = 3
    Output: 2
    Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.

"""

def findInMountainArray(target, mountain_arr):
    start = 0
    end = mountain_arr.length() - 1
    
    # get the peakIndex
    while start < end:
        mid = start + (end - start) // 2
        midVal, midRightVal = mountain_arr.get(mid), mountain_arr.get(mid+1)
        
        if midVal < midRightVal:
            start = mid + 1
        else:
            end = mid 
    peakIndex = start 
    
    # check the left side
    start = 0 
    end = peakIndex
    while start <= end:
        mid = start + (end - start) // 2
        
        if mountain_arr.get(mid) == target:
            return mid
        elif mountain_arr.get(mid) < target:
            start = mid + 1
        else:
            end = mid - 1
            
    # check the right
    start = peakIndex
    end = mountain_arr.length() - 1
    while start <= end:
        mid = start + (end - start) // 2
        
        if mountain_arr.get(mid) == target:
            return mid
        elif mountain_arr.get(mid) < target:
            end = mid - 1
        else:
            start = mid + 1
    return - 1
            
            
        


def main(): 
    mountain_arr = [1,2,3,4,5,3,1]
    target = 3
    print(findInMountainArray(target, mountain_arr))


if __name__ == "__main__":
    main()

