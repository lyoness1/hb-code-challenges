"""Convert a hexadecimal string, like '1A', into it's decimal equivalent.

    >>> hex_convert('6')
    6

    >>> hex_convert('10')
    16

    >>> hex_convert('FF')
    255

    >>> hex_convert('FFFF')
    65535
"""


def hex_convert(hex_in):
    """Convert a hexadecimal string, like '1A', into it's decimal equivalent."""

    # START SOLUTION

    # Dictionary to convert a hex character to equivalent decimal value

    CONVERT = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }

    # Straightforward solution: for each digit, multiply it's value
    # by 16 ** (position):

    result = 0
    for i, hex_char in enumerate(hex_in):
        hex_digit = CONVERT[hex_char]
        power = 16 ** (len(hex_in) - i - 1)
        result = result + hex_digit * power

    return result

    # Alternate solution: we can process each digit from left-to-right,
    # multiplying current value by 16 when we get to the next digit:

    # result = 0
    #
    # for hex_char in hex_in:
    #     result = result * 16 + CONVERT[hex_char]
    #
    # return result

    # END SOLUTION


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASS. YOU'RE TERRIFIC!\n"
