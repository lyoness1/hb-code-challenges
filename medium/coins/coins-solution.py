"""Calculate possible change from combinations of dimes and pennies.

Given an infinite supply of dimes and pennies, find the different
amounts of change can be created with exact `num_coins` coins?

For example, when num_coins = 3, you can create:

    3 = penny + penny + penny
   12 = dime + penny + penny
   21 = dime + dime + penny
   30 = dime + dime + dime

For example:

    >>> coins(0) == {0}
    True

    >>> coins(1) == {1, 10}
    True

    >>> coins(2) == {2, 11, 20}
    True

    >>> coins(3) == {3, 12, 21, 30}
    True

    >>> coins(4) == {4, 13, 22, 31, 40}
    True

    >>> coins(10) == {10, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100}
    True
"""

# START SOLUTION

DIME = 10
PENNY = 1


def add_coins(left, total, results):
    """Add combos coins to total.

    If this is the last time we can add coins, return change.

    Otherwise, recursively call until that condition.

        >>> results = set()
        >>> add_coins(left=1, total=0, results=results)
        >>> results == set([1, 10])
        True
    """

    if left == 0:
        # Base Case
        # We've added all the coins we're supposed to, so keep
        # track of this total of change and stop recursing
        results.add(total)
        return

    # Fork into two recursions, one adding a dime and another a penny
    # For each, we'll have 1 fewer coin to add afterwards, so left -= 1
    add_coins(left - 1, total + DIME, results)
    add_coins(left - 1, total + PENNY, results)

# END SOLUTION


def coins(num_coins):
    """Find change from combinations of `num_coins` of dimes and pennies.

    This should return a set of the unique amounts of change possible.
    """

    # START SOLUTION

    results = set()

    add_coins(left=num_coins, total=0, results=results)

    return results

    # END SOLUTION


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU CAN TAKE THAT TO THE BANK!\n"
