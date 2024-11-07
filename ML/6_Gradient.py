import numpy as np
import matplotlib.pyplot as plt

# Define the function to minimize
def function_to_minimize(x):
    return (x+3)**2  # Example function

# Define the derivative of the function
def derivative(x):
    return 2 * (x + 3)

# # Calculate the derivative using numerical differentiation
# def derivative(x, epsilon=1e-6):
#     return (function_to_minimize(x + epsilon) - function_to_minimize(x)) / epsilon

# Gradient Descent Algorithm
def gradient_descent(starting_x, learning_rate, num_iterations, derivative_fn):
    x = starting_x
    x_values = [x]  # Track the x-values for plotting
    for i in range(num_iterations):
        gradient = derivative_fn(x)
        x = x - learning_rate * gradient
        x_values.append(x)
        print(f"Iteration {i + 1}: x = {x}, f(x) = {function_to_minimize(x)}")
    return x, x_values

# Initial parameters
initial_x = 2  # Initial starting point
learning_rate = 0.1  # Adjust this based on your function and needs
iterations = 100  # Adjust the number of iterations as needed

# Find the local minimum
minima, x_values = gradient_descent(initial_x, learning_rate, iterations, derivative)

# Plot the function and the path of gradient descent
x_range = np.linspace(-6, 6, 400)
y_range = function_to_minimize(x_range)

plt.figure(figsize=(10, 6))
plt.plot(x_range, y_range, label='(x+3)**2', color='blue')
plt.scatter(x_values, [function_to_minimize(x) for x in x_values], color='red', label='Gradient Descent Path')
plt.title('Gradient Descent to Find Local Minimum')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()

print(f"Local minimum occurs at x = {minima}, f(x) = {function_to_minimize(minima)}")

# ===Method 2=====
# To calculate the derivative of any given function programmatically without manually 
# specifying the derivative, you can use automatic differentiation libraries such as SymPy 

# !pip install sympy

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Define the function symbolically
x_sym = sp.symbols('x')
f = (x_sym + 3)**2  # Example function

# Differentiate symbolically
derivative = sp.diff(f, x_sym)

# Convert symbolic derivative to a callable function
derivative_fn = sp.lambdify(x_sym, derivative, 'numpy')

# Gradient Descent Algorithm
def gradient_descent(starting_x, learning_rate, num_iterations, derivative_fn):
    x = starting_x
    x_values = [x]
    for i in range(num_iterations):
        gradient = derivative_fn(x)
        x = x - learning_rate * gradient
        x_values.append(x)
        print(f"Iteration {i + 1}: x = {x}, f(x) = {(x+3)**2}")
    return x, x_values

# Initial parameters
initial_x = 2
learning_rate = 0.1
iterations = 100

# Find the local minimum
minima, x_values = gradient_descent(initial_x, learning_rate, iterations, derivative_fn)

# Plot the function and gradient descent path
x_range = np.linspace(-6, 6, 400)
y_range = (x_range + 3)**2

plt.figure(figsize=(10, 6))
plt.plot(x_range, y_range, label='(x+3)**2', color='blue')
plt.scatter(x_values, [(x_val + 3)**2 for x_val in x_values], color='red', label='Gradient Descent Path')
plt.title('Gradient Descent to Find Local Minimum')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()

print(f"Local minimum occurs at x = {minima}, f(x) = {(minima + 3)**2}")



