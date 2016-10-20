"""Merge sort.

    >>> nums = [3, 5, 10, 2, 1, 9, 7, 6, 4, 8]
    >>> merge_sort(nums)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""


def merge_sort(lst):
    """Divide and conquer: reduce to lists of 0-1 items, then recombine."""
    
    # base case: list is 0 or 1 long (already sorted)
    if len(lst) < 2:
        return lst

    # break list in half, sort each half
    left, right = merge_sort(lst[:len(lst)/2]), merge_sort(lst[len(lst)/2:])

    # combine sorted lists
    merged = []
    while left and right:
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    if left and not right:
        merged.extend(left)

    if right and not left:
        merged.extend(right)

    return merged




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"
