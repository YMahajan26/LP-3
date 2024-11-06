import random
import time

# Partition function for quicksort
def partition(l, r, a):
    pivot = a[r]
    i = l - 1
    for j in range(l, r):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1

# Randomized partition function
def randomized_partition(l, r, a):
    random_index = random.randint(l, r)
    a[r], a[random_index] = a[random_index], a[r]  # Swap random pivot to the end
    return partition(l, r, a)

# QuickSort with deterministic partitioning
def quicksort(l, r, a):
    if l < r:
        pi = partition(l, r, a)
        quicksort(l, pi - 1, a)
        quicksort(pi + 1, r, a)

# Randomized QuickSort using randomized partition
def randomized_quicksort(l, r, a):
    if l < r:
        pi = randomized_partition(l, r, a)
        randomized_quicksort(l, pi - 1, a)
        randomized_quicksort(pi + 1, r, a)

if __name__ == "__main__":
    n = int(input("Enter the number of elements: "))
    arr = [random.randint(1, 1000) for _ in range(n)]
    
    # Display the unsorted array
    print("Unsorted array:", arr[:10])

    # Analyze deterministic QuickSort
    arr_copy = arr.copy()
    start_time = time.perf_counter()
    quicksort(0, n - 1, arr_copy)
    end_time = time.perf_counter()
    deterministic_time = end_time - start_time
    print(f"\nSorted array(Deterministic): {arr_copy}")
    print(f"Deterministic QuickSort took {deterministic_time:.6f} seconds")

    # Analyze randomized QuickSort
    arr_copy = arr.copy()
    start_time2 = time.perf_counter()
    randomized_quicksort(0, n - 1, arr_copy)
    end_time2 = time.perf_counter()
    randomized_time = end_time2 - start_time2
    print(f"\nSorted array(Randomized): {arr_copy}")
    print(f"Randomized QuickSort took {randomized_time:.6f} seconds\n")

    # Handling cases with very small durations
    if deterministic_time < 1e-6:
        print("Time for deterministic QuickSort was too small to measure accurately.")
    if randomized_time < 1e-6:
        print("Time for randomized QuickSort was too small to measure accurately.")
