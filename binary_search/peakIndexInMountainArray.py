"""
    Peak Index in a Mountain Array
    An array arr a mountain if the following properties hold:

    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
    arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
    Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

    You must solve it in O(log(arr.length)) time complexity.

    Input: arr = [0,1,0]
    Output: 1

    Input: arr = [0,2,1,0]
    Output: 1   

"""

def peakIndexInMountainArray(arr):
    start = 0
    end = len(arr) - 1 

    while start < end:
        mid = start + (end - start) // 2

        if arr[mid] < arr[mid+1]:
            start = mid + 1
        else:
            end = mid
    return start


def main():
    arr = [0,1,0]
    print(peakIndexInMountainArray(arr))


if __name__ == "__main__":
    main()