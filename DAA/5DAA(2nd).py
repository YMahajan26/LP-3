import random
import timeit
import matplotlib.pyplot as plt

# Generic Quick Sort (can be deterministic or randomized)
def quicksort(arr, low, high, is_randomized=False):
    if low < high:
        pi = partition(arr, low, high, is_randomized)
        quicksort(arr, low, pi - 1, is_randomized)
        quicksort(arr, pi + 1, high, is_randomized)

def partition(arr, low, high, is_randomized):
    if is_randomized:
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Randomized pivot
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Helper function to measure execution time
def measure_time(sort_function, arr, is_randomized=False):
    start_time = timeit.default_timer()
    sort_function(arr, 0, len(arr) - 1, is_randomized)
    return timeit.default_timer() - start_time

# Generate random data and analyze performance
def analyze_quick_sort():
    sizes = [100, 500, 1000, 5000, 10000]
    times_deterministic = []
    times_randomized = []

    for size in sizes:
        arr = [random.randint(1, 10000) for _ in range(size)]

        # Measure time for deterministic Quick Sort
        arr_copy = arr.copy()
        time_det = measure_time(quicksort, arr_copy, is_randomized=False)
        times_deterministic.append(time_det)

        # Measure time for randomized Quick Sort
        arr_copy = arr.copy()
        time_rand = measure_time(quicksort, arr_copy, is_randomized=True)
        times_randomized.append(time_rand)

        print(f"Size: {size} - Deterministic Time: {time_det:.5f}s, Randomized Time: {time_rand:.5f}s")

    # Plotting the time analysis
    plt.plot(sizes, times_deterministic, label='Deterministic Quick Sort')
    plt.plot(sizes, times_randomized, label='Randomized Quick Sort')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Quick Sort Performance: Deterministic vs Randomized')
    plt.legend()
    plt.show()

# Run the analysis
analyze_quick_sort()
