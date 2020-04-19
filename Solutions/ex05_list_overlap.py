# Given two list print the common elements within the two.

print("")
print("Given two lists print the common elements within the two")
print("")

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
b = [1, 2, 3, 4, 5, 6, 7,  8,  9,  10, 11, 12,  13,  14]

# Two different ways, achieving same output

# Without using set in-build function
common = []
for cnt in range(len(a)):
    if a[cnt] in b and a[cnt] not in common:
        common.append(a[cnt])
 
print("List1: ", a, "\nList2: ", b)
print("Common elements in List1 and List2: ", common)

# With using set in-build function
a = set(a)
b = set(b)
print("Common elements in List1 and List2: ", list(a&b))

