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


def find_most_anagrams_from_wordlist(wordlist):
    """Given list of words, return the word with the most anagrams."""

    anagrams = {}
    max_anagrams = 0
    max_anagrams_word = None

    for word in wordlist:

        # key is a sorted string of characters in each word
        chars = "".join(sorted([char.lower() for char in word]))

        # keep track of words in list by their sorted string key
        if chars in anagrams:
            anagrams[chars].append(word)
        else:
            anagrams[chars] = [word]

        # keep track of max key and num anagrams
        if len(anagrams[chars]) > max_anagrams:
            max_anagrams = len(anagrams[chars])
            max_anagrams_key = chars

    return anagrams[max_anagrams_key][0]


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"
