# Node structure for the Huffman tree
class Node:
    def __init__(self, data, freq):
        self.data = data       # Character
        self.freq = freq       # Frequency of the character
        self.left = None       # Left child
        self.right = None      # Right child

# Function to print Huffman codes
def printCodes(root, code=""):
    if not root:
        return
    if root.data != '$':  # If it's a leaf node
        print(f"{root.data}: {code}")  # Print the character and its code
    # Traverse left and right subtrees
    printCodes(root.left, code + "0")
    printCodes(root.right, code + "1")

# Function to generate Huffman Codes without using heapq
def HuffmanCode(data, freq):
    # Create a list of nodes
    nodes = [Node(data[i], freq[i]) for i in range(len(data))]

    # Build the Huffman tree
    while len(nodes) > 1:
        # Sort the nodes by frequency
        nodes = sorted(nodes, key=lambda x: x.freq)

        # Get the two nodes with the smallest frequency
        left = nodes.pop(0)
        right = nodes.pop(0)

        # Create a new internal node with these two nodes as children
        internal_node = Node('$', left.freq + right.freq)
        internal_node.left = left
        internal_node.right = right

        # Add the new node back to the list
        nodes.append(internal_node)

    # The root of the Huffman tree is the last remaining node
    root = nodes[0]
    printCodes(root)

# Driver code
data = ['A', 'B', 'C', 'D']  # Characters
freq = [23, 12, 34, 10]      # Corresponding frequencies
HuffmanCode(data, freq)       # Generate and print Huffman codes
