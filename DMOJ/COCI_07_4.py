'''
Your program will be given an integer X. Find the smallest number larger than X consisting of the same digits as X.

Input Specification
The first line of input contains the integer X (1≤X≤999999).

The first digit in X will not be a zero.
'''

from itertools import permutations
from utils import timed

@timed
def smallestPermutation(num):
    perms = [int(''.join(p)) for p in permutations(num)]
    lowest = 0

    for n in perms:
        if n > int(num) and (n < lowest or lowest == 0):
            lowest = n

    return lowest

print(smallestPermutation(input()))
