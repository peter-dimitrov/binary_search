#!/bin/python3

def find_smallest_positive(xs):
    '''
    Assume that xs is a list of numbers sorted from LOWEST to HIGHEST.
    Find the index of the smallest positive number.
    If no such index exists, return `None`.

    HINT: 
    This is essentially the binary search algorithm from class,
    but you're always searching for 0.

    >>> find_smallest_positive([-3, -2, -1, 0, 1, 2, 3])
    4
    >>> find_smallest_positive([1, 2, 3])
    0
    >>> find_smallest_positive([-3, -2, -1]) is None
    True
    '''
    if len(xs) == 0:
        return None
    if len(xs) == 1:
        if xs[0] <= 0:
            return None
        else:
            return 0
    left = 0
    right = len(xs)-1
    def go(left, right):
        mid = (left+right)//2
        if xs[mid]>0:
            right = mid
        if xs[mid]<0:
            left = mid+1
        if xs[mid]==0:
            if xs[-1] != 0:
                return mid+1
            else:
                return None
        if left == right:
            if xs[left] <= 0:
                return None
            else:
                return left
        return go(left, right)
    return go(left,right)


def count_repeats(xs, x):
    '''
    Assume that xs is a list of numbers sorted from HIGHEST to LOWEST,
    and that x is a number.
    Calculate the number of times that x occurs in xs.

    HINT: 
    Use the following three step procedure:
        1) use binary search to find the lowest index with a value >= x
        2) use binary search to find the lowest index with a value < x
        3) return the difference between step 1 and 2

    I highly recommend creating stand-alone functions for steps 1 and 2
    that you can test independently.

    >>> count_repeats([5, 4, 3, 3, 3, 3, 3, 3, 3, 2, 1], 3)
    7
    >>> count_repeats([1, 2, 3], 4)
    0
    '''
    if len(xs) == 0:
        return 0
    if len(xs) == 1:
        if xs[0] == x:
            return 1
        else:
            return 0
    if xs[-1] > xs[-2]:
        return 0
    if xs[0] == xs[-1] == x:
        return len(xs)
    a = bin_search_lowest_greater(xs,x)
    b = bin_search_lowest_less(xs,x)
    if xs[-1] == x:
        return b-a+1
    else:
        return b-a


def bin_search_lowest_greater(xs, x):
    left = 0
    right = len(xs)-1
    def go(left, right):
        mid = (left+right)//2
        if xs[mid]>x:
            if xs[mid+1] == x:
                return mid+1
            else:
                left = mid
        if xs[mid]<=x:
            right = mid
        if left == right:
            if xs[0] == x:
                return 0
            else:
                return left
        return go(left, right)
    return go(left,right)

def bin_search_lowest_less(xs, x):
    left = 0    
    right = len(xs)-1
    def go(left, right):
        mid = (left+right)//2
        if xs[mid]>=x:
            left = mid+1
        if xs[mid]<x:
            if xs[mid-1] == x:
                return mid
            else:
                right = mid
        if left == right:                
            if xs[-1] == x:
                return len(xs)-1
            else:
                return left
        return go(left, right)
    return go(left,right)


def argmin(f, lo, hi, epsilon=1e-3):
    '''
    Assumes that f is an input function that takes a float as input and returns a float with a unique global minimum,
    and that lo and hi are both floats satisfying lo < hi.
    Returns a number that is within epsilon of the value that minimizes f(x) over the interval [lo,hi]

    HINT:
    The basic algorithm is:
        1) The base case is when hi-lo < epsilon
        2) For each recursive call:
            a) select two points m1 and m2 that are between lo and hi
            b) one of the 4 points (lo,m1,m2,hi) must be the smallest;
               depending on which one is the smallest, 
               you recursively call your function on the interval [lo,m2] or [m1,hi]

    >>> argmin(lambda x: (x-5)**2, -20, 20)
    5.000040370009773
    >>> argmin(lambda x: (x-5)**2, -20, 0)
    -0.00016935087808430278
    '''
    if hi-lo < epsilon:
        return hi
    else:
        hival = f(hi)
        loval = f(lo)
        mid = (hi+lo)/2
        m1 = (lo+mid)/2
        m2 = (mid+hi)/2
        m1val = f(m1)
        m2val = f(m2)
        mini = min(loval, m1val, m2val, hival)
        if mini == loval or mini == m1val:
            return argmin(f, lo, m2, epsilon)
        else:
            return argmin(f, m1, hi, epsilon)
