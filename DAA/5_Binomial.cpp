#include <iostream>
#include <vector>
using namespace std;

int binomialCoefficient(int n, int k) {
    // Create a 2D array to store binomial coefficients
    vector<vector<int>> C(n + 1, vector<int>(k + 1, 0));

    // Calculate binomial coefficient using dynamic programming
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= min(i, k); j++) {
            // Base cases
            if (j == 0 || j == i) {
                C[i][j] = 1;
            }
            // Calculate value using previously computed values
            else {
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
            }
        }
    }

    return C[n][k];
}

int main() {
    int n = 5, k = 2;
    cout << "Binomial Coefficient C(" << n << ", " << k << ") = " << binomialCoefficient(n, k) << endl;
    return 0;
}
