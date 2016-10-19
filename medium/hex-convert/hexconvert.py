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

    conversions = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
                   '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                   '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}

    dec = 0
    for i in xrange(len(hex_in)):
        hex_digit = hex_in[len(hex_in) - i - 1]
        dec += conversions[hex_digit] * (16 ** i)

    return dec







if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASS. YOU'RE TERRIFIC!\n"
