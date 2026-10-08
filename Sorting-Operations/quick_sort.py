# The Partition Function
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1 # Boundary for smaller elements

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Lock the pivot into its final position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1 # Return the pivot's permanent index

# The Recursive Quick Sort Function
def quick_sort(arr, low, high):
    if low >= high: return # Base case

    # Lock one element and get its index
    pivot_index = partition(arr, low, high)

    # Recursively sort the left and right messy sides
    quick_sort(arr, low, pivot_index - 1)
    quick_sort(arr, pivot_index + 1, high)