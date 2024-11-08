#!/usr/bin/python3

"""N queens solution finder module."""

import sys

def get_input():
    """Retrieves and validates this program's argument.

    Returns:
        int: The size of the chessboard.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n

def is_safe(board, row, col, n):
    """Checks if a queen can be placed at board[row][col].

    Args:
        board (list of int): Current state of the board.
        row (int): Row to place the queen.
        col (int): Column to place the queen.
        n (int): Size of the chessboard.

    Returns:
        bool: True if safe, False otherwise.
    """
    for i in range(row):
        # Check the same column and both diagonals
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(n):
    """Solves the N queens problem and prints all solutions.

    Args:
        n (int): Size of the chessboard.
    """
    def backtrack(row, board):
        if row == n:
            solutions.append([[i, board[i]] for i in range(n)])
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                backtrack(row + 1, board)
                board[row] = -1  # Reset for backtracking

    solutions = []
    board = [-1] * n
    backtrack(0, board)
    
    for solution in solutions:
        print(solution)

# Main Execution
if __name__ == "__main__":
    n = get_input()
    solve_nqueens(n)
