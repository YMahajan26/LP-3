# Class to represent an item
class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

# Comparator function to sort items by profit/weight ratio
def compare(item):
    return item.profit / item.weight

# Function to calculate the maximum value that can be obtained
def getMaxValue(items, capacity):
    # Sort items by their value-to-weight ratio in descending order
    items.sort(key=compare, reverse=True)
    
    total_value = 0.0

    for item in items:
        if capacity == 0:
            break  # No more capacity

        if item.weight <= capacity:
            # If the item can be fully picked
            capacity -= item.weight
            total_value += item.profit
        else:
            # Item can't be picked fully, pick the fraction
            total_value += item.profit * (capacity / item.weight)
            break  # Knapsack is full

    return total_value  # Return total value

# Driver code
items = [Item(60, 10), Item(100, 20), Item(120, 30)]
capacity = 50

max_value = getMaxValue(items, capacity)

# Print the result
print("Maximum value in Knapsack =", max_value)
