#include <iostream>
#include <algorithm>
using namespace std;

// Function to solve 0/1 Knapsack problem
int knapSack(int W, int wt[], int val[], int n) {
    // Base Case
    if (n == 0 || W == 0)
        return 0;

    // If weight of the nth item is more than capacity W, skip this item
    if (wt[n - 1] > W)
        return knapSack(W, wt, val, n - 1);

    // Return max of including or excluding the nth item
    else
        return max(knapSack(W, wt, val, n - 1),
                   val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1));
}

// Driver code
int main() {
    int val[] = {60, 100, 120};
    int wt[] = {10, 20, 30};
    int W = 50;
    int n = sizeof(val) / sizeof(val[0]);

    cout << "Maximum profit: " << knapSack(W, wt, val, n) << endl;
    return 0;
}