#!/usr/bin/python3

"""N queens solution finder module.
"""

import sys

def print_usage_and_exit(message):
    print(message)
    sys.exit(1)

def is_valid(board, row, col):
    # Check if there's a queen in the same column or on the diagonals
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(board, row, N, solutions):
    if row == N:
        # We have a valid solution; convert board state to solution format
        solution = [[r, board[r]] for r in range(N)]
        solutions.append(solution)
        return

    for col in range(N):
        if is_valid(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, N, solutions)
            board[row] = -1  # Reset the row for backtracking

def nqueens(N):
    solutions = []
    board = [-1] * N
    solve_nqueens(board, 0, N, solutions)
    
    for solution in solutions:
        print(solution)

def main():
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N")
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number")
    
    if N < 4:
        print_usage_and_exit("N must be at least 4")
    
    nqueens(N)

if __name__ == "__main__":
    main()
