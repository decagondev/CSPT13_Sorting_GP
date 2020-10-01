"""
One of the most straightforward problems we can solve recursively is to print every number from n down to zero in succession.
We can do that simply by writing a function that prints n, then calls itself for n-1:
"""
# import sys

n = 10
def countdown_i(n):
    while (n > 0): # condition and label
        print(n) # body
        n -= 1 # decrement


countdown_i(n)