def print_recursively(lst):
    """Print items in the list, using recursion."""

    # START SOLUTION

    if lst:
        print lst[0]
        print_recursively(lst[1:])