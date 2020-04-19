# Make a random list and create a new list containing
# only the first and last elements of the random list.

import random

def list_ends(ranList):
    print("Original list    :", ranList)
    print("ListOf List ends :", [ranList[0], ranList[-1]])

list_ends([random.choice(range(1, 502)) for i in range(20)])
