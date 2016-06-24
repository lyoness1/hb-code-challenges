"""Return count number of prime numbers, starting at 2.

For example::

    >>> primes(0)
    []

    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

"""

def is_prime(num):
    """Checks if num is prime"""

    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    factor = 3

    while factor ** 2 <= num:
        if num % factor == 0:
            return False
        factor += 2

    return True


def primes(count):
    """Return count number of prime numbers, starting at 2."""

    primes = []

    num = 2

    while len(primes) < count:
        if is_prime(num):
            primes.append(num)
        num += 1

    return primes


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT WORK!\n"
