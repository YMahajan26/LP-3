# Initialize an 8x8 chessboard with all positions empty
def create_board():
    return [[0 for _ in range(8)] for _ in range(8)]

# Function to print the chessboard
def print_board(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))
    print("\n")

# Function to check if it's safe to place a queen at board[row][col]
def is_safe(board, row, col):
    # Check this column on upper rows
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, 8)):
        if board[i][j] == 1:
            return False

    return True

# Recursive function to solve the 8-queens problem using backtracking
def solve_queens(board, row):
    if row == 8:  # All queens are placed
        print_board(board)
        return True
    
    for col in range(8):
        # Check if it's safe to place queen at board[row][col]
        if is_safe(board, row, col):
            board[row][col] = 1  # Place the queen

            # Recur to place queens in the next row
            if solve_queens(board, row + 1):
                return True

            # If placing queen in board[row][col] doesn't lead to a solution
            # Remove the queen (backtrack)
            board[row][col] = 0

    return False  # No place to put a queen in this row

# Function to initialize the board with the first queen placed at a given position
def solve_with_first_queen(row, col):
    board = create_board()
    board[row][col] = 1  # Place the first queen
    print(f"Initial board with first queen at ({row}, {col}):")
    print_board(board)
    
    # Start solving from the next row
    if not solve_queens(board, row + 1):
        print("No solution found.")

# Example usage: Place the first queen at position (0, 0) and solve
solve_with_first_queen(0, 1)
