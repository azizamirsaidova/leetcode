"""
    Find Smallest Letter Greater Than Target
    Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.

    Note that the letters wrap around.

    For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.
    
    Input: letters = ["c","f","j"], target = "a"
    Output: "c"

"""

def nextGreatestLetter(letters, target):
    end = len(letters)-1
    start = 0

    while end <= start:
        mid = start + (end - start)//2

        if letters[mid] > target:
            end = mid - 1
        elif letters[mid] < target:
            start = mid + 1
    return letters[start]

def main():
    letters = ["c","f","j"]
    target = "a"
    print(nextGreatestLetter(letters, target))


if __name__ == "__main__":
    main()

