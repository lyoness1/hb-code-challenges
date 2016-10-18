"""Lazy lemmings.

Find the farthest any single lemming needs to travel for food.

    >>> furthest(3, [0, 1, 2])
    0

    >>> furthest(3, [2])
    2

    >>> furthest(3, [0])
    2

    >>> furthest(6, [2, 4])
    2
"""


def furthest(num_holes, cafes):
    """Find longest distance between a hole and a cafe."""

    dists_to_cafes = [(cafes[i+1] - cafes[i])/2 for i in xrange(len(cafes)-1)]

    if dists_to_cafes:
        return max(cafes[0], max(dists_to_cafes), num_holes - 1 - cafes[-1])

    else:
        return max(cafes[0], num_holes - 1 - cafes[-1])










if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; GREAT JOB!\n"
