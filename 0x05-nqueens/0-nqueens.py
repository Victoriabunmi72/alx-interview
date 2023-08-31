#!/usr/bin/python3
'''
NQUEENS module
obtains solution to nqueen puzzle from input value
'''
import sys


output = []  # List of outcomes for puzzle
n = 0  # Sample size i.e. Size of chess board
pos = None  # Position on board


def get_input():
    '''
    Obtains input for function and validates

    Args: N/A

    Returns: The size of the chessboard.
    '''
    global n
    n = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def threats(pos0, pos1):
    '''
    Checks positioning of queens

    Args:
        pos0: The 1st queen's position
        pos1: The 2nd queen's position

    Returns: True if the queens are in attacking postion, else False
    '''
    if (pos0[0] == pos1[0]) or (pos0[1] == pos1[1]):
        return True
    return abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])


def output_exists(group):
    '''
    Checks if an output exists in the list of solutions

    Args:
        group: A group of possible positions

    Returns: True if it exists, otherwise False
    '''
    global output
    for stn in output:
        i = 0
        for stn_pos in stn:
            for grp_pos in group:
                if stn_pos[0] == grp_pos[0] and stn_pos[1] == grp_pos[1]:
                    i += 1
        if i == n:
            return True
    return False


def build_output(row, group):
    '''
    Builds an output for the n queens problem

    Args:
        row: The current row in the chessboard
        group: The group of valid positions
    '''
    global output
    global n
    if row == n:
        tmp0 = group.copy()
        if not output_exists(tmp0):
            output.append(tmp0)
    else:
        for col in range(n):
            a = (row * n) + col
            matches = zip(list([pos[a]]) * len(group), group)
            used_positions = map(lambda x: threats(x[0], x[1]), matches)
            group.append(pos[a].copy())
            if not any(used_positions):
                build_output(row + 1, group)
            group.pop(len(group) - 1)


def get_output():
    '''
    Gets the output for the given chessboard size
    '''
    global pos, n
    pos = list(map(lambda x: [x // n, x % n], range(n ** 2)))
    a = 0
    group = []
    build_output(a, group)


n = get_input()
get_output()
for out in output:
    print(out)
