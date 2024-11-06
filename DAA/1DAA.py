# Naive recursive approach with step counting
def fibonacci_recursive(n, steps):
    # Base cases
    if n <= 0:
        steps[0] += 1  # Counting steps
        return 0
    elif n == 1:
        steps[0] += 1  # Counting steps
        return 1
    # Recursive calculation
    steps[0] += 1  # Counting addition operation
    return fibonacci_recursive(n - 1, steps) + fibonacci_recursive(n - 2, steps)

# Iterative approach with step counting
def fibonacci_iterative(n):
    if n <= 0:
        return 0, 1  # Base case, with one step
    elif n == 1:
        return 1, 1  # Base case, with one step

    a, b = 0, 1
    steps = 1  # Counting the first addition step for n = 2

    for i in range(2, n + 1):
        a, b = b, a + b
        steps += 1  # Each addition counts as a step

    return b, steps

# Test and output results
n = int(input("Enter a number to calculate Fibonacci: "))

# Naive recursive method
steps_recursive = [0]  # Using a list to pass steps by reference
fib_recursive = fibonacci_recursive(n, steps_recursive)
print(f"Recursive approach: F({n}) = {fib_recursive}, Steps = {steps_recursive[0]}")

# Iterative method
fib_iterative, steps_iterative = fibonacci_iterative(n)
print(f"Iterative approach: F({n}) = {fib_iterative}, Steps = {steps_iterative}")
