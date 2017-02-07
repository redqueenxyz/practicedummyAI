#! /usr/bin/env python3

# 3.1: List rotations

def rotate(l, j):
    """
    Rotate an array l by j rotations. 

    Parameters
    ----------
    l : list
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

    # take last n elements 
    # append before any elements before n
     return(l[-j:] + l[:-j]) if l and n > 0 else print('Invalid inputs.')

        
# 3.2: Find differences

def findPairswithDiff(arr, diff):
    """
    Return a set of all values in an array with a given difference.

    Parameters
    ----------
    arr : list
        An array of arbitrary length. 
    diff : int
        Defines the amount of difference required. 

    Returns
    -------
    list
         A list containing the sets themselves that satisfy the condition.

    >>> findPairswithDiff([8, 12, 16, 17, 4, 0, 20], 4)
    [(4, 0), (8, 4), (12, 8), (16, 12)]
    """

    arr.sort()
    pairs = []

    [pairs.append((arr[i],arr[i-1])) for i in range(0,len(arr)) if arr[i]-arr[i-1]==diff]
    
    return(pairs)
