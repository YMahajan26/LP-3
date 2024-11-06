#include <iostream>
//#include <cstdlib> // For rand()
//#include <ctime>   // For seeding rand()
#include <bits/stdc++.h>

using namespace std;

// Randomized partition function with random pivot selection
int randomizedPartition(int arr[], int low, int high) {
    int pivotIndex = low + rand() % (high - low + 1); // Select random pivot
    swap(arr[pivotIndex], arr[high]); // Swap pivot with last element
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

// Randomized Quick Sort function
void randomizedQuickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = randomizedPartition(arr, low, high);
        randomizedQuickSort(arr, low, pi - 1);
        randomizedQuickSort(arr, pi + 1, high);
    }
}

// Utility function to print the array
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        cout << arr[i] << " ";
    cout << endl;
}

// Example usage
int main() {
    int arr[] = {10, 7, 8, 9, 1, 5};
    int n = sizeof(arr) / sizeof(arr[0]);

    // Seed for random pivot selection
    srand(time(0));

    cout << "Original array: ";
    printArray(arr, n);

    randomizedQuickSort(arr, 0, n - 1);

    cout << "Sorted array (Randomized Quick Sort): ";
    printArray(arr, n);

    return 0;
}

