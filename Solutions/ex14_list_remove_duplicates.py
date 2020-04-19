# Remove duplicates from a list
# Two ways:
#   Using a function to remove duplicates
#   Using python sets function

import random

def usingOnebyOne(lst):
    b = []
    for i in lst:
        if i not in b:
            b.append(i)
    return b

def usingSetFunc(lst):
    return list(set(lst))

a = [random.choice(range(1, 502)) for i in range(random.randint(20, 50))]
# a = [1,2,3,4,5,22,645,1234,23,123,545,23,1212,11,22,423,445,3,5,4,3,554,54564,5,5,64,5,6,456,456]
print(" Original list with duplicates (count:", len(a), "):", sorted(a))
print(" Using one-by-one removal ...")
print("  List with duplicates removed (count:", len(usingOnebyOne(a)), "):", sorted(usingOnebyOne(a)))
print(" Using in-build set function ...")
print("  List with duplicates removed (count:", len(usingSetFunc(a)), "):", sorted(usingSetFunc(a)))

