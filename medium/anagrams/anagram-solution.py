"""Given a list of words, return the word with the most anagrams.

For a list of ['act', 'cat', 'bill']:
- 'act' and 'cat' are anagrams, so they both have 2 matching words.
- 'bill' has no anagrams, os it has one matching word (itself).

Given that 'act' is the first instance of the most-anagrammed word,
we return that.

    >>> find_most_anagrams_from_wordlist(['act', 'cat', 'bill'])
    'act'

Let's use a file of words where each line is a word:

    >>> all_words = [w.strip() for w in open('words.txt')]
    >>> find_most_anagrams_from_wordlist(all_words)
    'angor'

"""

# START SOLUTION


def make_anagram_dict(words):
    """Return dict mapping sorted letters -> [words w/ those letters]

        >>> make_anagram_dict(["act", "cat", "dog", "god"])
        {'dgo': ['dog', 'god'], 'act': ['act', 'cat']}
    """

    out = {}

    for w in words:
        sorted_word = "".join(sorted(w))
        out.setdefault(sorted_word, []).append(w)

    return out

# END SOLUTION


def find_most_anagrams_from_wordlist(wordlist):
    """Given list of words, return the word with the most anagrams."""

    # START SOLUTION

    all_anagrams_dict = make_anagram_dict(wordlist)

    highest_num_anagrams = 0
    most_anagrams = None

    for w in wordlist:
        sorted_word = "".join(sorted(w))
        number_anagrams = len(all_anagrams_dict[sorted_word])
        if number_anagrams > highest_num_anagrams:
            highest_num_anagrams = number_anagrams
            most_anagrams = w

    return most_anagrams

    # END SOLUTION


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"
