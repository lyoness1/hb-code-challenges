"""Convert a decimal number to binary representation.

For example::

    >>> dec2bin_backwards('0')
    0

    >>> dec2bin_backwards('1')
    1

    >>> dec2bin_backwards('10')
    2

    >>> dec2bin_backwards('100')
    4

    >>> dec2bin_backwards('1111')
    15

For example, using our alternate solution::

    >>> dec2bin_forwards(0)
    '0'

    >>> dec2bin_forwards(1)
    '1'

    >>> dec2bin_forwards(2)
    '10'

    >>> dec2bin_forwards(4)
    '100'

    >>> dec2bin_forwards(15)
    '1111'

"""


def dec2bin_forwards(dec):
    """Convert a decimal number to binary representation."""

    # find highest power of 2 contained in dec
    i = 0
    while i ** 2 <= dec:
        i += 1

    # extract powers of 2 from dec, appending 0 or 1 to result array
    out = []
    for bit in xrange(i - 1, -1, -1):
        if 2 ** bit <= dec:
            out.append("1")
            dec -= 2 ** bit
        else:
            out.append("0")

    # convert to string to remove leading 0's, then back to string
    return str(int("".join(out)))



def dec2bin_backwards(bin):
    """Convert a decimal number to binary representation."""

    output = 0
    for i in xrange(len(bin)):
        if bin[len(bin) - i - 1] == '1':
            output += 2 ** i

    return output









if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T!\n"
