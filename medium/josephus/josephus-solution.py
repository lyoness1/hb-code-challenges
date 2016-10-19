"""Given num_people in circle, kill [kill_every]th person, return survivor.

    >>> find_survivor(4, 2)
    1

    >>> find_survivor(41, 3)
    31

As a sanity case, if never skip anyone, the last person will be our survivor:

    >>> find_survivor(10, 1)
    10

"""


# START SOLUTION

class Node(object):
    """Doubly-linked node."""

    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return "<Node prev=%s data=%s next=%s>" % (
            self.prev.data, self.data, self.next.data)

    @classmethod
    def make_list(cls, n):
        """Construct a circular doubly-linked list of n items. Returns head node.

            >>> node = Node.make_list(3)

            >>> node.data
            1

            >>> node.next.data
            2

            >>> node.next.next.next.data
            1

            >>> node.prev.data
            3

            >>> node.prev.prev.prev.data
            1
        """

        # Make the first node (and remember that it's the first)
        first = node = prev = cls(1)

        # Make every other node
        for i in range(2, n + 1):
            node = Node(i, prev=prev)
            prev.next = node
            prev = node

        # Fix the last and first node's prev/next
        node.next = first
        first.prev = node

        return first

# END SOLUTION


def find_survivor(num_people, kill_every):
    """Given num_people in circle, kill [kill_every]th person, return survivor."""

    # START SOLUTION

    node = Node.make_list(num_people)

    # Loop until we're the only item in the list (last survivor)
    while node.next != node:

        for i in range(kill_every - 1):
            # If we will every 3rd person, we'll skip over two
            node = node.next

        # We're on the node to kill. Remove it from our doubly-linked list
        node.prev.next = node.next
        node.next.prev = node.prev

        node = node.next

    return node.data

    # END SOLUTION


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T!\n"
