"""
Time complexity: O(N)
Space complexity: O(1)

"""
def remove_duplicates(arr):

    next_non_duplicate = 1
    i = 0
    while i < len(arr):
        if arr[next_non_duplicate - 1] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1
        i += 1
    return next_non_duplicate

def main():
    print("After removing duplicates:", remove_duplicates([2, 3, 3, 3, 6, 9, 9]))

main()