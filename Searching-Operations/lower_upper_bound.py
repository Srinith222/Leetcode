def lower_bound(arr, target):
    left, right = 0, len(arr) - 1
    answer = len(arr)

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] >= target:
            answer = mid     # Store candidate
            right = mid - 1  # Keep looking left
        else:
            left = mid + 1

    return answer

def upper_bound(arr, target):
    left, right = 0, len(arr) - 1
    answer = len(arr)

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] > target:
            answer = mid     # Store candidate
            right = mid - 1  # Keep looking left
        else:
            left = mid + 1

    return answer