# We wrote this as two functions.

# A helper function:

def pig_latin_word(word):
    """Turn a word into the pig latin version.

    For example::

        >>> pig_latin_word('porcupine')
        'orcupinepay'

        >>> pig_latin_word('apple')
        'appleyay'
    """

    if word[0] in 'aeiou':
        return word + 'yay'

    else:
        return word[1:] + word[0] + 'ay'


# The main function:

def pig_latin(phrase):
    """Turn a phrase into pig latin.

    There will be no uppercase letters or punctuation in the phrase.

        >>> pig_latin('hello awesome programmer')
        'ellohay awesomeyay rogrammerpay'
    """

    # START SOLUTION

    words = phrase.split(' ')

    pl_words = [pig_latin_word(w) for w in words]

    return " ".join(pl_words)