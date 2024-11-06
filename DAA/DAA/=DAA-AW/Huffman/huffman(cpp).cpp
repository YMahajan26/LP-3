// #include <iostream>
// #include <queue>
// #include <vector>
// or
#include<bits/stdc++.h>
using namespace std;

// Node structure for the Huffman tree
struct Node {
    char data; // Character
    int freq;  // Frequency of the character
    Node *left; // Left child
    Node *right; // Right child
    
    Node(char d, int f) : data(d), freq(f), left(nullptr), right(nullptr) {}
};

// Function to print Huffman codes
void printCodes(Node* root, const string& code) {
    if (!root) return; // If the node is null, do nothing
    if (root->data != '$') { // If it's a leaf node
        cout << root->data << ": " << code << endl; // Print the code
    }
    // Traverse left and right subtrees
    printCodes(root->left, code + "0");
    printCodes(root->right, code + "1");
}

// Comparator for the priority queue
struct Compare {
    bool operator()(Node* a, Node* b) {
        return a->freq > b->freq; // Return true if a's frequency is greater than b's
    }
};

// Function to generate Huffman Codes
void HuffmanCode(char data[], int freq[], int size) {
    // Priority queue to store the nodes
    priority_queue<Node*, vector<Node*>, Compare> minHeap;
    
    // Create and push nodes to the min heap
    for (int i = 0; i < size; i++) {
        minHeap.push(new Node(data[i], freq[i]));
    }

    // Build the Huffman tree
    while (minHeap.size() > 1) {
        // Get the two nodes with the smallest frequency
        Node *left = minHeap.top(); minHeap.pop();
        Node *right = minHeap.top(); minHeap.pop();
        
        // Create a new internal node with these two nodes as children
        Node *internalNode = new Node('$', left->freq + right->freq);
        internalNode->left = left;
        internalNode->right = right;
        
        // Push the new node back into the min heap
        minHeap.push(internalNode);
    }

    // Print the codes using the root of the Huffman tree
    printCodes(minHeap.top(), "");
}

int main() {
    char data[] = {'A', 'B', 'C', 'D'}; // Characters
    int freq[] = {23, 12, 34, 10}; // Corresponding frequencies
    HuffmanCode(data, freq, 4); // Generate and print Huffman codes
    return 0;
}
