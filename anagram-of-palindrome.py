"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

I'm adding a line of comment here just to test some git stuff... 

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    # Keep track of character counts in a dictionary
    chars = {}
    for ch in word:
        if ch in chars:
            chars[ch] += 1
        else:
            chars[ch] = 1

    # If ana-of-pal, char count will be even, with one odd OK. 
    odd_counts = 0
    for count in chars.values():
        if count % 2 != 0:
            odd_counts += 1

    # Determine palindrominess
    if odd_counts <= 1:
        return True

    return False




if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"
