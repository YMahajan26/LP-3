import timeit
import matplotlib.pyplot as plt

# Naive recursive approach
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Iterative approach
def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def measure_time(func, *args):
    return timeit.timeit(lambda: func(*args), number=1000)

def plot_fibonacci_time_complexities(max_n):
    n_values = list(range(2, max_n + 1))
    times_iterative = []
    times_recursive = []

    for n in n_values:
        time_iterative = measure_time(fibonacci_iterative, n)
        time_recursive = measure_time(fibonacci_recursive, n)

        times_iterative.append(time_iterative)
        times_recursive.append(time_recursive)

    plt.plot(n_values, times_iterative, label='Iterative')
    plt.plot(n_values, times_recursive, label='Recursive')

    plt.xlabel('n (Fibonacci value)')
    plt.ylabel('Execution time (seconds)')
    plt.title('Comparison of Fibonacci Algorithms')
    plt.legend()
    plt.yscale('log')  # Use log scale for better visibility
    plt.show()

max_n = 25  # Limit to 30 due to the exponential nature of the recursive algorithm
plot_fibonacci_time_complexities(max_n)
