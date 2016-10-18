"""Is this binary search tree a valid BST?

A valid binary search tree follows a specific rule. In our case,
the rule is "left child must value must be less-than parent-value"
and "right child must be greater-than-parent value".

This rule is recursive, so *everything* left of a parent
must less than that parent (even grandchildren or deeper)
and everything right of a parent must be greater than.

For example, this tree is valid::

        4
     2     6
    1 3   5 7

Let's create this tree and test that::

    >>> t = Node(4,
    ...       Node(2, Node(1), Node(3)),
    ...       Node(6, Node(5), Node(7))
    ... )

    >>> t.is_valid()
    True

This tree isn't valid, as the left-hand 3 is wrong (it's less
than 2)::

        4
     2     6
    3 3   5 7

Let's make sure that gets caught::

    >>> t = Node(4,
    ...       Node(2, Node(3), Node(3)),
    ...       Node(6, Node(5), Node(7))
    ... )

    >>> t.is_valid()
    False

This tree is invalid, as the bottom-right 1 is wrong --- it is
less than its parent, 6, but it's also less than its grandparent,
4, and therefore should be left of 4::

        4
     2     6
    1 3   1 7

    >>> t = Node(4,
    ...       Node(2, Node(1), Node(3)),
    ...       Node(6, Node(1), Node(7))
    ... )

    >>> t.is_valid()
    False
"""


class Node:
    """Binary search tree node."""

    def __init__(self, data, left=None, right=None):
        """Create node, with data and optional left/right."""

        self.left = left
        self.right = right
        self.data = data

    def is_valid(self):
        """Is this tree a valid BST?"""

        # START SOLUTION

        def _ok(n, lt, gt):
            """Check this node & recurse to children

                lt: left children must be <= this
                gt: right child must be >= this
            """

            if n is None:
                # base case: this isn't a node
                return True

            if lt is not None and n.data > lt:
                # base case: bigger than allowed
                #  we'll fail fast here
                return False

            if gt is not None and n.data < gt:
                # base case: smaller than allowed
                #  we'll fail fast here
                return False

            if not _ok(n.left, n.data, gt):
                # general case: check our left child
                #   all descendants of left child must be
                #   less than our data (and greater than
                #   whatever we had to be greater than).
                #   if not, fail fast.
                return False

            if not _ok(n.right, lt, n.data):
                # general case: check our right child
                #   all descendants of right child must be
                #   greater than our data (and less than
                #   whatever we had to be less than)
                #   if not, fail fast.
                return False

            # If we reach here, we're either a leaf node with
            # valid data for lt/gt, or we're higher up, but
            # our recursive calls downward succeeded. Either way,
            # this is our winning base case.
            return True

        # Call our recursive function, starting here.
        # Since we haven't yet gone left or right, we don't know
        # our `lt` or `gt` values yet, so pass None for these.

        return _ok(self, None, None)

    def is_valid_exception(self):
        """Is tree a valid BST?

        This recurses similiarly to `is_valid`, but it uses
        exceptions to immediate exit when an invalid value is
        found. Using execeptions for quick control-passing can
        sometimes make for clearer code.
        """

        def _ok(n, lt, gt):
            """Check this node & recurse to children

                lt: left children must be <= this
                gt: right child must be >= this
            """

            if n is None:
                # base case: this isn't a node
                return

            if ((lt is not None and n.data > lt) or
                    (gt is not None and n.data < gt)):
                # base case: we're either smaller or bigger
                # than allowed. Raise exception to return
                # back to `is_valid_exception`
                raise ValueError

            # Check our children (see `is_valid` for comments)
            _ok(n.left, n.data, gt)
            _ok(n.right, lt, n.data)

        # Call our recursive function --- if it returns,
        # the tree is valid. If it raises a ValueError, it's
        # invalid.

        try:
            _ok(self, None, None)
            return True

        except ValueError:
            return False

    def is_valid_expression(self, lt=None, gt=None):
        """Is tree a valid BST?

        This uses a single expression --- the logic is the same
        as `is_valid`, but packed into an expression.

        This is a useful demonstration of how powerful logical
        expressions can be, but it's probably a terrible way to
        write this.
        """

        return (
            not (lt is not None and self.data >= lt) and
            not (gt is not None and self.data <= gt) and
            (self.left is None or
             self.left.is_valid_4(self.data, gt)) and
            (self.right is None or
             self.right.is_valid_4(lt, self.data))
        )

    def __iter__(self):
        """Iterate over nodes in BST in proper order.

        The __iter__ method is called when you iterate
        over an object. It should yield successive
        values (for information on yielding, learn about
        "generators").

        Our BST can be iterated over to get the values
        in order. For example, for this tree::

                4
             2     6
            1 3   5 7

        We can loop over it::

            >>> t = Node(4,
            ...       Node(2, Node(1), Node(3)),
            ...       Node(6, Node(5), Node(7))
            ... )

            >>> for n in t:
            ...     print n.data,
            1 2 3 4 5 6 7

        This method of navigating a BST by left-recurse, self,
        right-recurse, is often called "in-order traversal".
        """

        # walk the left descendants recursively:
        for n in self.left or []:
            yield n

        # hand back this node
        yield self

        # walk the right descendants recursively:
        for n in self.right or []:
            yield n

    def is_valid_using_iter_sort(self):
        """Is tree a valid BST?

        Compare the iteration order with the sort order; if
        they're different, it's not a valid tree.

        This method of checking for validity isn't nearly as
        efficient --- we have to walk the tree (O(n))
        and then sort the nodes (O(n log n)). Our runtime is
        therefore O(n log n), which is greater than O(n) for
        the other methods. We also can't fail-fast, unlike the
         other methods --- they quit as soon as they find
         an invalid value, whereas this iterates over the
         entire tree.

        It is a good example of how having an __iter__ method
        can be useful, though.
        """

        # Get node data in traversal-order
        values = [n.data for n in self]

        return values == sorted(values)

    def is_valid_using_iter_check(self):
        """Is tree a valid BST?

        Another way to use our __iter__ method --- this time,
        walking over the iteration, and just making sure it
        doesn't ever go backwards.

        This solution is O(n) and does let us fail fast.
        """

        last = None

        for n in self:
            if last is not None and n.data < last:
                return False
            last = n.data

        # Made it through without problerms, in right order!
        return True

        # Another possibility in similar style.
        # This is still O(n), but no longer fails fast --- since
        # ``list(self)`` will traverse the entire tree

        ns = list(self)
        return all(ns[i] >= ns[i - 1] for i in range(1, len(ns)))


# END SOLUTION

if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; THAT'S VALID!\n"
