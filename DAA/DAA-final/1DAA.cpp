#include <iostream>
#include <vector>

using namespace std;

// Naive recursive approach with step counting
int fibonacci_recursive(int n, int &steps) {
    // Base cases
    if (n <= 0) {
        steps++;  // Counting steps
        return 0;
    } else if (n == 1) {
        steps++;  // Counting steps
        return 1;
    }
    steps++;  // Counting addition operation
    return fibonacci_recursive(n - 1, steps) + fibonacci_recursive(n - 2, steps);
}

// Iterative approach with step counting
pair<int, int> fibonacci_iterative(int n) {
    if (n <= 0) {
        return {0, 1};  // Base case, with one step
    } else if (n == 1) {
        return {1, 1};  // Base case, with one step
    }

    int a = 0, b = 1;
    int steps = 1;  // Counting the first addition step for n = 2

    for (int i = 2; i <= n; ++i) {
        int c = a + b;
        a = b;
        b = c;
        steps++;  // Each addition counts as a step
    }

    return {b, steps};
}

int main() {
    int n;
    cout << "Enter a number to calculate Fibonacci: ";
    cin >> n;

    // Naive recursive method
    int steps_recursive = 0;  // Counter for steps
    int fib_recursive = fibonacci_recursive(n, steps_recursive);
    cout << "Recursive approach: F(" << n << ") = " << fib_recursive 
         << ", Steps = " << steps_recursive << endl;

    // Iterative method
    pair<int, int> result = fibonacci_iterative(n);
    cout << "Iterative approach: F(" << n << ") = " << result.first 
         << ", Steps = " << result.second << endl;

    return 0;
}
