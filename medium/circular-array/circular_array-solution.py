"""Implement a Circular Array

A circular array is defined by having a start and indexes (be
sure to think about optimizing runtime for indexing)::

    >>> circ = CircularArray()
    >>> circ.add_item('harry')
    >>> circ.add_item('hermione')
    >>> circ.add_item('ginny')
    >>> circ.add_item('ron')
    >>> circ.print_array()
    harry
    hermione
    ginny
    ron
    >>> circ.get_by_index(2)
    'ginny'
    >>> print circ.get_by_index(15)
    None

However, the last item circles back around to the first item, 
so you can also rotate the list and shift the indexes. Positive
numbers rotate the list start to the right (or higher indexes)::

    >>> circ = CircularArray()
    >>> circ.add_item('harry')
    >>> circ.add_item('hermione')
    >>> circ.add_item('ginny')
    >>> circ.add_item('ron')
    >>> circ.rotate(1)
    >>> circ.print_array()
    hermione
    ginny
    ron
    harry
    >>> circ.get_by_index(2)
    'ron'

And negative numbers rotate the list start to the left (or lower
indexes)::

    >>> circ = CircularArray()
    >>> circ.add_item('harry')
    >>> circ.add_item('hermione')
    >>> circ.add_item('ginny')
    >>> circ.add_item('ron')
    >>> circ.rotate(-1)
    >>> circ.print_array()
    ron
    harry
    hermione
    ginny
    >>> circ.get_by_index(2)
    'hermione'

And you can also rotate more than once around the ring::

    >>> circ = CircularArray()
    >>> circ.add_item('harry')
    >>> circ.add_item('hermione')
    >>> circ.add_item('ginny')
    >>> circ.add_item('ron')
    >>> circ.rotate(-17)
    >>> circ.get_by_index(1)
    'harry'

If you add a new item after rotating, it should go at the end of
the list in its current rotation::

    >>> circ = CircularArray()
    >>> circ.add_item('harry')
    >>> circ.add_item('hermione')
    >>> circ.add_item('ginny')
    >>> circ.add_item('ron')
    >>> circ.rotate(-2)
    >>> circ.add_item('dobby')
    >>> circ.print_array()
    ginny
    ron
    harry
    hermione
    dobby

"""


class CircularArray(object):
    """An array that may be rotated, and items retrieved by index"""

    def __init__(self):
        """Instantiate CircularArray."""

        # START SOLUTION

        # using a list to store the array instead of linked-list
        # style nodes in order to optimize runtime for indexes
        self.array = []

        # track the current item at index 0 for the circular array
        # by storing that item's actual index in self.array.
        # Store None for an empty array.
        self.head = None

        # END SOLUTION

    def add_item(self, item):
        """Add item to array, at the end of the current rotation."""

        # START SOLUTION

        if self.head is None:
            # if there are currently no items in the array, set
            # `self.array` to contain our new item, and set the head
            # to point to that item (at index 0 in self.array).
            self.head = 0
            self.array = [item]
        else:
            # insert item. If we insert it at the self.head position,
            # it will  get inserted just before the head, which puts
            # it at the end of the current rotation
            self.array.insert(self.head, item)

            # reassign head --- it has shifted ahead by one thanks
            # to the insert for the new item.
            self.head += 1

        # END SOLUTION

    def get_by_index(self, index):
        """Return the data at a particular index."""

        # START SOLUTION

        # index doesn't exist the list, return None
        if index >= len(self.array):
            return None

        # this is the easy case -- the index doesn't go off the
        # end of self.array when you start from head
        if index + self.head < len(self.array):
            return self.array[index + self.head]

        # the fun case: we have to go round the twist (beyond end of
        # self.array). 
        # In this case, add index to self.head and then shift left by
        # the length of array to get back into self.array index space
        adjusted_index = index + self.head - len(self.array)
        return self.array[adjusted_index]

        # END SOLUTION

    def rotate(self, increment):
        """Rotate array, positive for right, negative for left.

        If increment is greater than list length, keep going around.
        """

        # START SOLUTION

        # if the array doesn't have any elements, don't do anything
        if not self.head:
            return

        # mod take care of cases where we've gone all the way around
        adjusted_index = (increment + self.head) % len(self.array)
        self.head = adjusted_index

        # END SOLUTION

    def print_array(self):
        """Print the circular array items in order, one per line"""

        # START SOLUTION

        for i in range(len(self.array)):
            print self.get_by_index(i)

        # END SOLUTION

if __name__ == "__main__":
    print
    import doctest

    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED; YOU MUST BE DIZZY WITH JOY! ***"
    print
