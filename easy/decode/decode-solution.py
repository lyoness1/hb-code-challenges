def decode(s):
    """Decode a string."""

    # START SOLUTION

    word = ""

    i = 0

    while i < len(s):

        num_to_skip = int(s[i])
        i += num_to_skip + 1

        word += s[i]

        i += 1

    return word