
def pig_latin(phrase):
    """Turn a phrase into pig latin.

    There will be no uppercase letters or punctuation in the phrase.

        >>> pig_latin('hello awesome programmer')
        'ellohay awesomeyay rogrammerpay'
    """

    vowels = ['a', 'e', 'i', 'o', 'u']
    words = phrase.split(' ')
    output = ""

    for word in words:
        if word[0] not in vowels:
            output += word[1:] + word[0] + "ay "
        else:
            output += word + "yay "

    return output.strip()


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. REATGAY OBJAY!\n"
