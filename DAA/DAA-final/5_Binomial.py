def binomial_coefficient(n, k):
    # Create a 2D array to store binomial coefficients
    C = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    
    # Calculate binomial coefficient using dynamic programming
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            # Base cases
            if j == 0 or j == i:
                C[i][j] = 1
            # Use previously computed values
            else:
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
    
    return C[n][k]

# Example usage
n = 5
k = 7
print(f"Binomial Coefficient C({n}, {k}) = {binomial_coefficient(n, k)}")



# space optimized - 1D
def binomial_coefficient2(n, k):
    # Create a 1D array to store binomial coefficients
    C = [0] * (k + 1)
    C[0] = 1  # Base case: C(i, 0) = 1 for all i
    
    # Calculate binomial coefficient using dynamic programming
    for i in range(1, n + 1):
        # Traverse backward to prevent overwriting the values
        for j in range(min(i, k), 0, -1):
            C[j] += C[j - 1]
    
    return C[k]

# Example usage
n = 5
k = 7
print(f"Binomial Coefficient C({n}, {k}) = {binomial_coefficient2(n, k)}")
