#!/usr/bin/python3

import sys

def solve(row, column):
    '''
    Solves the N-Queens problem recursively.

    Args:
        row: The current row being considered.
        column: The total number of columns (and queens).

    Returns:
        A list of solutions for placing queens on the chessboard.
    '''
    solver = [[]]
    for q in range(row):
        solver = place_queen(q, column, solver)
    return solver

def place_queen(q, column, prev_solver):
    '''
    Places a queen in a safe position on the chessboard.

    Args:
        q: The current row being considered.
        column: The total number of columns (and queens).
        prev_solver: The list of previous solutions.

    Returns:
        A list of solutions after placing a queen in a safe position.
    '''
    solver_queen = []
    for array in prev_solver:
        for x in range(column):
            if is_safe(q, x, array):
                solver_queen.append(array + [x])
    return solver_queen

def is_safe(q, x, array):
    '''
    Checks if it's safe to place a queen at a certain position.

    Args:
        q: The row being considered.
        x: The column being considered.
        array: The array representing the current board configuration.

    Returns:
        True if it's safe to place a queen, False otherwise.
    '''
    if x in array:
        return False
    else:
        return all(abs(array[column] - x) != q - column
                   for column in range(q))

def init():
    '''
    Initializes the N-Queens problem by obtaining and validating input.

    Returns:
        The number of queens (chessboard size).
    '''
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        the_queen = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if the_queen < 4:
        print("N must be at least 4")
        sys.exit(1)
    return the_queen

def n_queens():
    '''
    Main function to solve and print N-Queens solutions.
    '''
    the_queen = init()
    solver = solve(the_queen, the_queen)
    for array in solver:
        clean = []
        for q, x in enumerate(array):
            clean.append([q, x])
        print(clean)

if __name__ == '__main__':
    n_queens()
