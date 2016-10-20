"""Merge sort.

    >>> nums = [3, 5, 10, 2, 1, 9, 7, 6, 4, 8]
    >>> merge_sort(nums)
    >>> nums
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""


def merge_sort(lst):
    """Divide and conquer: reduce to lists of 0-1 items, then recombine."""

    # START SOLUTION

    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        merge_sort(left)
        merge_sort(right)

        left_index = right_index = new_index = 0

        # Interleave lists together

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                lst[new_index] = left[left_index]
                left_index += 1
            else:
                lst[new_index] = right[right_index]
                right_index += 1
            new_index += 1

        # If lists were uneven length, add remainder of longer list

        while left_index < len(left):
            lst[new_index] = left[left_index]
            left_index += 1
            new_index += 1

        while right_index < len(right):
            lst[new_index] = right[right_index]
            right_index += 1
            new_index += 1

    # END SOLUTION

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"
