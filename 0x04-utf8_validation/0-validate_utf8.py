#!/usr/bin/python3
"""
UTF-8 validation checker
"""


def validUTF8(data):
    """
    Checks if list of integers are UTF-8 valid

    Args:
        data: List of integers

    Return: True if valid, false otherwise
    """
    count = 0
    n = len(data)
    for i in range(n):
        if count > 0:
            count -= 1
            continue
        if type(data[i]) is not int or data[i] < 0 or data[i] > 0x10ffff:
            return False
        elif data[i] <= 0x7f:
            count = 0
        elif data[i] & 0b11111000 == 0b11110000:
            # 4-byte
            byte = 4
            if n - i >= byte:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + byte],
                ))
                if not all(next_body):
                    return False
                count = byte - 1
            else:
                return False
        elif data[i] & 0b11110000 == 0b11100000:
            # 3-byte
            byte = 3
            if n - i >= byte:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + byte],
                ))
                if not all(next_body):
                    return False
                count = byte - 1
            else:
                return False
        elif data[i] & 0b11100000 == 0b11000000:
            # 2-byte
            byte = 2
            if n - i >= byte:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + byte],
                ))
                if not all(next_body):
                    return False
                count = byte - 1
            else:
                return False
        else:
            return False
    return True
