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

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; NICE JOB!\n"
