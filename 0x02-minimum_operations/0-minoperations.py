#!/usr/bin/python3
'''
Calculated minimum number of operations required
'''


def minOperations(n):
    '''
    Calculates the fewest number of operations required to achieve n
    H characters

    Args:
        n: Number of H characters

    Return: Fewest number of operations
    '''
    if not isinstance(n, int):
        return 0
    operations = 0  # Tracks number of operations
    clipboard = 0   # Stores current number of characters
    characters = 1  # Initial character H

    while characters < n:
        if clipboard == 0:
            # first copy_all and paste
            clipboard = characters
            characters += clipboard
            operations += 2

        elif n - characters > 0 and (n - characters) % characters == 0:
            # copy all and paste
            clipboard = characters
            characters += clipboard
            operations += 2

        elif clipboard > 0:
            # paste
            characters += clipboard
            operations += 1

    return operationsi
