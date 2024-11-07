# Function to solve 0/1 Knapsack problem using dynamic programming
def knapSack(W, wt, val, n):
    # Create a 2D array to store the maximum profit for each subproblem
    dp = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build the dp array in bottom-up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif wt[i - 1] <= w:
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]

# Driver code
val = [5,4,8,6]
wt = [1,2,4,5]
W = 5
n = len(val)

print("Maximum profit:", knapSack(W, wt, val, n))
