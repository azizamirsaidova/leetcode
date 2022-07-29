
def partition(arr, low, high):
    pivot = arr[high]

    # point to greater element
    i = low-1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        # if element smaller than pivot is found
        # swap it with the greater element pointed by i
        if arr[j] <= pivot:
            i += 1

        # swapping element at i with element at j
        (arr[i], arr[j]) = (arr[j], arr[i])
        
    # swap the pivot element with the greater element specified by i
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i+1


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        # recursive call on the left of pivot
        quickSort(arr, low, pi-1)

        # recursive call on the right of pivot
        quickSort(arr, pi+1, high)


