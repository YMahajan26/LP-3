# Deterministic Quick Sort with last element as pivot
def deterministic_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def deterministic_quick_sort(arr, low, high):
    if low < high:
        pi = deterministic_partition(arr, low, high)
        deterministic_quick_sort(arr, low, pi - 1)
        deterministic_quick_sort(arr, pi + 1, high)

# Example usage for deterministic quick sort
arr = [10, 7, 8, 9, 1, 5]
print("Original array:", arr)
deterministic_quick_sort(arr, 0, len(arr) - 1)
print("Sorted array (Deterministic Quick Sort):", arr)
