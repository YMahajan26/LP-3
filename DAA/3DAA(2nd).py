import collections

# Define the Item tuple with profit and weight
Item = collections.namedtuple('Item', ['profit', 'weight'])

# Function to calculate the maximum profit using the Fractional Knapsack strategy
def FractionalKnapsack(arr, W):
    # Sort items by value-to-weight ratio in descending order
    arr.sort(key=lambda x: (x.profit / x.weight), reverse=True)
    
    ans = 0.0  # Total profit
    
    # Loop through the sorted items and fill the knapsack
    for i in arr:
        if i.weight <= W:
            # If the item can be fully accommodated in the knapsack
            W -= i.weight
            ans += i.profit
        else:
            # If only part of the item can be accommodated
            ans += i.profit * (W / i.weight)
            break  # No more items can be added once the knapsack is full
    
    return ans

# Main function to test the knapsack implementation
def main():
    arr = [Item(30, 5), Item(40, 10), Item(45, 15), Item(77, 22), Item(90, 25)]
    max_weight = 60  # Capacity of the knapsack
    
    # Calculate the maximum profit for the given knapsack
    result = FractionalKnapsack(arr, max_weight)
    print(f"Maximum profit in the knapsack: {result:.2f}")

# Call the main function to execute the program
main()
