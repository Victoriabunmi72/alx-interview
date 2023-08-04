#!/usr/bin/python3
"""
    Function to determine if all Boxes can be unlocked
"""


def canUnlockAll(boxes):
    """
    Using boolean value to test boxes in list
    Function uses 2 iterations, 1 to transverse the list
    2 to compare if key is index or not in order to open boxes
    """
    if type(boxes) is not list:
        return False
    elif (len(boxes)) == 0:
        return False
    for k in range(1, len(boxes) - 1):
        box_check = False
        for index in range(len(boxes)):
            box_check = k in boxes[index] and k != index
            if box_check:
                break
        if box_check is False:
            return box_check
    return True
