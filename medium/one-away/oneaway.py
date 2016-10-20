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

    if abs(len(w1) - len(w2)) > 1:
        return False

    i1 = i2 = diffs = 0

    while i1 < len(w1) and i2 < len(w2):
        # case: same letter
        if w1[i1] == w2[i2]:
            i1 += 1
            i2 += 1
        # case: extra letter in w2
        elif len(w1) < len(w2):
            diffs += 1
            i2 += 1
        # case: extra letter in w1
        elif len(w2) < len(w1):
            diffs += 1
            i1 += 1
        # case: typo in either
        elif len(w1) == len(w2):
            diffs += 1
            i1 += 1
            i2 += 1

        if diffs > 1:
                return False

    return True


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; NICE JOB! ***\n"
