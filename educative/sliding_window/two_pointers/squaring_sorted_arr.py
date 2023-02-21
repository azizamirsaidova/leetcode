"""
Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]

"""

def sorted_arrs(arr):
    squares = []
    total = 0
    
    left = 0
    right = len(arr)-1
    for i in range(len(arr)):
        total = arr[i]**2

        #if total[i] > total[i]+1
        squares.append(total)

        print(total[i])
        print(total[i+1])
    return squares

def make_squares(arr):
    n = len(arr)
    squares = [0 for x in range(n)]
    highestSquareIdx = n - 1
    left, right = 0, n - 1
    while left <= right:
        leftSquare = arr[left] * arr[left]
        rightSquare = arr[right] * arr[right]
        if leftSquare > rightSquare:
            squares[highestSquareIdx] = leftSquare
            left += 1
        else:
            squares[highestSquareIdx] = rightSquare
            right -= 1
        highestSquareIdx -= 1

    return squares

def main():
   # print("Squared arr is, ", sorted_arrs([-2, -1, 0, 2, 3]))
    print("Squared arr is, ", str(make_squares([-2, -1, 0, 2, 3])))

main()