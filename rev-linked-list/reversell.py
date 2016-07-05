"""Given linked list head node, return head node of new, reversed linked list.

For example:

    >>> ll = Node(1, Node(2, Node(3)))
    >>> reverse_linked_list_iteratively(ll).as_string()
    '321'
    >>> reverse_linked_list_recursively(ll).as_string()
    '321'
"""


class Node(object):
    """Class in a linked list."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def as_string(self):
        """Represent data for this node and it's successors as a string.

        >>> Node(3).as_string()
        '3'

        >>> Node(3, Node(2, Node(1))).as_string()
        '321'
        """

        out = []
        n = self

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(out)


def reverse_linked_list_iteratively(head):
    """Given LL head node, return head node of new, reversed linked list.

    >>> ll = Node(1, Node(2, Node(3)))
    >>> reverse_linked_list_iteratively(ll).as_string()
    '321'
    """

    output_head = None
    current = head

    while current:
        output_head = Node(current.data, output_head)
        current = current.next

    return output_head


def reverse_linked_list_recursively(head):
    """Given LL head node, return head node of new, reversed linked list.

    >>> ll = Node(1, Node(2, Node(3)))
    >>> reverse_linked_list_recursively(ll).as_string()
    '321'
    """

    tail = Node(head.data)

    def recurse_through_ll_helper(node, next):
        """progresses to end of ll"""

        # base case: reached tail
        if node.next == None:
            return Node(node.data, next)

        # progress toward base case:
        return recurse_through_ll_helper(node.next, Node(node.data, next))


    return recurse_through_ll_helper(head.next, tail)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. RIGHT ON!\n"
