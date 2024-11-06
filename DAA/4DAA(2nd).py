def knapsack_memoization(values, weights, capacity):
    n = len(values)
    # Initialize memo table with -1 to indicate uncomputed results
    memo = [[-1] * (capacity + 1) for _ in range(n)]
    
    def recursive_knapsack(i, w):
        # Base condition
        if i < 0 or w <= 0:
            return 0
        # Return the result if it’s already computed
        if memo[i][w] != -1:
            return memo[i][w]
        # If the weight of the current item is more than the remaining capacity, skip this item
        if weights[i] > w:
            memo[i][w] = recursive_knapsack(i - 1, w)
        else:
            # Include or exclude the current item
            include = values[i] + recursive_knapsack(i - 1, w - weights[i])
            exclude = recursive_knapsack(i - 1, w)
            memo[i][w] = max(include, exclude)
        return memo[i][w]
    
    # Start recursion with the last item and full capacity
    return recursive_knapsack(n - 1, capacity)

def knapsack_tabulation(values, weights, capacity):
    n = len(values)
    # Initialize DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                # Include or exclude the item
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                # Exclude the item
                dp[i][w] = dp[i - 1][w]
    
    # The answer is the maximum value at dp[n][capacity]
    return dp[n][capacity]

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 40

# Using memoization approach
max_value_memoization = knapsack_memoization(values, weights, capacity)
print(f"Maximum value (Memoization): {max_value_memoization}")

# Using tabulation approach
max_value_tabulation = knapsack_tabulation(values, weights, capacity)
print(f"Maximum value (Tabulation): {max_value_tabulation}")