# The Heapify function
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child is larger than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)

# Main Heap Sort function
def heap_sort(arr):
    n = len(arr)

    # Phase 1: Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Phase 2: Extract Maximum One By One
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0] # Move current root to end
        heapify(arr, i, 0)              # Call max heapify on the reduced heap