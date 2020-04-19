# Extension to Ex05 List Overlap

import random

print("")
print("Given two lists print the common elements within the two")
print("")

a = [random.choice(range(1, 520)) for i in range(110)]
b = [random.choice(range(1, 502)) for i in range(101)]
print("Common elements between 'a' and 'b': ", list(set([i for i in a if i in b])))
 
