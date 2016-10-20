"""When can the monkey cross the river?

In this problem, a monkey is trying to jump across a certain 
distance across a river, using stones in the river to break its
jumps into sections.

However, the monkey can only jump N number of stones at a time.

As an added piece of complexity, the water level is decreasing 
with each hour, and as the water level gets lower, more stones 
emerge for the monkey to use to cross the river.

We can represent the `stones` in the river like this::

    [ 1, 2, 5, 0, 3, 4 ]

Where the number in the array corresponds to when the stone will 
emerge. (Bigger numbers are later in time.)

The stone times are **unique** -- numbers in
the list will never appear more than once.

So, for the above array, at time `t`, the stones would emerge as::

    t     river (* stone, - not yet a stone)
    -     ----------------------------------
    0     [ -  -  -  *  -  -  ]
    1     [ *  -  -  *  -  -  ]
    2     [ *  *  -  *  -  -  ]
    3     [ *  *  -  *  *  -  ]
    4     [ *  *  -  *  *  *  ]

Write a function that given the `stones` in the river as represented 
above, and the number of stones the monkey is able to jump, the earliest
time `t` that the monkey would be able to make it across the river.

For example::

    >>> earliest_arrival(3, [1, 2, 3, 0])
    1

    >>> earliest_arrival(2, [1, 2, 3, 0])
    2

    >>> earliest_arrival(3, [1, 4, 0, 2, 3, 5])
    2

    >>> earliest_arrival(5, [5, 2, 3, 8, 9, 99, 4, 0])
    3

"""


def earliest_arrival(jump_distance, stones):
    """Find the earliest time a monkey can jump across a river."""

    # START SOLUTION

    # Position of monkey (-1 = the start)
    pos = -1
    
    # The time of all stones landed on
    landings = []
    
    while pos + jump_distance < len(stones):

        # Where can we jump to
        possible_landings = stones[pos + 1:pos + jump_distance + 1]

        # Take the earliest-time stone and keep track of its time
        soonest_landing = min(possible_landings)
        landings.append(soonest_landing)
        
        # Get our new position
        # (since stones list is defined in the problem to be unique,
        # we can find index of new position by using `list.index` ---
        # if there were repeat times, we'd need to do this differently)
        pos = stones.index(soonest_landing) 
        
    # What was the latest time of a stone used?
    return max(landings)

    # END SOLUTION


if __name__ == "__main__":
    import doctest
    if not doctest.testmod().failed:
        print "\n*** ALL TESTS PASS; YOU MUST BE JUMPING WITH JOY\n"
