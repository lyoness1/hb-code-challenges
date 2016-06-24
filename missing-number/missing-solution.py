# Solution #1: Simple

# You could keep track of the numbers you’ve seen and then check which one is missing.

def missing_number_scan(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number_scan([1, 2, 3, 4, 5, 6, 7, 9, 10], 10)
    8
    """

    # 1st solution: Initial solution: keep track of what you've
    #               seen in a separate list

    seen = [False] * max_num

    for n in nums:
        seen[n - 1] = True

    # The False value is the one we haven't seen

    return seen.index(False) + 1

    
# Note how we’re keeping track of this—in a list with True or False for each value. This is a bit faster than, say, adding each “seen” number to a set, since we’d have do O(n) lookup for every number!
# This solution is O(n) and requires additional storage.





# Solution #2: Sorting

# For a simple O(n log n) solution, you could sort the numbers first, then scan them to see which one is missing:

def missing_number_sort(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number_sort([1, 2, 3, 4, 5, 6, 7, 9, 10], 10)
    8
    """

    # 2nd solution: if we can't create another data structure
    #               sort and scan for missing number

    nums.append(max_num + 1)
    nums.sort()
    last = 0

    for i in nums:
        if i != last + 1:
            return last + 1
        last += 1

    raise Exception("None are missing!")

# This solution does not require additional storage.





# Solution #3: Expected Sum

# For a clever-math related formula, you can just sum the numbers and subtract the sum from the expected sum—this will reveal the missing number!

def missing_number_sum(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list

    >>> missing_number_sum([1, 2, 3, 4, 5, 6, 7, 9, 10], 10)
    8
    """

    # 3rd solution: find missing number by comparing expected sum vs actual

    expected = sum(range(max_num + 1))

    # Alternatively, there's a math formula that finds the sum of 1..n
    # https://en.wikipedia.org/wiki/Arithmetic_progression#Sum
    #
    # expected = ( n + 1 ) * ( n / 2 )
    #
    # This makes this problem O(1) !

    return expected - sum(nums)

# This solution is O(n) and requires no additional lists. If you use the equation in comments, it becomes O(1).


