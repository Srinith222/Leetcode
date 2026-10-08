def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid - 1 # Discard right half
        else:
            left = mid + 1 # Discard left half

    return -1 # Target not found