# To solve this, we first made a is_prime function that checks for prime numbers:

def is_prime(num):
    """Is num a prime number?

    num will always be a positive integer.

    >>> is_prime(0)
    False

    >>> is_prime(1)
    False

    >>> is_prime(2)
    True

    >>> is_prime(3)
    True

    >>> is_prime(4)
    False

    >>> is_prime(7)
    True

    >>> is_prime(25)
    False
    """

    assert num >= 0, "Num should be a positive integer!"

    # definition: 0 and 1 are not prime
    if num < 2:
        return False

    # definition: 2 is prime
    if num == 2:
        return True

    # if it's divisible by 2, it's not prime
    # (We do this as a special case, so that after this we can check
    # only odd numbers -- all even numbers are divisible by 2)
    if num % 2 == 0:
        return False

    # see if number is prime -- we'll do this by checking
    # to see if there's any odd number 3 .. sqrt(num)
    # that evenly divides num (why square root? think about it!)

    n = 3

    while n * n <= num:
        if num % n == 0:
            return False
        # Go to next odd number
        n += 2

    return True
# it treats 2 as a special case (2 is a prime number) and multiples of 2 are not.
# it then only has to check whether the number is divisible by prime numbers
# it only checks up to sqrt(num) – why? Think about it!


# We then made a primes function:

def primes(count):
    """Return count number of prime numbers, starting at 2."""

    # START SOLUTION

    primes = []
    num = 2

    while count > 0:

        if is_prime(num):
            primes.append(num)
            count -= 1

        num += 1

    return primes


# Sieve of Eratosthenes

# In our problem, we had to find the first count number primes. If our problem was different – to find all prime numbers less than or equal to max_prime, we could have used a more efficient algorithm, the Sieve of Eratosthenes.

# This algorithm finds all prime numbers in a range by efficiently getting rid of non-primes.

# Advanced: Are there ways you could think of to use this to help make your program more efficient?