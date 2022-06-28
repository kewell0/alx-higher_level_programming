#!/usr/bin/python3
import sys
"""
This module contains a program that solves the N queens problem.
The N queens problem is a puzzle that requires placing N queens on an
NxN chessboard so that no 2 queens threaten each other.
"""


# Function to check if two queens threaten each other or not
def is_safe(board, row, column):
    """Checks if two queens threaten each other or not
    Args:
        board (list): An NxN array  of '-' or 'Q'
        row (int): row number
        column (int): column number
    """

    # Return false if two queens share the same column
    for i in range(row):
        if board[i][column] == 'Q':
            return False

    # Return false if two queens share the same '/' diagonal
    (i, j) = (row, column)
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i = i - 1
        j = j - 1

    # Return false if two queens share the same '\' diagonal
    (i, j) = (row, column)
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i = i - 1
        j = j + 1

    return True


def print_sols(board):
    """Print the coordinates of placed queens in the solutions
    Args:
        board (list): NxN array of '-' and 'Q'
    """

    sols = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'Q':
                sols.append([i, j])
    print(sols)


def n_queens(board, row):
    """Find n solutions for NxN board
    Args:
        board (list): NxN array of '-' or 'Q'
        row (int): row number
    """

    # if n queens are placed successfully, print the solution
    if row == n:
        print_sols(board)
        return

    # place queen at every square in current 'row' and recur for each
    # valid movement
    for i in range(n):
        # if no two queens threaten each other
        if is_safe(board, row, i):
            # place queen in the current square
            board[row][i] = 'Q'
            # recur for the next row
            n_queens(board, row + 1)
            # backtrack and remove the queen from the current square
            board[row][i] = '-'


if __name__ == '__main__':

    # Check number of arguments and exit if more than 2
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check type of argument passed and exit if not an integer
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)

    # Check if argument is less than 4 and exit if it is
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    n = int(sys.argv[1])

    # build a board which is an nxn matrix filled with '-'
    board = [['-' for x in range(n)] for y in range(n)]

    n_queens(board, 0)
