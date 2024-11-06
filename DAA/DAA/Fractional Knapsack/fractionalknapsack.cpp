#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Class to represent an item
class Item {
public:
    int profit;
    int weight;
    Item(int p, int w) : profit(p), weight(w) {}
};

// Comparator function to sort items by profit/weight ratio
bool compare(Item& a, Item& b) {
    double r1 = (double)a.profit / a.weight;
    double r2 = (double)b.profit / b.weight;
    return r1 > r2; // Sort in descending order
}

// Function to calculate the maximum value that can be obtained
double getMaxValue(vector<Item>& items, int capacity) {
    // Sort items by their value-to-weight ratio
    sort(items.begin(), items.end(), compare);
    
    double totalValue = 0.0;

    for (auto& item : items) {
        if (capacity == 0) break; // No more capacity

        if (item.weight <= capacity) {
            // If the item can be fully picked
            capacity -= item.weight;
            totalValue += item.profit;
        } else {
            // Item can't be picked fully, pick the fraction
            totalValue += item.profit * ((double)capacity / item.weight);
            break; // Knapsack is full
        }
    }

    return totalValue; // Return total value
}

int main() {
    vector<Item> items = { Item(30, 5), Item(40, 10), Item(45, 15), Item(77, 22), Item(90, 25) };
    int capacity = 60;
    
    double maxValue = getMaxValue(items, capacity);
    
    // Print the result
    cout << "Maximum value in Knapsack = " << maxValue << endl;
    return 0;
}
