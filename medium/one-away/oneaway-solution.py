"""Given two strings, are they, at most, one edit away?

    >>> one_away("make", "make")
    True

    >>> one_away("make", "fake")
    True

    >>> one_away("task", "take")
    False

    >>> one_away("ask" ,"asks")
    True

    >>> one_away("asks", "ask")
    True

    >>> one_away("act", "tact")
    True

    >>> one_away("fat", "fact")
    True

    >>> one_away("yes", "no")
    False

"""


def one_away(w1, w2):
    """Given two strings, are they, at most, one edit away?"""

    # START SOLUTION

    # Strings length can only vary by, at most, one letter
    if abs(len(w1) - len(w2)) > 1:
        return False

    # Make sure w2 is the shorter string
    if len(w2) > len(w1):
        w1, w2 = w2, w1

    # Keep track of number of wrong letters
    wrong = 0

    # Loop over w1 with i and over w2 with j
    i = j = 0

    while j < len(w2):

        if w1[i] != w2[j]:

            # We found a wrong letter
            wrong += 1
            if wrong > 1:
                return False

            # We'll move to the next char in the longer string.
            i += 1

            # If same length, move the next char in shorter.
            # Otherwise, don't move in shorter string --- this
            # will cover the case of a added letter.
            if len(w1) == len(w2):
                j += 1

        else:
            # Both letters match; move to next letter in both
            i += 1
            j += 1

    return True

    # END SOLUTION


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; NICE JOB! ***\n"
