#include <iostream>
using namespace std;

// Function to print Fibonacci numbers using recursion
void printFibonacciRecursive(int n, int n1 = 0, int n2 = 1)
{
    if (n <= 0)
        return;                                  // Base case: if n is zero or negative, do nothing
    cout << n1 << " ";                           // Print the current Fibonacci number
    printFibonacciRecursive(n - 1, n2, n1 + n2); // Recursive call with next numbers
}

// Function to print Fibonacci numbers without recursion
void printFibonacciNonRecursive(int n)
{
    int n1 = 0, n2 = 1, n3; // Initialize first two Fibonacci numbers
    if (n >= 1)
        cout << n1 << " "; // Print first number
    if (n >= 2)
        cout << n2 << " "; // Print second number

    for (int i = 2; i < n; ++i)
    {                      // Loop from 2 to n
        n3 = n1 + n2;      // Calculate next Fibonacci number
        cout << n3 << " "; // Print the next Fibonacci number
        n1 = n2;           // Update n1 and n2
        n2 = n3;
    }
}

int main()
{
    int n;

    // Input the number of Fibonacci numbers to print
    cout << "Enter the number of Fibonacci numbers to print: ";
    cin >> n;

    // Print using recursion
    cout << "Fibonacci (Recursive): ";
    printFibonacciRecursive(n);
    cout << endl;

    // Print using non-recursion
    cout << "Fibonacci (Non-Recursive): ";
    printFibonacciNonRecursive(n);
    cout << endl;

    return 0;
}
