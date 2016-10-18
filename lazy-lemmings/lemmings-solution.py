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

    # START SOLUTION

    worst = 0

    for hole in range(num_holes):

        # Looking at all cafes, find distance to this hole,
        # and choose the smallest distance.

        dist = min([abs(hole - cafe) for cafe in cafes])

        # Keep track of the longest distance we've seen

        worst = max(worst, dist)

    return worst


def furthest_optimized(num_holes, cafes):
    """Find longest distance between a hole and a cafe.

    This solution uses binary search to quickly find the
    one or two cafes closest to the hole. This makes the
    problem O(n log n), rather than O(n**2).
    """

    from bisect import bisect_left

    cafes = sorted(cafes)   # O(n log n)

    worst = 0

    for hole in range(num_holes):

        # Find the place we'd insert this hole into the
        # sorted cafes list.

        idx = bisect_left(cafes, hole)

        if idx == len(cafes):
            # This hole is after all the cafes, so the distance
            # is from this hole to the cafe before it
            dist = hole - cafes[idx - 1]

        elif idx == 0:
            # This hole is before all the cafes, so the distance
            # is from this hole to the cafe after it
            dist = cafes[idx] - hole

        elif cafes[idx] == hole:
            # This hole is a cafe, so no travel is needed!
            dist = 0

        else:
            # This hole is between two cafes, so use the smaller
            # distance between them
            dist = min(hole - cafes[idx - 1], cafes[idx] - hole)

        # Keep track of the longest distance we've seen
        worst = max(worst, dist)

    return worst

# END SOLUTION

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; GREAT JOB!\n"
