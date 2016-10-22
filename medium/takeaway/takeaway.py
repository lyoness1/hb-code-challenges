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
    """Determine which play can win takeaway. 2, 3, 5"""

    # memoize whether current player can win at n stones
    # include index n
    memo = [False for num in xrange(n+1)]
    
    # fill in memo for each play
    # i = 0 or 1 will always be losses for current player
    for i in xrange(2, n+1):
        # try every option
        for option in [2, 3, 5]:
            # if current play returns False, other player can't win
            # if other player can't win, current player will win
            if i >= option and memo[i - option] == False:
                memo[i] = True
                break

    # add one for zero indexed list
    return 1 if memo[n] == True else 2




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; NICE JOB!\n"
