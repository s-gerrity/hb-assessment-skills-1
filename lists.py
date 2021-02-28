"""SKILLS: LISTS

Complete the following functions.
"""


def print_indices(items):
    """Print each item in the list, followed by its index.

    Do this without using a "counting variable" --- in other words,
    DON'T do this:

        >>> count = 0
        >>> for item in list:
        ...     print(count)
        ...     count = count + 1
        ...

    The output should look like this:

        >>> print_indices(['apple', 'berry', 'cherry'])
        apple 0
        berry 1
        cherry 2
    """
    
    #doesnt work    
    # find the index for each item in items
    # add item and index to a string
    # print one by one in the loop

    for i in range(len(items)):
        for item in items:
            print(f"{item} {i}")


def words_in_common(words1, words2):
    """Return words that are shared between `words1` and `words2`.

    The returned words are sorted alphabetically.

    NOTE: For this problem, feel free to use other data structures we've
    learned about in this class.

    For example:

    >>> words_in_common(
    ...     ['Python', 'Python', 'Python'],
    ...     ['Lizard', 'Turtle', 'Python']
    ... )
    ['Python']

    The returned list should not have any duplicates:

    >>> words_in_common(
    ...     ['cheese', 'cheese', 'cheese', 'cake'],
    ...     ['cheese', 'hummus', 'beets', 'cake']
    ... )
    ['cake', 'cheese']

    If there are no words in common, return an empty list:

    >>> words_in_common(
    ...     ['lamb', 'chili', 'cheese'],
    ...     ['cake', 'ice cream']
    ... )
    []
    """
    new_list = []
    for word in words1:
        if word in new_list:
            continue
        for item in words2:
            if word == item:
                new_list.append(word)
                new_list.sort()
    return print(new_list)

# def every_other_item(items):
#     """Return every other item in `items`, starting at first item.

#     For example:

#     >>> every_other_item(['a', 400, True, 'b', 0])
#     ['a', True, 0]
#     """

#     new_list = []
#     for index in range(0, len(items), 2):
#         new_list.append(items[index])
#     return print(new_list)


def smallest_n_items(items, n):
    """Return the `n` smallest integers in list in descending order.

    You can assume that `n` will be less than the length of the list.

    For example:

        >>> smallest_n_items([2, 6006, 700, 42, 6, 59], 3)
        [42, 6, 2]

    If `n` is 0, return an empty list:

        >>> smallest_n_items([3, 4, 5], 0)
        []

    Duplicates are OK:

        >>> smallest_n_items([1, 1, 1, 1, 1, 1], 2)
        [1, 1]
    """

    new_list = []
    for item in items:
        if n == 0:
            return print(new_list)
        items.sort()
        new_list = items[:n]
        new_list.reverse()
    return print(new_list)

#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\nALL TESTS PASSED. GOOD WORK!\n")