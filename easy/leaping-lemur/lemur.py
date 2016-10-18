"""Leaping lemur.

Calculate the fewest number of jumps the lemur needs to
jump to the last tree. The lemur can jump 1 or 2 branches.
It cannot use deadly branch (1 in the list).

    >>> lemur([0])
    0

    >>> lemur([0, 0])
    1

    >>> lemur([0, 0, 0])
    1

    >>> lemur([0, 1, 0])
    1

    >>> lemur([0, 0, 1, 0])
    2

    >>> lemur([0, 0, 0, 0, 1, 0, 0, 1, 0])
    5
"""


def  lemur(branches):
    """Return number of jumps needed."""

    assert branches[0] == 0, "First branch must be alive"
    assert branches[-1] == 0, "Last branch must be alive"

    if len(branches) == 1:
        return 0

    if len(branches) <= 3:
        return 1

    min_jumps_to_location = [0 if x == 0 else float('inf') for x in branches]
    if min_jumps_to_location[1] == 0:
        min_jumps_to_location[1] = 1

    for i in xrange(2, len(branches)):
        if branches[i] == 0:
            min_jumps_to_location[i] = 1 + min(min_jumps_to_location[i-2],
                                               min_jumps_to_location[i-1])

    return min_jumps_to_location[-1]







if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NICE JUMPING!\n"