#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

// Partition function to count comparisons
int partition(std::vector<int>& arr, int low, int high, int& comparisons) {
    int pivot = arr[high];  // pivot is chosen to be the last element
    int i = low - 1;

    for (int j = low; j < high; ++j) {
        comparisons++;
        if (arr[j] <= pivot) {
            i++;
            std::swap(arr[i], arr[j]);
        }
    }

    // Place the pivot in the correct position
    std::swap(arr[i + 1], arr[high]);
    return i + 1;
}

// Quick Sort - Deterministic (pivot is the last element)
int quickSort(std::vector<int>& arr, int low, int high, bool isRandomized, int& comparisons) {
    if (low < high) {
        if (isRandomized) {
            // Randomize pivot
            int pivotIndex = rand() % (high - low + 1) + low;
            std::swap(arr[high], arr[pivotIndex]);
        }
        
        int pi = partition(arr, low, high, comparisons);
        
        quickSort(arr, low, pi - 1, isRandomized, comparisons);
        quickSort(arr, pi + 1, high, isRandomized, comparisons);
    }
    return 0;
}

// Function to analyze both deterministic and randomized quicksort
void analyzeQuickSort(std::vector<int>& arr) {
    // Copy the original array for deterministic quicksort
    std::vector<int> arr_deterministic = arr;
    int comparisons_deterministic = 0;
    clock_t start_time = clock();
    quickSort(arr_deterministic, 0, arr_deterministic.size() - 1, false, comparisons_deterministic);
    double time_deterministic = (double)(clock() - start_time) / CLOCKS_PER_SEC;

    // Copy the original array for randomized quicksort
    std::vector<int> arr_randomized = arr;
    int comparisons_randomized = 0;
    start_time = clock();
    quickSort(arr_randomized, 0, arr_randomized.size() - 1, true, comparisons_randomized);
    double time_randomized = (double)(clock() - start_time) / CLOCKS_PER_SEC;

    // Output results
    std::cout << "Array: ";
    for (int num : arr) {
        std::cout << num << " ";
    }
    std::cout << "\n";

    std::cout << "Deterministic Quick Sort - Comparisons: " << comparisons_deterministic
              << ", Time: " << time_deterministic << " seconds\n";

    std::cout << "Randomized Quick Sort - Comparisons: " << comparisons_randomized
              << ", Time: " << time_randomized << " seconds\n";
}

int main() {
    // Fixed input array of size 15
    std::vector<int> arr = {1, 5, 2, 3, 4, 6, 11, 12, 13, 14, 15};

    // Analyze the fixed array
    analyzeQuickSort(arr);

    return 0;
}
