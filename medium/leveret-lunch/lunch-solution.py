"""Leveret lunch count.

Check that garden is valid::

    >>> garden = [
    ...     [1, 1],
    ...     [1],
    ... ]

    >>> lunch_count(garden)
    Traceback (most recent call last):
    ...
    AssertionError: Garden not a matrix!

    >>> garden = [
    ...     [1, 1],
    ...     [1, 'a'],
    ... ]

    >>> lunch_count(garden)
    Traceback (most recent call last):
    ...
    AssertionError: Garden values must be ints!

Consider simple cases::

    >>> garden = [
    ...     [0, 0, 0],
    ...     [0, 0, 0],
    ...     [0, 0, 0]
    ... ]

    >>> lunch_count(garden)
    0

    >>> garden = [
    ...     [1, 1, 1],
    ...     [0, 1, 1],
    ...     [9, 1, 9]
    ... ]

    >>> lunch_count(garden)
    3

    >>> garden = [
    ...     [1, 1, 1],
    ...     [1, 1, 1],
    ...     [1, 1, 1]
    ... ]

    >>> lunch_count(garden)
    9

Make sure it works with even-sides
(this will start with the 4 and head east)::

    >>> garden = [
    ...     [9, 9, 9, 9],
    ...     [9, 3, 1, 0],
    ...     [9, 1, 4, 2],
    ...     [9, 9, 1, 0],
    ... ]

    >>> lunch_count(garden)
    6

Consider our most complex case::

    >>> garden = [
    ...     [2, 3, 1, 4, 2, 2, 3],
    ...     [2, 3, 0, 4, 0, 3, 0],
    ...     [1, 7, 0, 2, 1, 2, 3],
    ...     [9, 3, 0, 4, 2, 0, 3],
    ... ]

    >>> lunch_count(garden)
    15

"""


def lunch_count(garden):
    """Given a garden of nrows of ncols, return carrots eaten."""

    # Sanity check that garden is valid

    row_lens = [len(row) for row in garden]
    assert min(row_lens) == max(row_lens), "Garden not a matrix!"
    assert all(type(c) is int for c in row for row in garden), \
        "Garden values must be ints!"

    # Get number of rows and columns

    nrows = len(garden)
    ncols = len(garden[0])

    # START SOLUTION

    def most_carrots(cells):
        """Find cell with most carrots.

        Given list of (row, col) coords, return coords w/max carrots.
        Cells provided may be outside grid; drop invalid cells.

        If zero carrots can be found, returns None.

        For example::

            >>> garden = [[2, 3],
            ...           [0, 3]]

        For single cell, this should win, as long as it has carrots::

            >>> most_carrots([(0, 0)])
            (0, 0)

        If no carrots can be found, return 0::

            >>> most_carrots([1, 0])
            None

        With a tie (for 3), prefer first-given::

            >>> most_carrots([(0, 0), (0, 1), (1, 0), (1, 1)])
            (0, 1)

        Make sure illegal cells aren't considered::

            >>> most_carrots([(-1, -1), (0, 0), (2, 2)])
            (0, 0)
        """

        # Make list of (#-carrots, row, col) from cells
        # Throw out cells that are outside the garden grid.

        legal = [(row, col) for row, col in cells
                 if 0 <= row < nrows and 0 <= col < ncols]

        num_carrots = 0
        best = None

        for row, col in legal:
            if num_carrots < garden[row][col]:
                num_carrots = garden[row][col]
                best = row, col

        return best

    eaten = 0

    # Find center cells. There can be at most four center cells,
    # if both ncols and nrows are odd. Since we're guaranteed that
    # there will never be tie of number of carrots in center cells,
    # we don't have to worry if a particular cell is duplicated, so
    # we can just test all possible center cells.

    consider = [
        ((nrows - 1) / 2, (ncols - 1) / 2),
        ((nrows - 1) / 2, (ncols - 0) / 2),
        ((nrows - 0) / 2, (ncols - 1) / 2),
        ((nrows - 0) / 2, (ncols - 0) / 2)
    ]

    while True:

        # Find row, col coords of cell with most carrots
        curr = most_carrots(consider)

        if not curr:
            # We can't find any carrots, so take nap & return
            return eaten

        row, col = curr

        # Eat carrots in that cell and mark it as eaten
        eaten += garden[row][col]
        # print consider, row, col, garden[row][col], eaten
        garden[row][col] = 0

        # Use the WNES neighbors as our next cells to consider.
        # The order here is important --- most_carrots breaks ties
        # by using the first-of-ties, so ensure these are WNES

        consider = [
            (row, col - 1),  # W
            (row - 1, col),  # N
            (row, col + 1),  # E
            (row + 1, col),  # S
        ]

# END SOLUTION


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASS! HOP ALONG NOW!\n"
