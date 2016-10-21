"""Takeaway game.

    >>> takeaway(1)
    2

    >>> takeaway(2)
    1

    >>> takeaway(3)
    1

    >>> takeaway(4)
    1

    >>> takeaway(5)
    1

    >>> takeaway(6)
    1

    >>> takeaway(7)
    2

    >>> takeaway(8)
    2

    >>> takeaway(9)
    1

    >>> takeaway(10)
    1

    >>> takeaway(20)
    1
"""


def takeaway(n):
    """Determine which play can win takeaway."""

    # START SOLUTION

    def _play(p, n):

        # To make it easier to invert p1 <-> p2,
        # we'll use 1 for p1, and -1 for p2.

        # If this player cannot move, opponent wins
        if n < 2:
            return -p

        # Try all of the legal moves
        for move in [2, 3, 5]:

            # If this player finds win with move, they win
            if _play(-p, n - move) == p:
                return p

        # No win was found, so the other player wins
        return -p

    return 1 if _play(1, n) == 1 else 2


def takeaway_dynamic(n):
    """Determine which play can win takeaway."""

    # cache of movies --- if the current player
    # wins w/this number of stones, `1`, else `-1`
    cache = {}

    def _play(p, n):

        # To make it easier to invert p1 <-> p2,
        # we'll use 1 for p1, and -1 for p2.

        # If this player cannot move, opponent wins
        if n < 2:
            return -p

        if n in cache:
            return cache[n] * p

        # Try all of the legal moves
        for move in [2, 3, 5]:
            result = _play(-p, n - move)

            # Cache this result --- but since it's seen from
            # the opponents view, store the opposite result
            # (ie, if opponent wins, store as a loss)
            cache[n - move] = -result

            # If this player finds win with move, they win
            if result == p:
                cache[n] = p
                return p

        # No win was found, so the other player wins
        cache[n] = -p
        return -p

    return 1 if _play(1, n) == 1 else 2

# END SOLUTION

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; NICE JOB!\n"
