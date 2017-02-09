#! /usr/bin/env python3

"""An example solution to problem3."""

__author__ = "Vivek Menon"

## Arrays
# Array rotations

def rotate(array, j):
    """
    Rotate an array by j rotations.

    Parameters
    ----------
    array : list
        An array of arbitrary length.
    j : int
        Defines how many rotations are done.

    Returns
    -------
    list
        The array after rotations.

    >>> rotate( [1,2,3,4], 3)
    [2, 3, 4, 1]
    """

    # take last n elements using -j
    # append that in front of any elements before -j
    return(array[-j:] + array[:-j])


# Array differences

def pairswithdiff(arr, diff):
    """
    Return a set of all values in an array with a given difference.

    Parameters
    ----------
    arr : list
        An array of arbitrary length.
    diff : int
        The difference to look for.

    Returns
    -------
    list
         A list containing the sets themselves that satisfy the condition.

    >>> pairswithdiff([8, 12, 16, 17, 4, 0, 20], 4)
    [(4, 0), (8, 4), (12, 8), (16, 12)]
    """

    pairs = []

    for i in arr:
        for j in arr:
            if i - j == diff:
                pairs.append((i, j))

    return(pairs)
