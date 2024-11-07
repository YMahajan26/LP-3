// #include <iostream>
// #include <vector>
// #include <cmath>
#include<bits/stdc++.h>
using namespace std;

bool isSafe(int row, int col, vector<int>& board) {
    // Check for queens in the same column
    for (int i = 0; i < row; ++i) {
        if (board[i] == col || abs(i - row) == abs(board[i] - col)) {
            return false;
        }
    }
    return true;
}

void printBoard(vector<int>& board) {
    int n = board.size();
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (board[i] == j) {
                cout << "Q ";
            } else {
                cout << "_ ";
            }
        }
        cout << endl;
    }
    cout << endl;
}

void solveNQueensBacktracking(int row, vector<int>& board, int& count) {
    int n = board.size();
    if (row == n) {
        count++;
        cout << "Solution " << count << ":\n";
        printBoard(board);
        return;
    }
    for (int col = 0; col < n; ++col) {
        if (isSafe(row, col, board)) {
            board[row] = col;
            solveNQueensBacktracking(row + 1, board, count);
            board[row] = -1;
        }
    }
}

bool promising(int row, int col, vector<int>& board) {
    // ckecks if it is safe to place a queen at a given position(row,col) on a chessboard
    int n = board.size();
    for (int i = 0; i < row; ++i) {
        if (board[i] == col || abs(i - row) == abs(board[i] - col)) {
            return false;
        }
    }
    return true;
}

int main() {
    int n;
    cout << "Enter the number of queens: ";
    cin >> n;

    vector<int> board(n, -1); // Initialize board with -1 (no queen placed)
    int count = 0;

    cout << "\nBacktracking Solutions:\n";
    solveNQueensBacktracking(0, board, count);
    if (count == 0) {
        cout << "No solutions found using backtracking.\n";
    }
    return 0;
}