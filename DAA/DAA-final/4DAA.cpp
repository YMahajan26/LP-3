#include <iostream>
#include <vector>
using namespace std;

// Function to solve 0/1 Knapsack problem using dynamic programming
int knapSack(int W, int wt[], int val[], int n) {
    // Create a 2D array to store the maximum profit for each subproblem
    vector<vector<int>> dp(n + 1, vector<int>(W + 1, 0));

    // Build the dp array in a bottom-up manner
    for (int i = 0; i <= n; i++) {
        for (int w = 0; w <= W; w++) {
            if (i == 0 || w == 0) {
                dp[i][w] = 0; // Base case
            } else if (wt[i - 1] <= w) {
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w]);
            } else {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }

    return dp[n][W]; // Return the maximum profit
}

// Driver code
int main() {
    int val[] = {60, 100, 120}; // Values of the items
    int wt[] = {10, 20, 30};    // Weights of the items
    int W = 40;                 // Maximum weight capacity
    int n = sizeof(val) / sizeof(val[0]); // Number of items

    cout << "Maximum profit: " << knapSack(W, wt, val, n) << endl;

    return 0;
}

