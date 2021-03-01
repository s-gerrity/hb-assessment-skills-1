"""SKILLS: LISTS

Complete the following functions.
"""


def print_indices(items):
    """Print each item in the list, followed by its index.

    Do this without using a "counting variable" --- in other words,
    DON'T do this:

        # # >>> count = 0
        # # >>> for item in list:
        # ...     print(count)
        # ...     count = count + 1
        ...

    The output should look like this:

        >>> print_indices(['apple', 'berry', 'cherry'])
        apple 0
        berry 1
        cherry 2
    """
    #Determine how many items in the list by length of list
    for i in range(0, len(items)):
        #Go through each item in the list
        for item in items:
            #If the index has not reached the end of the list
            if i < len(items):
                #Pring the name of the item and its index placement
                print(f"{item} {i}")
                #Increase the index placement for the next item in the list
                i += 1
        #If the index has reached the length of the list, stop printing and leave this function
        break


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

    #create a new, empty list
    new_list = []

    #Check through each word in the list
    for word in words1:
        #Check if the word in the list is already in the new list
        if word in new_list:
            #If it is, start the loop again and go through the next item in the new list
            continue
        #Check the items in our other list
        for item in words2:
            #Confirm if the item is the same as a word in our other list
            if word == item:
                #If it's the same, add it to our new list
                new_list.append(word)
                #Always sort the new list in alphabetical order
                new_list.sort()
    #When both lists have been searched and compared, print the new list of words in common
    return print(new_list)

def every_other_item(items):
    """Return every other item in `items`, starting at first item.

    For example:

    >>> every_other_item(['a', 400, True, 'b', 0])
    ['a', True, 0]
    """

    #Make a new empty list
    new_list = []

    #go through the items in the list, starting at the beginning, 
    # skipping every other one, and stopping when it's reached the end of the list
    for index in range(0, len(items), 2):
        #Add every other item to the new list
        new_list.append(items[index])

    #Print the new list!
    return print(new_list)


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

    #Start a new empty list
    new_list = []
    #Go through each item in the list of items
    for item in items:
        #If the input n has 0
        if n == 0:
            #Return an empty list
            return print(new_list)
        #If input is not zero, sort the items in the list from smallest to largest
        items.sort()
        #add the first n amount of items to the new empty list
        new_list = items[:n]
        #Swap the order so the items go in descending order
        new_list.reverse()
    #Print the new list of numbers    
    return print(new_list)
