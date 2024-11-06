#include <iostream>
#include <vector>
#include <cstdlib>  // For rand()
#include <chrono>   // For time measurement

using namespace std;

// Standard partition function
int partition(vector<int>& arr, int l, int r) {
    int pivot = arr[r];
    int i = l - 1;
    for (int j = l; j < r; j++) {
        if (arr[j] <= pivot) {
            swap(arr[++i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[r]);
    return i + 1;
}

// Randomized partition function
int randomizedPartition(vector<int>& arr, int l, int r) {
    int randomIndex = l + rand() % (r - l + 1);
    swap(arr[r], arr[randomIndex]);
    return partition(arr, l, r);
}

// Deterministic QuickSort
void quicksort(vector<int>& arr, int l, int r) {
    if (l < r) {
        int pi = partition(arr, l, r);
        quicksort(arr, l, pi - 1);
        quicksort(arr, pi + 1, r);
    }
}

// Randomized QuickSort
void randomizedQuicksort(vector<int>& arr, int l, int r) {
    if (l < r) {
        int pi = randomizedPartition(arr, l, r);
        randomizedQuicksort(arr, l, pi - 1);
        randomizedQuicksort(arr, pi + 1, r);
    }
}

int main() {
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;

    // Generate random array
    vector<int> arr(n);
    for (int &num : arr) {
        num = rand() % 1000 + 1;
    }

    cout << "\nUnSorted array: ";
    for (int i = 0; i < min(n, 10); i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    // Measure Deterministic QuickSort
    auto arrCopy = arr;
    auto start = chrono::high_resolution_clock::now();
    quicksort(arrCopy, 0, n - 1);
    auto end = chrono::high_resolution_clock::now();
    auto deterministicTime = chrono::duration<double>(end - start).count();
    cout << "\nSorted array (Deterministic QuickSort): ";
    for (int i = 0; i < min(n, 10); i++) {
        cout << arrCopy[i] << " ";
    }
    cout << "\nDeterministic QuickSort took " << deterministicTime << " seconds\n";

    // Measure Randomized QuickSort
    arrCopy = arr;
    start = chrono::high_resolution_clock::now();
    randomizedQuicksort(arrCopy, 0, n - 1);
    end = chrono::high_resolution_clock::now();
    auto randomizedTime = chrono::duration<double>(end - start).count();
    cout << "\nSorted array (Randomized QuickSort): ";
    for (int i = 0; i < min(n, 10); i++) {
        cout << arrCopy[i] << " ";
    }
    cout << "\nRandomized QuickSort took " << randomizedTime << " seconds\n";

    return 0;
}
