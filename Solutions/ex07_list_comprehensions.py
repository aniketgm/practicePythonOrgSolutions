# Get only even elements from the list

# With list comprehensions this is very easy.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print("Original List : ", a)
print("Even elements : ", [i for i in a if (i%2 == 0)])
