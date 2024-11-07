import random
import time

# Partition function counts comparisons
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    comparisons = 0
    
    for j in range(low, high):
        comparisons += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1, comparisons

# Quick Sort - Deterministic (pivot is the last element)
def quick_sort(arr, low, high, is_randomized=False):
    if low < high:
        if is_randomized:
            pivot_index = random.randint(low, high)
            arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
        pi, comparisons = partition(arr, low, high)
        comparisons += quick_sort(arr, low, pi - 1, is_randomized)
        comparisons += quick_sort(arr, pi + 1, high, is_randomized)
        return comparisons
    return 0

# Fixed input array of size 15
arr = [1, 5, 2, 3, 4, 6, 11, 12, 13, 14, 15]

# Function to analyze both deterministic and randomized quicksort
def analyze_quick_sort(arr):
    # Copy of the original array for deterministic quicksort
    arr_deterministic = arr[:]
    start_time = time.perf_counter()
    comparisons_deterministic = quick_sort(arr_deterministic, 0, len(arr_deterministic) - 1)
    time_deterministic = time.perf_counter() - start_time
    
    # Copy of the original array for randomized quicksort
    arr_randomized = arr[:]
    start_time = time.perf_counter()
    comparisons_randomized = quick_sort(arr_randomized, 0, len(arr_randomized) - 1, is_randomized=True)
    time_randomized = time.perf_counter() - start_time
    
    # Output results
    print(f"Array: {arr}")
    print(f"Deterministic Quick Sort - Comparisons: {comparisons_deterministic}, Time: {time_deterministic:.6f} seconds")
    print(f"Randomized Quick Sort - Comparisons: {comparisons_randomized}, Time: {time_randomized:.6f} seconds")

# Analyze the fixed array
analyze_quick_sort(arr)

