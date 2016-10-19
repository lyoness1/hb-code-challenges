"""Find the subsequence with the largest sum.

Given a list of integers, like:

  [1, 0, 3, -8, 4, -2, 3]

Return the contiguous subsequence with the largest sum. For
that example, the answer would be [4, -2, 3], which sums to 5.


    >>> largest_sum([1, 0, 3, -8, 4, -2, 3])
    [4, -2, 3]

    >>> largest_sum([1, 0, 3, -8, 4, -2, 3, -2])
    [4, -2, 3]

    >>> largest_sum([1, 0, 3, -8, 19, -20, 4, -2, 3, -2])
    [19]

For ties, return the first one:

    >>> largest_sum([2, 2, -10, 1, 3, -20])
    [2, 2]

Return the shortest version:

    >>> largest_sum([2, -2, 3, -1])
    [3]

    >>> largest_sum([-1, -2])
    [-1]
"""


def largest_sum(nums):
    """Find subsequence with largest sum."""

    # can't find sum of empty list
    if not nums:
        return None
    
    # initialize memoization of largest contig. sum possible up to that index
    largest_so_far = [[nums[0], 0]] + nums[1:]

    # track largest sum overall, and index where it occurs
    largest_sum = largest_so_far[0][0]
    largest_sum_idx = 0

    # iterate over list to find largest sum, keep traack of idx sum starts
    start_idx = 0
    for i in xrange(1, len(largest_so_far)):
        new_sum = max(largest_so_far[i-1][0] + nums[i], nums[i])
        # update largest overall sum, idx
        if new_sum > largest_sum:
            largest_sum = new_sum
            largest_sum_idx = i 
        # if curr value drops overall sum, restart starting index 
        if new_sum == nums[i]:
            start_idx = i
        # update memo with sum, start index
        largest_so_far[i] = [new_sum, start_idx]

    # return the section of nums from start idx of largest sum overall to sum
    return nums[largest_so_far[largest_sum_idx][1]:largest_sum_idx+1]






if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU HANDLED THIS SUMMARILY!\n"
