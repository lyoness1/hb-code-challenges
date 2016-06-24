def print_digits(num):
    """Given int, print digits in reverse order, starting with the ones place."""

    # START SOLUTION

    while not num % 10 == num:

        next_digit = num % 10
        print next_digit
        num = (num - next_digit) / 10

    print num