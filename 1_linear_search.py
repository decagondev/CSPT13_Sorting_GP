# Linear Search

"""
Key Points
- Linear search is the simplest type of search we can do
- Sometimes it's the only method available. If the data is unordered, this is the only way to do it
- It also beats a binary search under some special circumstances
- Key words: unsorted, random
"""

import random
import time  # We'll use this later

my_range = 100
my_size = 100

my_random = random.sample(range(my_range), my_size)
print(my_random)

searching_for = 7

def linear_search(arr, target):
    pass

# Binary Search

"""
Key Points
- Binary search requires sorted data
- Each pass, we cut the remaining possibilities by half, hence the term binary
- Key words: sorted, ordered
"""

def find_value_binary(arr, value):
    pass



# Comparing Linear vs. Binary

"""
Key Points
- Binary search is only faster if the data is already sorted.
- It's slower for the first search if the data needs to be sorted first
- Subsequent searches will be much faster
"""

print("Linear")
start = time.time()
print(linear_search(my_random, searching_for))
end = time.time()
print(f"Runtime: {end - start}")

print("Binary")
start = time.time()
my_random.sort()
print(find_value_binary(my_random, searching_for))
end = time.time()
print(f"Runtime: {end - start}")


# lets see what heppens with multiple runs

# print("Linear")
# start = time.time()
# print(linear_search(my_random, searching_for))
# end = time.time()
# print(f"Runtime: {end - start}")

# print("Linear Again")
# start = time.time()
# print(linear_search(my_random, searching_for))
# end = time.time()
# print(f"Runtime: {end - start}")

# print("Binary")
# start = time.time()
# my_random.sort()
# print(find_value_binary(my_random, searching_for))
# end = time.time()
# print(f"Runtime: {end - start}")

# print("Binary _after_ sort")
# start = time.time()
# print(find_value_binary(my_random, searching_for))
# end = time.time()
# print(f"Runtime: {end - start}")