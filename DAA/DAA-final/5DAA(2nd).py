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

# Generate a random array of integers
def generate_random_array(size, max_value=1000):
    return [random.randint(1, max_value) for _ in range(size)]

# Analyze both deterministic and randomized quicksort
def analyze_quick_sort(size):
    arr = generate_random_array(size)
    
    # Deterministic Quick Sort
    arr_copy = arr[:]
    start_time = time.time()
    comparisons_deterministic = quick_sort(arr_copy, 0, len(arr_copy) - 1)
    time_deterministic = time.time() - start_time
    
    # Randomized Quick Sort
    arr_copy = arr[:]
    start_time = time.time()
    comparisons_randomized = quick_sort(arr_copy, 0, len(arr_copy) - 1, is_randomized=True)
    time_randomized = time.time() - start_time
    
    # Output results
    print(f"Array Size: {size}")
    print(f"Deterministic Quick Sort - Comparisons: {comparisons_deterministic}, Time: {time_deterministic:.6f} seconds")
    print(f"Randomized Quick Sort - Comparisons: {comparisons_randomized}, Time: {time_randomized:.6f} seconds")

# Main function to test for different array sizes
if __name__ == "__main__":
    for size in [100, 500, 1000, 5000, 10000]:
        analyze_quick_sort(size)

