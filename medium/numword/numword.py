"""Convert an integer number to the word representation.

We should handle zero:

    >>> num_word(0)
    'zero'

And numbers under a thousand:

    >>> num_word(2)
    'two'

    >>> num_word(-2)
    'negative two'

    >>> num_word(11)
    'eleven'

    >>> num_word(20)
    'twenty'

    >>> num_word(100)
    'one hundred'

    >>> num_word(121)
    'one hundred twenty one'

And numbers over a thousand:

    >>> num_word(1256)
    'one thousand two hundred fifty six'

    >>> num_word(100001)
    'one hundred thousand one'

    >>> num_word(1000000)
    'one million'

And all numbers ranging from -999,999,999,999 to 999,999,999,999 (you
can stop there):

    >>> num_word(-1234567890)  # doctest:+NORMALIZE_WHITESPACE
    'negative one billion two hundred thirty four million
    five hundred sixty seven thousand eight hundred ninety'

    >>> num_word(999999999999)  # doctest:+NORMALIZE_WHITESPACE
    'nine hundred ninety nine billion nine hundred ninety nine million
    nine hundred ninety nine thousand nine hundred ninety nine'

"""

# Leave a blank space for zero -- we don't want to print anything for this.
# Otherwise, put a space at the end of each word

ONES = ["", "one ", "two ", "three ", "four ", "five ", "six ", "seven ",
        "eight ", "nine ", "ten ", "eleven ", "twelve ", "thirteen ",
        "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ",
        "nineteen "]

# Leave a space for 0-tens and teens (teens are printed in the ONES, above)

TENS = ["", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ",
        "seventy ", "eighty ", "ninety "]

# Leave a space for the 0-thousands (there's no label for those)

THOUSANDS = ["", "thousand ", "million ", "billion "]


def _handle_cluster(n):
        out = ""

        if n >= 100:
            out += ONES[n / 100] + "hundred "
            n %= 100

        if n >= 20:
            out += TENS[n / 10]
            n %= 10

        out += ONES[n]

        return out


def num_word(num):
    """Convert word to number."""

    output = []

    # assess pos vs negative
    if num < 0:
        output.append("negative ")
        num *= -1

    # break number into list of three-digit clusters to be treated the same
    clusters = []
    while num >= 1000:
        num, rem = divmod(num, 1000)
        clusters.append(rem)
    clusters.append(num)

    # print clusters
    lengths = {0: "", 1: "thousand ", 2: "million ", 3: "billion "}

    while clusters:
        cluster = clusters.pop()
        output.append(_handle_cluster(cluster))
        if cluster > 0:
            output.append(lengths[len(clusters)])

    return "".join(output).strip() or "zero"






if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT JOB!\n"
