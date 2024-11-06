import random

# Randomized Quick Sort with random pivot selection
def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Swap pivot with last element
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quick_sort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, pi - 1)
        randomized_quick_sort(arr, pi + 1, high)

# Example usage for randomized quick sort
arr = [10, 7, 8, 9, 1, 5]
print("Original array:", arr)
randomized_quick_sort(arr, 0, len(arr) - 1)
print("Sorted array (Randomized Quick Sort):", arr)
