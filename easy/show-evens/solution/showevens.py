"""Given list of ints, return list of *indices* of even numbers in list.

For example::

    >>> show_evens([])
    []

    >>> show_evens([2])
    [0]

    >>> show_evens([1, 2, 3, 4])
    [1, 3]

"""


def show_evens(nums):
    """Given list of ints, return list of *indices* of even numbers in list."""

    # START SOLUTION

    out = []

    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            out.append(i)

    return out

    # Alternately, we could use the `enumerate()` function:
    #
    # for i, n in enumerate(nums):
    #     if n % 2 == 0:
    #         out.append(i)
    #
    # return out
    #

    # Or, even prettier, write as a list comprehension
    #
    # return [i for i, n in enumerate(nums) if n % 2 == 0]

    # END SOLUTION


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. EVENLY HANDLED!\n"
