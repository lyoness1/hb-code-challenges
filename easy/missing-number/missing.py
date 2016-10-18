"""Given a list of numbers 1...max_num, find which one is missing in a list."""


def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number([1, 2, 3, 4, 6, 7, 8], 8)
    5

    """

    # brute force ( is this O(n)? )
    for i in range(len(nums) - 1):
        if nums[i+1] - nums[i] == 2:
            return nums[i] + 1


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASS. NICELY DONE!\n"
