"""Turn a string of 24h time into words.

You can trust that you'll be given a valid string (it will
always have a two-digit hour 00-23, and a two-digit minute
00-59). Hours 0-11 are am, and hours 12-23 are pm.

Handle noon and midnight specially:

    >>> time_word("00:00")
    'midnight'

    >>> time_word("12:00")
    'noon'

Otherwise, covert times to text:

    >>> time_word("01:00")
    "one o'clock am"

    >>> time_word("06:01")
    'six oh one am'

    >>> time_word("06:10")
    'six ten am'

    >>> time_word("06:18")
    'six eighteen am'

    >>> time_word("06:30")
    'six thirty am'

    >>> time_word("10:34")
    'ten thirty four am'

Don't forget to handle early morning properly:

    >>> time_word("00:12")
    'twelve twelve am'

For times after noon, add 'pm'

    >>> time_word("12:09")
    'twelve oh nine pm'

    >>> time_word("23:23")
    'eleven twenty three pm'

By Joel Burton <joel@joelburton.com>.
"""

# START SOLUTION CONSTANTS

HOURS = ["twelve", "one", "two", "three", "four", "five", "six",
         "seven", "eight", "nine", "ten", "eleven"]

ONES = ["", "one", "two", "three", "four", "five", "six",
        "seven", "eight", "nine", "ten", "eleven", "twelve",
        "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
        "eighteen", "nineteen"]

TENS = ["", "", "twenty", "thirty", "forty", "fifty"]

# END SOLUTION CONSTANTS


def time_word(time):
    """Convert time to text."""

    # START SOLUTION

    if time == "00:00":
        return "midnight"

    if time == "12:00":
        return "noon"

    # "06:30" -> 6 hours, 30 minutes
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)

    # Add hour (uses 'twelve' for 0)
    out = HOURS[hours % 12] + " "

    if minutes >= 20:  # "twenty " ... "fifty nine"
        out += TENS[minutes / 10] + " " + ONES[minutes % 10]

    elif minutes >= 10:  # "ten", "eleven", ..., "nineteen"
        out += ONES[minutes]

    elif minutes > 0:  # "oh one" ... "oh nine"
        out += "oh " + ONES[minutes]

    else:
        out += "o'clock"

    # There might be space at the end (if we ended with a tens
    # and nothing after it, like 06:30 -> "six thirty "), so
    # strip it off, then add a space and am/pm indicator.
    return out.rstrip() + (" pm" if hours >= 12 else " am")

    # END SOLUTION


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. YOU'RE A TIME WIZARD!\n"