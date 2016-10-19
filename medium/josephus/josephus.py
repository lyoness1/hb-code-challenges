"""Given num_people in circle, kill [kill_every]th person, return survivor.

    >>> find_survivor(4, 2)
    1

    >>> find_survivor(41, 3)
    31

As a sanity case, if never skip anyone, the last person will be our survivor:

    >>> find_survivor(10, 1)
    10

"""


def find_survivor(num_people, kill_every):
    """Given num_people in circle, kill [kill_every]th person, return survivor."""

    # 1 represents alive, 0 represents dead
    people = [1 for person in xrange(num_people)]

    # track kills so we know when only one is left
    dead_count = 0
    # for a 0-indexed list, start at position -1
    position = -1
    # continue kills until only one left
    while dead_count < num_people - 1:
        # increment position 'kill_every' times, skipping already dead people
        for _ in xrange(kill_every):
            position += 1
            while people[position % num_people] == 0:
                position += 1
        # make the kill
        people[position % num_people] = 0
        dead_count += 1

    # add one because of 0-indexed list
    return people.index(1) + 1










if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T!\n"
